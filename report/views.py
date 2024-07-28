from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.conf import settings
from .forms import LaporForm, CaptchaTestForm
from .models import Lapor, Foto
from geonode.geokincia.tasks import tambah_laporan_baru
from geonode.geokincia.utils import get_report_stat
from geonode.base.models import ResourceBase
from PIL import Image, ImageOps
from PIL.ExifTags import TAGS
from datetime import datetime
import uuid

def home(request):
    dataset = ResourceBase.objects.filter(resource_type='dataset').count()
    peta = ResourceBase.objects.filter(resource_type='map').count()
    laporan_baru, laporan_progress = get_report_stat()
    return render(request, 'home.html', {'dataset': dataset,
                                            'peta': peta, 
                                            'laporan_baru': laporan_baru,
                                            'laporan_progress': laporan_progress})

def pelaporan(request):
    if request.method == 'POST':
        lapor_form = LaporForm(request.POST, request.FILES)
        captcha_form = CaptchaTestForm(request.POST)

        if captcha_form.is_valid():
            if lapor_form.is_valid():
                lapor_form.instance.kondisi = request.POST.get('kondisi_objek') if request.POST.get('kondisi_objek') else request.POST.get('kondisi_rumah')
                if lapor_form.instance.kondisi:
                    lapor_form.save()
                    ds_new_laporan = to_dataset(request, lapor_form.instance.kondisi)
                    ds_new_laporan['___att'] = handle_file_upload(request.FILES.getlist('foto'), lapor_form.instance)
                    tambah_laporan_baru.delay(ds_new_laporan)
                    messages.success(request, 'Laporan Anda telah kami terima. Berikutnya petugas akan melakukan verikasi. Terimakasih atas pertisipasi Anda.')
                    return redirect('home')
                else:
                    messages.error(request, 'Kondisi object harus diisi.')
                
            else:
                messages.error(request, 'Formulir tidak valid. Silakan periksa kembali data Anda.')
        else:
            messages.error(request, 'Validasi Captcha gagal. Silahkan coba lagi.')
    else:
        lapor_form = LaporForm()
        captcha_form = CaptchaTestForm()

    context = {
        'form': lapor_form,
        'captcha_form': captcha_form
    }
    return render(request, 'pelaporan.html', context)

def handle_file_upload(files, lapor_instance):
    attachments = []
    IMG_SIZE = 720
    tgl = datetime.now().strftime("%a %d-%m-%Y")
    for foto in files:
        fs = FileSystemStorage(location=settings.GEOKINCIA['ATTACHMENT_DIR'])
        filename = fs.save(foto.name, foto)
        Foto.objects.create(lapor=lapor_instance, foto=filename)
        #resize
        try:
            with Image.open(fs.path(filename)) as img:
                img = ImageOps.exif_transpose(img)
                x, y = img.size
                ratio = IMG_SIZE / min(x,y)
                img = img.resize((int(x * ratio), int(y * ratio)))
                img.save(fs.path(filename), optimize=True, quality=90)
        except:
            pass
        attachments.append(f'{filename}#photo#{tgl}')
    return ';'.join(attachments)

def to_dataset(request, kondisi):
    return {
            'pelapor' : request.POST.get('pelapor').upper(),
            'nik' : request.POST.get('nik'),
            'email' : request.POST.get('email', ''),
            'nohp' : request.POST.get('nohp'),
            'jenis_pelaporan' : request.POST.get('jenis_pelaporan').upper(),
            'geom': f"multipoint(({request.POST.get('longitude')} {request.POST.get('latitude')}))",
            'kondisi' : kondisi.upper(),
            'status': 'BARU',
            'tgl_laporan': datetime.now().strftime('%d-%m-%Y'),
            'created_at': datetime.now().strftime('%d-%m-%Y'),
            'created_by': 'UMUM',
            '___id': str(uuid.uuid4())
    }
    

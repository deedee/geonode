from django import forms
from .models import Lapor
from captcha.fields import ReCaptchaField

class CaptchaTestForm(forms.Form):
    captcha_field=ReCaptchaField()

class LaporForm(forms.ModelForm):
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())
    foto = forms.FileField()
    class Meta:
        model = Lapor
        fields = ['pelapor', 'nik', 'email', 'nohp', 'jenis_pelaporan', 'lokasi', 'latitude', 'longitude']
        widgets = {
            'jenis_pelaporan': forms.Select(choices=[
                ('Jalan Lingkungan', 'Jalan Lingkungan'),
                ('Drainase Lingkungan', 'Drainase Lingkungan'),
                ('RTLH', 'Rumah Tidak Layak Huni (RTLH)')
            ]),
        }
from django.contrib import admin
# from django.utils.safestring import mark_safe
# from leaflet.admin import LeafletGeoAdmin
from .models import Lapor, Foto
# from .forms import LaporForm

admin.site.register(Lapor)
admin.site.register(Foto)

# class FotoInline(admin.TabularInline):
#     model = Foto
#     extra = 1
#     fields = ['display_image']
#     readonly_fields = ['display_image']
#     template = 'admin/edit_inline/tabular_no_delete.html'

#     def display_image(self, instance):
#         if instance.foto:
#             return mark_safe('<a href="{}" target="_blank"><img src="{}" width="100" height="auto" /></a>'.format(instance.foto.url, instance.foto.url))
#         else:
#             return ''

# @admin.register(Lapor)
# class LaporAdmin(LeafletGeoAdmin):
#     form = LaporForm
#     list_display = ("id", "tanggal_pelaporan", "pelapor", "jenis_pelaporan", "lokasi", "status")
#     list_filter = ("jenis_pelaporan", "status")
#     search_fields = ("pelapor", "nik", "email", "tanggal_pelaporan", "jenis_pelaporan", "lokasi", "status")
#     inlines = [FotoInline]

#     class Media:
#         js = ('https://unpkg.com/leaflet@1.7.1/dist/leaflet.js',)

#     def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
#         context['leaflet_lat'] = obj.latitude if obj else 0
#         context['leaflet_lng'] = obj.longitude if obj else 0
#         context['leaflet_address'] = obj.lokasi if obj else 'Address not available'
#         return super().render_change_form(request, context, add, change, form_url, obj)

# @admin.register(Foto)
# class FotoAdmin(admin.ModelAdmin):
#     list_display = ("id", "foto", "lapor_info")

#     def lapor_info(self, obj):
#         return f"Pelapor {obj.lapor.pelapor} - {obj.lapor.jenis_pelaporan} [{obj.lapor.status}]"

#     lapor_info.short_description = 'Informasi Pelaporan'

# @admin.register(Jalan)
# class JalanAdmin(admin.ModelAdmin):
#     list_display = ("id", "pelapor", "get_foto_images", "lokasi")
#     search_fields = ("lapor_id__pelapor", "lokasi", "kondisi")  
    
#     def get_lapor_pelapor(self, obj):
#         if obj.lapor_id and isinstance(obj.lapor_id, Lapor):
#             return obj.id.pelapor  
#         return None

#     get_lapor_pelapor.short_description = 'Pelapor'

#     def get_foto_images(self, obj):
#         if obj.lapor_id:  
#             fotos = Foto.objects.filter(lapor=obj.lapor_id)
#             if fotos.exists():
#                 return mark_safe('<br>'.join(['<img src="{}" width="100" height="auto" />'.format(foto.foto.url) for foto in fotos]))
#             else:
#                 return 'No photos'
#         return 'No photos' 

#     get_foto_images.short_description = 'Fotos'


# @admin.register(Drainase)
# class DrainaseAdmin(admin.ModelAdmin):
#     list_display = ("id", "pelapor", "get_foto_images", "lokasi")
#     search_fields = ("lapor_id__pelapor", "lokasi", "kondisi")  
    
#     def get_lapor_pelapor(self, obj):
#         if obj.lapor_id and isinstance(obj.lapor_id, Lapor):
#             return obj.id.pelapor  
#         return None

#     get_lapor_pelapor.short_description = 'Pelapor'

#     def get_foto_images(self, obj):
#         if obj.lapor_id: 
#             fotos = Foto.objects.filter(lapor=obj.lapor_id)
#             if fotos.exists():
#                 return mark_safe('<br>'.join(['<img src="{}" width="100" height="auto" />'.format(foto.foto.url) for foto in fotos]))
#             else:
#                 return 'No photos'
#         return 'No photos'  

#     get_foto_images.short_description = 'Fotos'


# @admin.register(Rtlh)
# class RtlhAdmin(admin.ModelAdmin):
#     list_display = ("id", "pelapor", "get_foto_images", "lokasi")
#     search_fields = ("lapor_id__pelapor", "lokasi", "kondisi") 
    
#     def get_lapor_pelapor(self, obj):
#         if obj.lapor_id and isinstance(obj.lapor_id, Lapor):
#             return obj.id.pelapor  
#         return None

#     get_lapor_pelapor.short_description = 'Pelapor'

#     def get_foto_images(self, obj):
#         if obj.lapor_id:  
#             fotos = Foto.objects.filter(lapor=obj.lapor_id)
#             if fotos.exists():
#                 return mark_safe('<br>'.join(['<img src="{}" width="100" height="auto" />'.format(foto.foto.url) for foto in fotos]))
#             else:
#                 return 'No photos'
#         return 'No photos' 

#     get_foto_images.short_description = 'Fotos'

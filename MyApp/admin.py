from django.contrib import admin
from MyApp.forms import User, UserCreationForm
from .models import  Indio_Solari,La_renga,LasPelotas,Divididos,Ciro,notvg, lugares, presentacion_divididos, presentacion_LaRenga,presentacion_Ciro,presentacion_LasPelotas,presentacion_ntvg




# Register your models here.

class imagenes_foto(admin.ModelAdmin):
    list_display = ('title', 'image', 'mostrar_imagen')


admin.site.register(Indio_Solari)
admin.site.register(La_renga)
admin.site.register(LasPelotas)
admin.site.register(Divididos)
admin.site.register(Ciro)
admin.site.register(notvg)
#presentaciones 
admin.site.register(lugares)
admin.site.register(presentacion_divididos)
admin.site.register(presentacion_LaRenga)
admin.site.register(presentacion_Ciro)
admin.site.register(presentacion_LasPelotas)
admin.site.register(presentacion_ntvg)
#admin.site.register(UserCreationForm)

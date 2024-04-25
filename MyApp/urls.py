from django.urls import path,include
from MyApp import views
from .views import RegistroView, InicioSesionView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name= 'Home'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('inicio-sesion/', InicioSesionView.as_view(), name='inicio-sesion'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('indio/', views.indio_solari_view, name='Indio'),
    path('LaRenga/', views.la_renga_view, name='LaRenga'),
    path('divididos/', views.divididos_view, name='Divididos'),
    path('laspelotas/', views.las_pelotas_view, name='LasPelotas'),
    path('ciro/', views.ciro_view, name='Ciro'),
    path('ntvg/', views.notvg_view, name='ntvg'),
    path('contacto/', views.contacto, name='contacto'),
    path('gracia/', views.gracais, name='gracia'),
    path('quienesSomos/', views.QuienesSomos, name='quienesSomos'),
    path('imagen/', views.imagen, name= 'imagen'),
    
    
    path('modificar-datos/', views.modificar_datos_usuario, name='modificar_datos_usuario'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='inicio/password_reset.html'), name= 'password_reset'),

    path('reset_password_done/',auth_views.PasswordResetDoneView.as_view(template_name='inicio/reset_password_sent.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view( template_name= 'inicio/restablecer_contraseña.html'), name= 'password_reset_confirm'),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'inicio/password_reset_complete.html'), name= 'password_reset_complete'),
]
    
    

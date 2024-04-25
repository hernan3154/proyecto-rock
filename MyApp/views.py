from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from .forms import RegistroForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import ModificarUsuarioForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from MyApp.forms import PasswordResetRequestForm
from django.utils import timezone
from datetime import timedelta
from .forms import PasswordResetRequestForm
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Indio_Solari, La_renga,Divididos,Ciro,notvg,LasPelotas,lugares

def home(request):
    return render(request, "index.html")

def imagen(request):
    return render(request, "fotos.html")






class RegistroView(FormView):
    template_name = "inicio/registro1.html"
    form_class = RegistroForm
    success_url = reverse_lazy("inicio-sesion")
    success_message = "Usuario registrado exitosamente."

    def form_valid(self, form):
        #Verifica si el correo electronico ya esta en uso
        email = form.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            messages.error(self.request, "El email ya está registrado.")
            return super().form_invalid(form)
        #Guardar el formulario si el correo electronico no esta en uso
        form.save()
        messages.success(self.request, "Usuario registrado exitosamente.")
        return super().form_valid(form)


class InicioSesionView(FormView):
    template_name = "inicio/inicio-sesion1.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy(
        "Home"
    )  # URL a la que redirigir despues del inicio de sesion

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return super().form_invalid(form)


#def logout_view(request):
#   logout(request)
#  return redirect("Home")

from django.shortcuts import redirect

def logout_view(request):
    response = redirect('Home')
    response.delete_cookie('sessionid')  # Borra la cookie de sesión
    return response



# Vista para mostrar la información de Indio Solari
def indio_solari_view(request):
    # Obtiene todos los objetos de Indio Solari desde la base de datos
    indio_solari_objects = Indio_Solari.objects.all()
    # Obtiene todos los objetos de lugares desde la base de datos
    lugares_objects = lugares.objects.all()
    # Renderiza la plantilla y pasa los objetos como contexto
    return render(request, 'indio.html', {'indio_solari_objects': indio_solari_objects, 'lugares': lugares_objects})

# Vista para mostrar la información de La Renga
def la_renga_view(request):
    # Obtiene todos los objetos de La Renga desde la base de datos
    la_renga_objects = La_renga.objects.all()
    # Renderiza la plantilla y pasa los objetos como contexto
    return render(request, 'LaRenga.html', {'la_renga_objects': la_renga_objects})

# Vista para mostrar la información de Divididos
def divididos_view(request):
    # Obtiene todos los objetos de Divididos desde la base de datos
    divididos_objects = Divididos.objects.all()
    # Renderiza la plantilla y pasa los objetos como contexto
    return render(request, 'Divididos.html', {'divididos_objects': divididos_objects})

# Vista para mostrar la información de Ciro
def ciro_view(request):
    # Obtiene todos los objetos de Ciro desde la base de datos
    ciro_objects = Ciro.objects.all()
    # Renderiza la plantilla y pasa los objetos como contexto
    return render(request, 'ciro.html', {'ciro_objects': ciro_objects})

# Vista para mostrar la información de notvg
def notvg_view(request):
    # Obtiene todos los objetos de notvg desde la base de datos
    notvg_objects = notvg.objects.all()
    # Renderiza la plantilla y pasa los objetos como contexto
    return render(request, 'ntvg.html', {'notvg_objects': notvg_objects})

# Vista para mostrar la información de Las Pelotas
def las_pelotas_view(request):
    # Obtiene todos los objetos de Las Pelotas desde la base de datos
    las_pelotas_objects = LasPelotas.objects.all()
    # Renderiza la plantilla y pasa los objetos como contexto
    return render(request, 'LasPelotas.html', {'las_pelotas_objects': las_pelotas_objects})


# esto modifica los datos del usuario
# *********************************************#
@login_required  # Requiere que el usuario esté autenticado
def modificar_datos_usuario(request):
    usuario = request.user  # Obtiene el usuario actual
    if request.method == "POST":  # Si el método es POST
        form = ModificarUsuarioForm(
            request.POST, instance=usuario
        )  # Crea un formulario con los datos del usuario
        if form.is_valid():  # Si el formulario es válido
            form.save()  # Guarda los cambios
            return redirect(
                "modificar_datos_usuario"
            )  # Redirige al perfil del usuario después de la modificación
    else:
        form = ModificarUsuarioForm(instance=usuario)
    return render(request, "inicio/modifica-usuario.html", {"form": form})


# ****************************************************************#


# Vista para el Proceso de Olvido de Contraseña:
# **********************************************#

def forgot_password(request):
    if request.method == "POST":   
        form = PasswordResetRequestForm(request.POST) 
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            if user is not None: 
                # Generar token de restablecimiento de contraseña
                token = get_random_string(length=32)
                user.password_reset_token = token 
                user.password_reset_token_created = timezone.now()
                user.save()
                # Enviar correo electrónico con el enlace de restablecimiento
                send_mail(
                    "Restablecer contraseña",
                    "Sigue este enlace para restablecer tu contraseña: http://127.0.0.1:8000/restablecer-password/{}/".format(
                        token
                    ),
                    "kraquen8686@gmail.com", 
                    [email],
                    fail_silently=False,
                )
                return redirect("inicio-sesion")
    else:
        form = PasswordResetRequestForm()
    return render(request, "olvido-contraseña.html", {"form": form})


#vista formulario de contacto 

def FormContacto(request):
    return render(request, 'formulario-de-contacto.html')

#**********************************************#
#vista para capturar los datos y enviar al mail 

def contacto(request):
    if request.method=='POST':

        miFormulario = ContactForm(request.POST)

        if miFormulario.is_valid():
            infForm = miFormulario.cleaned_data
            send_mail(infForm['nombre'],infForm['mensaje'], infForm.get('email', ' '),['kraquen8686@gmail.com'])
            return render(request,'gracias.html')
    else:
        miFormulario=ContactForm()
        
        return render(request, 'formulario-de-contacto.html', {'form':miFormulario})
    

def gracais(request):
    return render(request, 'gracias.html')

def QuienesSomos(request):
    return render(request,'quienes_somos.html')



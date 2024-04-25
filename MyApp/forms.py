from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm): 
    email = forms.EmailField()
    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ]


#modelo para modificar datos del usuario
class ModificarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



#Formulario de Olvido de Contraseña:
class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [ 'email']

# formulario de contacto 
class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Correo Electrónico', max_length=100)
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)



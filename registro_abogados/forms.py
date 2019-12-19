#==============================================================
# CONSTRUYENDO FORMAS EN DJANGO
#==============================================================

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.core.validators import RegexValidator

from .models import Municipio

class NameWidget(forms.MultiWidget):

    def __init__(self, attrs=None):       
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
        ], attrs)

    def decompress(self, value):
        # 'firstvalue secondvalue'
        if value:
            return value.split(' ')
        # 'firstvalue', secondvalue
        return ['nombre', 'apellido']


class NameField(forms.MultiValueField):

    widget = NameWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+', 'Ingrese un primer nombre valido (solo letras)')
            ]), # test
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+', 'Ingrese un segundo nombre valido (solo letras)')
            ]) # none
        )
        super().__init__(fields, *args, **kwargs)
    
    def compress(self, data_list):
        # data_List = ['firstvalue', 'secondvalue']
        return f'{data_list[0]} {data_list[1]}'



class FormularioAbogados(forms.Form):
    name = NameField()
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'category',
            'subject',
            'body',
            Submit('submit', 'Submit', css_class = 'btn-success')
        )


class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ('codigo_dane', 'departamento', 'municipio') 
        
#============================================================================================
#==> FORMA PARA REGISTRO DE USUARIO
#============================================================================================

STATES = (
    ('', 'Elegir rol...'), # esto es para prueba de campo de formulario registro usuario
    ('Co', 'Comercial...'),
    ('Jur', 'Juridico...'),
    ('Tec', 'Tecnologico...'),
    ('Op', 'Operaciones..')
)

class RegisterForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput)
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder':'1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Apartament, studio, or floor'})
    )
    city = forms.CharField
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

#===========================================================================================
#==> Forma para envio de correo desde plantilla contacto
class ContactoForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True)
     






 
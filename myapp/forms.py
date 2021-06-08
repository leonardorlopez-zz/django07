from django.forms import ModelForm, forms
from .models import Curso, Adidas

class FormularioCurso(ModelForm):
    class Meta:
        model = Curso
        fields = ("nombre", "inscriptos", "turno")

class FormularioAdidas(ModelForm):
    class Meta:
        model = Adidas
        fields = ("articulo", "talle")
 

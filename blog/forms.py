from django.forms import ModelForm
from blog.models import Perfil

class PostForm(ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
from django.forms import ModelForm
from app.models import Animals

class AnimalsForm(ModelForm):
    class Meta:
        model = Animals
        fields = ['owner', 'animalName', 'breed', 'contact']

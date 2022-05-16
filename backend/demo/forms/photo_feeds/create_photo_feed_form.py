from django import forms
from demo.models import PhotoFeedModel

class CreatePhotoFeedForm(forms.ModelForm):
    class Meta:
        model = PhotoFeedModel
        fields = (
            'description',
            'image'
        )
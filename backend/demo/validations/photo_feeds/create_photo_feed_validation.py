from django import forms
from django.core.validators import FileExtensionValidator


class CreatePhotoFeedValidation(forms.Form):
    description = forms.CharField(required=True)
    image = forms.FileField(
        required=True,
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png'])
        ]
    )
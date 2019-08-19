from django import forms

from .models import WeightFile, ImageFile

# class UploadFileForm(forms.ModelForm):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()


class WeightFileForm(forms.ModelForm):
    class Meta:
        model = WeightFile
        fields = ['title','weight_file']


class ImageFileForm(forms.ModelForm):
    class Meta:
        model = ImageFile
        fields = ['title', 'image_file']

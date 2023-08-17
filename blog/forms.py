from django import forms
from .models import Blog

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['content'].strip = False
    class Meta:
        model = Blog
        fields = ('title','content', 'image')
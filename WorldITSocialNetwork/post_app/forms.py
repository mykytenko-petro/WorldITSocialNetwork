from django import forms
from .models import Post, Tag

MAX_COMPRESSED_IMAGE_SIZE = 5 * 1024 * 1024

class MultipleFieldInput(forms.ClearableFileInput):
    allow_multiple_selection = True
    
class MultipleFileField(forms.FileField):
    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(file, initial) for file in data]
        return single_file_clean(data, initial)
    
class PostCreationForm(forms.ModelForm):
    
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    urls = forms.URLField(required=True)
    
    image = MultipleFileField(
        required=False,
        widget=MultipleFieldInput(attrs={'accept': 'image/*'})
    )
    
    class Meta:
        model = Post
        fields = ('title', 'topic', 'content')
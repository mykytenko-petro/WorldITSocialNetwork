from django import forms

from .models import Post, Tag, PostImage, PostLink
from .utils import compress_image


class HashPrefixModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return f"#{obj}"

class MultipleFieldInput(forms.ClearableFileInput):
    allow_multiple_selection = True
    
class MultipleFileField(forms.FileField):
    def clean(self, data, initial = None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(file, initial) for file in data]

        return single_file_clean(data, initial)

class PostCreationForm(forms.ModelForm):
    tags = HashPrefixModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Post
        fields = ('title', 'topic', 'content', 'tags')
        
        labels = {
            'title': 'Назва публікації',
            'topic': 'Тема публікації',
        }
        widgets = {
            'title': forms.TextInput(attrs= {'placeholder': 'Природа, книга і спокій 🌿'}),
            'topic': forms.TextInput(attrs= {'placeholder': 'Напишіть тему публікації'}),
            'content': forms.Textarea(attrs= {'rows': 5})
        }
    
    def __init__(self, links: list | None = None, images= None, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def save(self, author: AbstractUser): # type: ignore
        post: Post = super().save(commit= False)
        post.author = author
        post.save()
        self.save_m2m()
        
        return post
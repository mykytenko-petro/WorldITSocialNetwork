from typing import Any

from django import forms
from django.contrib.auth.models import AbstractUser

from .models import Post, Tag, PostImage, PostLink
from .utils import compress_image


# custom fields
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

# forms
class PostCreationForm(forms.ModelForm):
    tags = HashPrefixModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Post
        fields = ('title', 'topic', 'content', 'tags')
        
        widgets = {
            'title': forms.TextInput(attrs= {'placeholder': 'Природа, книга і спокій 🌿'}),
            'topic': forms.TextInput(attrs= {'placeholder': 'Напишіть тему публікації'}),
            'content': forms.Textarea(attrs= {'rows': 5, 'placeholder': 'Текст публікації'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.links = []
        self.images = []

    def clean(self) -> dict[str, Any]:
        # links
        links: list | None = self.data.getlist('links')  # type: ignore
        url_validator = forms.URLField()

        if links:
            for link in links:
                try:
                    url_validator.clean(link)
                    self.links.append(link)

                except forms.ValidationError:
                    self.add_error('links', f"Некоректне посилання: {link}")

        # TODO: images

        return super().clean()

    def save(self, author: AbstractUser): # type: ignore
        post: Post = super().save(commit=False)

        # user
        post.author = author

        post.save()
        self.save_m2m()

        # links
        for url in self.links:
            PostLink.objects.create(post=post, url=url)
        
        # TODO: images

        return post
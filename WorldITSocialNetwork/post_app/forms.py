from typing import Any

from django import forms
from django.contrib.auth.models import AbstractUser

from .models import Post, Tag, PostImage, PostLink
from .utils import compress_image


# custom fields
class HashPrefixModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return f"#{obj}"

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

        self.link_list = []
        self.image_list = []

    def clean(self) -> dict[str, Any]:
        # links
        try:
            links: list = self.data.getlist('links')  # type: ignore
            url_validator = forms.URLField()

            if links:
                for link in links:
                    try:
                        url_validator.clean(link)
                        self.link_list.append(link)

                    except forms.ValidationError:
                        self.add_error('links', f"Некоректне посилання: {link}")
        except ValueError:
            pass

        try:
            image_validator = forms.ImageField()
            images = self.files.getlist('images')
        
            for image in images:
                try:
                    image_validator.clean(image)
                except forms.ValidationError:
                    self.add_error('images', "Завантажте коректне зображення")
        except ValueError:
            pass

        return super().clean()

    def save(self, author: AbstractUser): # type: ignore
        post: Post = super().save(commit=False)

        # user
        post.author = author

        post.save()
        self.save_m2m()

        # links
        for url in self.link_list:
            PostLink.objects.create(post=post, url=url)
        
        images = self.files.getlist('images')
        print(images)

        for image in images:
            PostImage.objects.create(
                post=post,
                original_image=image,
                compressed_image=compress_image(image) # type: ignore
            )

        return post
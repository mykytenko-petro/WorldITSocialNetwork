from django import forms

from .models import Post, Tag, PostImage, PostLink
from .utils import compress_image


class MultipleFieldInput(forms.ClearableFileInput):
    allow_multiple_selection = True
    
class MultipleFileField(forms.FileField):
    def clean(self, data, initial = None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(file, initial) for file in data]

        return single_file_clean(data, initial) 
    
class PostCreationForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        required = False,
        queryset= Tag.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )
    images = MultipleFileField(
        required=False,
        widget=MultipleFieldInput(attrs={
            'accept': 'image/*'
        })
    )

    class Meta:
        model = Post
        fields = ('title', 'topic', 'content')
        
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

        self.fields['tags'].queryset = Tag.objects.all() # type: ignore

        self.links_list = []
        self.images_list = []

        if links is None:
            links = []

        for link in links:
            clean_link = link.strip()
            if clean_link:
                self.links_list.append(clean_link)
        
        if images is not None:
            self.images_list = list(images)
        
    def clean(self):
        cleaned_data = super().clean()

        url_field = forms.URLField()
        image_field = forms.ImageField()

        for link in self.links_list:
            try:
                url_field.clean(link)
            except forms.ValidationError:
                self.add_error('links', f'Некоректне посиланння: {link}')
                
        for image in self.images_list:
            try:
                image_field.clean(image)
            except forms.ValidationError:
                self.add_error('images', 'Завантажте коректне зображення')
                
        return cleaned_data
    
    def save(self, author): # type: ignore
        post = super().save(commit= False)
        post.author = author

        post.save()
        post.tags.set(self.cleaned_data['tags'])

        for url in self.links_list:
            PostLink.objects.create(post= post, url= url)

        for image in self.images_list:
            PostImage.objects.create(
                post= post,
                original= image,
                compressed=compress_image(image)
            )
        
        return post
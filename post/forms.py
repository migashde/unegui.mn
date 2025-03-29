from django import forms
from .models import Post, PostImage
from django.forms import inlineformset_factory
import uuid


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content', 'price', 'category']
        labels = {
            'subject': 'Гарчиг',
            'content': 'Агуулга',
            'price': 'Үнэ',
            'category': 'Ангилал',
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.post_number = uuid.uuid4()  # Generate UUID here
        if commit:
            instance.save()
        return instance

PostImageFormSet = inlineformset_factory(
    Post,
    PostImage,
    fields=('img',),
    extra=3,
    can_delete=False,
    labels={
        'img': 'Зураг',
    }
)

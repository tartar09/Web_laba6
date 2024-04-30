from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import Category, Characteristics, Recipes
from django.core.validators import MinLengthValidator, MaxLengthValidator


class UploadFileForm(forms.Form):
    file = forms.FileField(label="файл")


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 empty_label="Категория не выбрана", label="Категории")

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов')
        return title

    class Meta:
        model = Recipes
        fields = ['title', 'slug', 'content', 'is_published',
                  'cat', 'tags', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

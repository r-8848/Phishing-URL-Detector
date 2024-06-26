from django import forms
from django.forms import TextInput, NumberInput
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Review

class ReviewForm(forms.ModelForm):
    stars = forms.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        widget=NumberInput(attrs={
            'class': 'form-control',
            'min': 1,
            'max': 5
        })
    )

    class Meta:
        model = Review
        fields = ['stars', 'name', 'review_text']
        widgets = {
            'review_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter your review here...'
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'size': 20,
                'placeholder': 'Enter your name'
            }),
        }

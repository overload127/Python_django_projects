from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Формаотзывов"""
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')

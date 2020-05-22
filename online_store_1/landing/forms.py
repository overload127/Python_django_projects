from django import forms
from . import models


class SubscriberForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SubscriberForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control m-1'

    class Meta:
        model = models.Subscriber
        exclude = ['']
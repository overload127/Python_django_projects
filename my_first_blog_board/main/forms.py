from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import AdvUser


class RegisterAdvUserForm(forms.ModelForm):

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'password')


class AdvUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = AdvUser
        fields = ['username', 'password']


class ChangeAdvUserInfoForm(forms.ModelForm):
    email = forms.EmailField(
        required=True, label='Адрес электронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'send_message')

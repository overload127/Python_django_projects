from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', initial='undefined',
                           help_text='Введите свое имя')
    age = forms.IntegerField(
        label='Комментарий', 
        widget=forms.Textarea,
        initial=18,
        help_text='Введите свой возраст',
        required=False,
        max_value=100,
        min_value=1)
    field_order = ['age', 'name']

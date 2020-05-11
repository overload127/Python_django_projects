from django.forms import ModelForm
from django.views.generic.edit import FormView
from django.urls import reverse

from .models import Bb, Rubric


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')


class BbAddView(FormView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    initial = {'price': 0.0}

    def get_context_data(self, *args, **kvargs):
        context = super().get_context_data(*args, **kvargs)
        context['rubrics'] = Rubric.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse(
            'bboard:by_rubric',
            kwargs={'rubric_id': self.object.cleaned_data['rubric'].pk})

from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin, CreateView
from django.views.generic.list import ListView

from sins.forms import VoteForCost, AboutQuestionnaire, CreateYourSinForm
from sins.models import Sin, Sinner


class SinListView(ListView):
    model = Sin
    template_name = "sin-list.html"

    def post(self, request, *args, **kwargs):
        sinner = get_object_or_404(Sinner, id=request.session['sinner_id'])
        sins_id = request.POST['sins']
        for sin_id in sins_id:
            sinner.sin_set.add(sin_id)
        sinner.save()
        return redirect(reverse('sin-create'))


class SinsListMale(SinListView):
    def get_queryset(self):
        self.model.objects.filter(target_sex=Sin.MALE).order_by('cost')


class SinsListFemale(SinListView):
    def get_queryset(self):
        return self.model.objects.filter(target_sex=Sin.FEMALE).order_by('cost')


class SinDetailView(FormMixin, DetailView):
    model = Sin
    template_name = "sin-detail.html"
    form_class = VoteForCost


class IndexPageView(FormMixin, TemplateView):
    template_name = 'index.html'
    form_class = AboutQuestionnaire

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            sinner_object = Sinner.objects.get_or_create(
                age=cd['age'],
                sex=cd['sex'],
                occupation=cd['occupation'],
                country_of_residence=cd['country_of_residence'],
                religion=cd['religion']
            )
            request.session['sinner_id'] = sinner_object[0].id
            request.session['created'] = sinner_object[1]
            if sinner_object.sex == Sinner.MALE:
                return redirect(reverse('male-sin-list'))
            elif sinner_object.sex == Sinner.FEMALE:
                return redirect(reverse('female-sin-list'))
            else:
                return redirect(reverse('sin-list'))
        return render(request, self.template_name, context={'form': form})


class SinCreateView(CreateView):
    model = Sin
    template_name = "sin-create.html"
    form_class = CreateYourSinForm

from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin, CreateView
from django.views.generic.list import ListView

from sins.forms import VoteForCost, AboutQuestionnaire
from sins.models import Sin


class SinListView(FormMixin, ListView):
    model = Sin
    template = "sin-list"

    def post(self, request, *args, **kwargs):
        for key, value in request.POST:
            pass


class SinsListMale(SinListView):
    def get_queryset(self):
        self.model.objects.filter(target_sex=Sin.MALE).order_by('cost')


class SinsListFemale(SinListView):
    def get_queryset(self):
        return self.model.objects.filter(target_sex=Sin.FEMALE).order_by('cost')


class SinDetailView(FormMixin, DetailView):
    model = Sin
    template = "sin-detail"
    form_class = VoteForCost


class IndexPageView(FormMixin, TemplateView):
    template = 'index'
    form_class = AboutQuestionnaire


class SinCreateView(CreateView):
    model = Sin
    template = "sin-create"

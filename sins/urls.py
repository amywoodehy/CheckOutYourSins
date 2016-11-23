from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
    url(r'^$', views.IndexPageView.as_view(), name='index-page'),
    url(r'^u/$', views.SinListView.as_view(), name='sin-list'),
    url(r'^m/$', views.SinsListMale.as_view(), name='male-sin-list'),
    url(r'^f/$', views.SinsListFemale.as_view(), name='female-sin-list'),
    url(r'^s/(?P<pk>\d+)/$', views.SinDetailView.as_view(), name='sin-detail'),
    url(r'^create/$', views.SinCreateView.as_view(), name='sin-create'),
    url(r'^about/$', RedirectView.as_view(url='https://about.me/amywoodehy'), name='about')
]

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexPageView.as_view(), name='index-page'),
    url(r'^m/$', views.SinsListMale.as_view(), name='male-sin-list'),
    url(r'^f/$', views.SinsListFemale.as_view(), name='female-sin-list'),
    url(r'^s/(?P<id>\d+)/$', views.SinDetailView.as_view(), name='sin-detail'),
    url(r'^create/$', views.SinCreateView.as_view(), name='sin-create')
]

from django.conf import settings
from django.conf.urls import patterns, url
from three_d_viewer import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/$', views.MineralDetailView.as_view(), name='mineral_detail'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)

from django.conf import settings
from django.conf.urls import patterns, url
from django.views import generic
from three_d_viewer import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^$', generic.TemplateView.as_view(template_name="three_d_viewer/home.html"), name='home'),
    url(r'^minerals_theory/$', generic.TemplateView.as_view(template_name="three_d_viewer/minerals_theory.html"), name='minerals_theory'),
    url(r'^minerals_practice/$', views.MineralPracticeView.as_view(template_name="three_d_viewer/minerals_practice.html"), name='minerals_practice'),
    url(r'^minerals_selftest/$', generic.TemplateView.as_view(template_name="three_d_viewer/minerals_selftest.html"), name='minerals_selftest'),
    url(r'^minerals/(?P<pk>\d+)/$', views.MineralPracticeView.as_view(), name='mineral_detail'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^minerals/(?P<pk>\d+)/$', views.MineralDetailView.as_view(), name='mineral_detail'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)

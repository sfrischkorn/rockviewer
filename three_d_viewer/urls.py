from django.conf import settings
from django.conf.urls import patterns, url
from django.views import generic
from three_d_viewer import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^$', generic.TemplateView.as_view(template_name="three_d_viewer/home.html"), name='home'),
    url(r'^theory/structure/$', generic.TemplateView.as_view(template_name="three_d_viewer/theory/structure.html"), name='theory_structure'),
    url(r'^theory/bowen/$', generic.TemplateView.as_view(template_name="three_d_viewer/theory/bowen.html"), name='theory_bowen'),
    url(r'^theory/pressure_temp/$', generic.TemplateView.as_view(template_name="three_d_viewer/theory/pressure_temp.html"), name='theory_pt'),
    url(r'^minerals_practice/$', views.MineralPracticeView.as_view(template_name="three_d_viewer/minerals_practice.html"), name='minerals_practice'),
    url(r'^minerals/(?P<pk>\d+)/$', views.MineralDetailView.as_view(), name='mineral_detail'),
    url(r'^minerals_selftest/$', generic.TemplateView.as_view(template_name="three_d_viewer/minerals_selftest.html"), name='minerals_selftest'),
    url(r'^rock_practice/$', views.RockPracticeView.as_view(), name='rocks_practice'),
    url(r'^rocks/(?P<pk>\d+)/$', views.RockDetailView.as_view(), name='rock_detail'),
    url(r'^fossil_practice/$', views.FossilPracticeView.as_view(), name='fossil_practice'),
    url(r'^fossils/(?P<pk>\d+)/$', views.FossilDetailView.as_view(), name='fossil_detail'),
    url(r'^glossary/$', views.GlossaryView.as_view(), name='glossary'),
    url(r'^acknowledgements/$', generic.TemplateView.as_view(template_name='three_d_viewer/acknowledgements.html'), name='acknowledgements'),
    url(r'^erb101/$', views.ERB101HomeView.as_view(), name='erb101_home'),
    url(r'^erb101/$', generic.TemplateView.as_view(template_name="three_d_viewer/erb101/home.html"), name='erb101_home'),
    url(r'^erb101_rock_practice/$', views.ERB101RockPracticeView.as_view(), name='erb101_rocks_practice'),
    url(r'^erb101_minerals_practice/$', views.ERB101MineralPracticeView.as_view(), name='erb101_minerals_practice'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)

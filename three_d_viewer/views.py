"""
Define the views for the Django MVC
"""

from django import template
from django.views import generic

from three_d_viewer.models import Sample, Category, Mineral
register = template.Library()


class HomeView(generic.ListView):
    """
    Show the home page
    """

    template_name = 'three_d_viewer/home.html'
    model = Sample

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['active_samples'] = Sample.objects.select_subclasses(Mineral).filter(active=True).order_by('name')
        context['parent_categories'] = Category.objects.filter(parent=None). \
            filter(active=True).order_by('name')
        return context



class DetailView(generic.DetailView):
    """
    Define the view to view the 3D model of a sample
    """

    model = Sample
    template_name = 'three_d_viewer/detail.html'
    parent_categories = Category.objects.filter(parent=None). \
        filter(active=True).order_by("name")

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['active_samples'] = Sample.objects.select_subclasses(Mineral).filter(active=True).order_by('name')
        context['parent_categories'] = Category.objects.filter(parent=None). \
            filter(active=True).order_by('name')
        return context

class MineralDetailView(DetailView):
    """
    Add extra functionality for mineral details
    """

    model = Mineral
    template_name = 'three_d_viewer/mineral_detail.html'

    parent_categories = Category.objects.filter(parent=None). \
        filter(active=True).order_by("name")

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['active_samples'] = Sample.objects.select_subclasses(Mineral).filter(active=True).order_by('name')
        context['parent_categories'] = Category.objects.filter(parent=None). \
            filter(active=True).order_by('name')
        return context
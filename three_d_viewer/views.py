"""
Define the views for the Django MVC
"""

from django import template
from django.views import generic
from itertools import chain
from operator import attrgetter

from three_d_viewer.models import Sample, Category, Mineral, GlossaryEntry
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

class MineralPracticeView(generic.ListView):
    model = Mineral
    template_name = 'three_d_viewer/minerals_practice.html'

    def get_context_data(self, **kwargs):
        context = super(MineralPracticeView, self).get_context_data(**kwargs)
        cat = Category.objects.get(name='Minerals')
        result = cat.active_samples

        for child in cat.active_children:
            result = chain(result, child.active_samples)

        context['active_samples'] = sorted(result, key=attrgetter('name'))
        return context

class MineralDetailView(generic.DetailView):
    """
    Add extra functionality for mineral details
    """

    model = Mineral
    template_name = 'three_d_viewer/mineral_detail.html'

    parent_categories = Category.objects.filter(parent=None). \
        filter(active=True).order_by("name")

    def get_context_data(self, **kwargs):
        context = super(MineralDetailView, self).get_context_data(**kwargs)
        cat = Category.objects.get(name='Minerals')
        result = cat.active_samples

        for child in cat.active_children:
            result = chain(result, child.active_samples)

        context['active_samples'] = sorted(result, key=attrgetter('name'))
        return context

class RockPracticeView(generic.ListView):
    model = Sample
    template_name = 'three_d_viewer/rock_practice.html'

    parent_categories = Category.objects.filter(parent=None). \
        filter(active=True).order_by("name")


    def get_context_data(self, **kwargs):
        context = super(RockPracticeView, self).get_context_data(**kwargs)
        cat = Category.objects.get(name='Rocks')
        result = cat.active_samples

        for child in cat.active_children:
            result = chain(result, child.active_samples)

        context['active_samples'] = sorted(result, key=attrgetter('name'))
        return context

class RockDetailView(generic.DetailView):
    model = Sample
    template_name = 'three_d_viewer/rock_detail.html'

    parent_categories = Category.objects.filter(parent=None). \
        filter(active=True).order_by("name")


    def get_context_data(self, **kwargs):
        context = super(RockDetailView, self).get_context_data(**kwargs)
        cat = Category.objects.get(name='Rocks')
        result = cat.active_samples

        for child in cat.active_children:
            result = chain(result, child.active_samples)

        context['active_samples'] = sorted(result, key=attrgetter('name'))
        return context

class FossilPracticeView(generic.ListView):
    model = Sample
    template_name = 'three_d_viewer/fossil_practice.html'

    parent_categories = Category.objects.filter(parent=None). \
        filter(active=True).order_by("name")


    def get_context_data(self, **kwargs):
        context = super(FossilPracticeView, self).get_context_data(**kwargs)
        cat = Category.objects.get(name='Fossils')
        result = cat.active_samples

        for child in cat.active_children:
            result = chain(result, child.active_samples)

        context['active_samples'] = sorted(result, key=attrgetter('name'))
        return context

class FossilDetailView(generic.DetailView):
    model = Sample
    template_name = 'three_d_viewer/fossil_detail.html'

    parent_categories = Category.objects.filter(parent=None). \
        filter(active=True).order_by("name")


    def get_context_data(self, **kwargs):
        context = super(FossilDetailView, self).get_context_data(**kwargs)
        cat = Category.objects.get(name='Fossils')
        result = cat.active_samples

        for child in cat.active_children:
            result = chain(result, child.active_samples)

        context['active_samples'] = sorted(result, key=attrgetter('name'))
        return context
	
class GlossaryView(generic.ListView):
	model = GlossaryEntry
	template_name = 'three_d_viewer/glossary.html'
	
	def get_context_data(self, **kwargs):
	    context = super(GlossaryView, self).get_context_data(**kwargs)
	    context['entries'] = GlossaryEntry.objects.all()
	    return context

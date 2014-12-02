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
        context['base_template'] = 'three_d_viewer/base.html'
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
        context['base_template'] = 'three_d_viewer/base.html'
        return context

    def get_object(self, queryset=None):
        object = super(MineralDetailView, self).get_object()
        object.viewed_count += 1
        object.save()
        return object

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
        context['base_template'] = 'three_d_viewer/base.html'
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
        context['base_template'] = 'three_d_viewer/base.html'
        return context

    def get_object(self, queryset=None):
        object = super(RockDetailView, self).get_object()
        object.viewed_count += 1
        object.save()
        return object

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
        context['base_template'] = 'three_d_viewer/base.html'
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
        context['base_template'] = 'three_d_viewer/base.html'
        return context

    def get_object(self, queryset=None):
        object = super(FossilDetailView, self).get_object()
        object.viewed_count += 1
        object.save()
        return object
	
class GlossaryView(generic.ListView):
	model = GlossaryEntry
	template_name = 'three_d_viewer/glossary.html'
	
	def get_context_data(self, **kwargs):
	    context = super(GlossaryView, self).get_context_data(**kwargs)
	    context['entries'] = GlossaryEntry.objects.all().order_by("name")
	    return context
        
class ERB101HomeView(generic.ListView):
    """
    Show the home page
    """

    template_name = 'three_d_viewer/erb101/home.html'
    model = Sample

    def get_context_data(self, **kwargs):
        context = super(ERB101HomeView, self).get_context_data(**kwargs)
        context['active_samples'] = Sample.objects.select_subclasses(Mineral).filter(active=True).filter(erb101_sample=True).order_by('name')
        context['parent_categories'] = Category.objects.filter(parent=None). \
            filter(active=True).order_by('name')
        return context  

class ERB101MineralPracticeView(generic.ListView):
    model = Mineral
    template_name = 'three_d_viewer/erb101/minerals_practice.html'

    def get_context_data(self, **kwargs):
        context = super(ERB101MineralPracticeView, self).get_context_data(**kwargs)
        cat = Category.objects.get(name='Minerals')
        result = cat.active_101_samples

        for child in cat.active_children:
            result = chain(result, child.active_101_samples)

        context['active_samples'] = sorted(result, key=attrgetter('name'))
        context['base_template'] = 'three_d_viewer/erb101/base.html'
        return context
        
class ERB101MineralDetailView(generic.DetailView):
    """
    Add extra functionality for mineral details
    """

    model = Mineral
    template_name = 'three_d_viewer/erb101/mineral_detail.html'

    parent_categories = Category.objects.filter(parent=None). \
        filter(active=True).order_by("name")

    def get_context_data(self, **kwargs):
        context = super(ERB101MineralDetailView, self).get_context_data(**kwargs)
        cat = Category.objects.get(name='Minerals')
        result = cat.active_samples

        for child in cat.active_children:
            result = chain(result, child.active_samples)

        context['active_samples'] = sorted(result, key=attrgetter('name'))
        context['base_template'] = 'three_d_viewer/erb101/base.html'
        return context

    def get_object(self, queryset=None):
        object = super(ERB101MineralDetailView, self).get_object()
        object.viewed_count += 1
        object.save()
        return object     
        
class ERB101RockPracticeView(generic.ListView):
    model = Sample
    template_name = 'three_d_viewer/erb101/rock_practice.html'

    parent_categories = Category.objects.filter(parent=None). \
        filter(active=True).order_by("name")


    def get_context_data(self, **kwargs):
        context = super(ERB101RockPracticeView, self).get_context_data(**kwargs)
        cat = Category.objects.get(name='Rocks')
        result = cat.active_101_samples

        for child in cat.active_children:
            result = chain(result, child.active_101_samples)
        
        context['active_samples'] = sorted(result, key=attrgetter('name'))
        context['base_template'] = 'three_d_viewer/erb101/base.html'
        return context
        
        
class ERB101RockDetailView(generic.DetailView):
    model = Sample
    template_name = 'three_d_viewer/erb101/rock_detail.html'

    parent_categories = Category.objects.filter(parent=None). \
        filter(active=True).order_by("name")


    def get_context_data(self, **kwargs):
        context = super(ERB101RockDetailView, self).get_context_data(**kwargs)
        cat = Category.objects.get(name='Rocks')
        result = cat.active_samples

        for child in cat.active_children:
            result = chain(result, child.active_samples)

        context['active_samples'] = sorted(result, key=attrgetter('name'))
        context['base_template'] = 'three_d_viewer/erb101/base.html'
        return context

    def get_object(self, queryset=None):
        object = super(ERB101RockDetailView, self).get_object()
        object.viewed_count += 1
        object.save()
        return object
        
class TheoryTemplateView(generic.TemplateView):

    def get_context_data(self, **kwargs):
        context = super(TheoryTemplateView, self).get_context_data(**kwargs)
        context['base_template'] = 'three_d_viewer/base.html'
        context['olivine'] = Mineral.objects.filter(name='Olivine')[0]
        context['quartz'] = Mineral.objects.filter(name='Quartz')[0]
        context['microcline'] = Mineral.objects.filter(name='Microcline')[0]
        context['plag'] = Mineral.objects.filter(name='Plagioclase')[0]
        return context
 
class ERB101TheoryTemplateView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        context = super(ERB101TheoryTemplateView, self).get_context_data(**kwargs)
        context['base_template'] = 'three_d_viewer/erb101/base.html'
        return context
        

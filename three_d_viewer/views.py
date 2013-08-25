"""
Define the views for the Django MVC
"""

from django import template
from django.views import generic

from three_d_viewer.models import Sample
register = template.Library()


@register.inclusion_tag('children.html')
def children_tag(category):
    children = category.children.all()
    return {'children': children}


class IndexView(generic.ListView):
    """
    Define the page to display the Sample objects that can be viewed
    """
    template_name = 'three_d_viewer/index.html'
    context_object_name = 'active_samples'

    def get_queryset(self):
        """
        Return the active samples
        """
        return Sample.objects.filter(active=True)


class DetailView(generic.DetailView):
    """
    Define the view to view the 3D model of a sample
    """
    model = Sample
    template_name = 'three_d_viewer/detail.html'

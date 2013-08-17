from django import template
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from three_d_viewer.models import Sample
register = template.Library()


@register.inclusion_tag('children.html')
def children_tag(category):
    children = category.children.all()
    return {'children': children}


class IndexView(generic.ListView):
    template_name = 'three_d_viewer/index.html'
    context_object_name = 'active_samples'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """
        return Sample.objects.filter(active=True)


class DetailView(generic.DetailView):
    model = Sample
    template_name = 'three_d_viewer/detail.html'

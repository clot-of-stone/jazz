from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    objects_list = \
        Student.objects.all().order_by(ordering).prefetch_related('teachers')
    context = {'objects_list': objects_list}
    return render(request, template, context)

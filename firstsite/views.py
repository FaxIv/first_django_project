# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Notes


def index(request):
    template = loader.get_template('notes/index.html')
    notes = Notes.objects.order_by('-date')
    context = {'notes': notes}
    return HttpResponse(template.render(context, request))

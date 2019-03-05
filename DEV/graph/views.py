

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.template import loader
import os, json

def viewgraph(request):
    template = loader.get_template('graph/graph.html')
    context = {'The bubble graoh will be':
    1}
    return HttpResponse(template.render(context,request))

from decimal import Context

from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


# Create your views here.
def homepage(request):

    t = get_template('home.html')
    c = Context()
    return HttpResponse(t.render(c))
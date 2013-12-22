'''
Created on Dec 19, 2013

@author: cyrano821
'''

import datetime
import os

from django.http import HttpResponse
from django.http.response import Http404
from django.template.base import Template
from django.template.context import Context
from django.template.loader import get_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


def checkList(request):
    t = get_template('checklist.html')
    c = Context({})
    return HttpResponse(t.render(c))

def hello(request):
    
    header = "<head><body>"
    text = "OH YEA"
    footer = "</body></head>"
    return HttpResponse(header+text+text+footer)


def homepage(request):
    return HttpResponse("HOME")

def currentTime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hoursAhead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def template(request, name):
#     t = Template("""
#         {{ name }}
#         
#         {% if name %}
#             BAR IS TRUE
#         {% endif %}
#         
#     """)
    True
    t = get_template('temp.html')
    c = Context({"name":name})
    return HttpResponse(t.render(c))


def test(request):
    t = get_template('test.html')    
    return HttpResponse(t.render(Context({})))


def myName(request, name):
    return HttpResponse("Hello, " + name)

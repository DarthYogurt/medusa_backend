'''
Created on Dec 19, 2013

@author: cyrano821
'''

import datetime
import json
import operator
import os

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.http.response import Http404
from django.template.base import Template
from django.template.context import Context
from django.template.loader import get_template

from soplog.models import *


def checkList(request):
    #get groups
    variables = {}
    variables['group'] = []
    
    g = Group.objects.all()
    for item in g:
        temp = {}
        temp['id'] = item.id
        temp['name'] = item.name
        variables['group'].append(temp)
    
    variables['checklist']=[]
    c = Checklist.objects.all()
    for item in c:
        temp = {}
        temp['id'] = item.id
        temp['name'] = item.name
        temp['groupId'] = item.groupId.id
        variables['checklist'].append(temp)
        
    variables['checklistStep']=[]
    s = ChecklistStep.objects.all()
    for item in s:
        temp = {}
        temp['checklistId'] = item.checklistId.id
        temp['id'] = item.id
        temp['name'] = item.name
        temp['stepType'] = item.stepTypeId.name
        variables['checklistStep'].append(temp)
    
    t = get_template('checklist.html')
    c = Context(variables)
    return HttpResponse(t.render(c))


def checklistSearchByGroup(request, groupId):
    #lookup by groupId
    checklists = Checklist.objects.filter(groupId=groupId)
    j = {}
    j['groupId'] = groupId
    j['checklist'] = []
    
    for item in checklists:
        temp = {}
        temp['name'] = item.name
        temp['id'] = item.id
        j['checklist'].append(temp)    
    return HttpResponse(json.dumps(j))

def checklistSteps(request, checklistId):
    steps = ChecklistStep.objects.filter(checklistId = checklistId).order_by('stepNumber')
    j = {}
    j['checklistId'] = checklistId
    j['steps'] = []
    if len(steps) > 0:
        j['checklistName'] = steps[0].checklistId.name
    else:
        j['error'] = "No Results"
    for step in steps:
        temp = {}
        temp['name'] = step.name
        temp['id'] = step.id
        temp['stepNumber'] = step.stepNumber
        temp['stepType'] = step.stepTypeId.name
        j['steps'].append(temp)
    return HttpResponse(json.dumps(j))

# def hello(request):
#     
#     header = "<head><body>"
#     text = "OH YEA"
#     footer = "</body></head>"
#     return HttpResponse(header+text+text+footer)


# def currentTime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)
# 
# def hoursAhead(request, offset):
#     try:
#         offset = int(offset)
#     except ValueError:
#         raise Http404()
#     dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#     html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
#     return HttpResponse(html)


# def template(request, name):
# #     t = Template("""
# #         {{ name }}
# #         
# #         {% if name %}
# #             BAR IS TRUE
# #         {% endif %}
# #         
# #     """)
#     True
#     t = get_template('temp.html')
#     c = Context({"name":name})
#     return HttpResponse(t.render(c))


# def homepage(request):
#     return HttpResponse("HOME")
# 
# 
# def test(request):
#     t = get_template('test.html')    
#     return HttpResponse(t.render(Context({})))
# 
# 
# def myName(request, name):
#     return HttpResponse("Hello, " + name)

    

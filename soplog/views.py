from decimal import Context
import json

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.http.response import Http404, HttpResponse
from django.template.base import Template
from django.template.context import Context
from django.template.loader import get_template, get_template


from soplog.models import *



from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def testPost(request):
    #a = request.GET['alpha']
    #a = request.POST
    
    s = ""
    for item in request.POST:
        s += item + request.POST[item] + " | "    
    
    print "--------------------"
    print request.body
    print request.FILES
    #print repr(request)
    print "--------------------"
    return HttpResponse("Post response complete "+ request.FILES)
    
# 
# def testGet(request):
#     s = ""
#     for item in request.GET:
#         s += item + request.GET[item] + " | "
#         True
#     return HttpResponse(s)


def logChecklist(request):
    print request.FILES
    return HttpResponse()

# Create your views here.
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
        temp['groupId'] = item.group.id
        variables['checklist'].append(temp)
        
    variables['checklistStep']=[]
    s = ChecklistStep.objects.all()
    for item in s:
        temp = {}
        temp['checklistId'] = item.checklist.id
        temp['id'] = item.id
        temp['name'] = item.name
        temp['stepTypeId'] = item.stepType.id
        variables['checklistStep'].append(temp)
        
    variables['stepType']=[]
    st = StepType.objects.all()
    for item in st:
        temp={}
        temp['id']=item.id
        temp['name']=item.name
        variables['stepType'].append(temp)
    
    t = get_template('checklist.html')
    c = Context(variables)
    return HttpResponse(t.render(c))


def checklistSearchByGroup(request, groupId):
    #lookup by groupId
    checklists = Checklist.objects.filter(group=groupId)
    j = {}
    j['groupId'] = groupId
    j['checklist'] = []
    
    for item in checklists:
        temp = {}
        temp['name'] = item.name
        temp['id'] = item.id
        j['checklist'].append(temp)    
    return HttpResponse(json.dumps(j), content_type="application/json")

def checklistSteps(request, checklistId):
    steps = ChecklistStep.objects.filter(checklist = checklistId).order_by('stepNumber')
    j = {}
    j['checklistId'] = checklistId
    j['steps'] = []
    if len(steps) > 0:
        j['checklistName'] = steps[0].checklist.name
    else:
        j['error'] = "No Results"
    for step in steps:
        temp = {}
        temp['name'] = step.name
        temp['id'] = step.id
        temp['stepNumber'] = step.stepNumber
        temp['stepType'] = step.stepType.name
        j['steps'].append(temp)
    return HttpResponse(json.dumps(j), content_type="application/json")
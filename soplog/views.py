import datetime
from decimal import Context
import inspect
from itertools import chain
import json
import os
from xml.dom.minidom import Document

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.files.base import ContentFile, File
from django.http import HttpResponse
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.template.base import Template
from django.template.context import Context
from django.template.loader import get_template, get_template
from django.views.decorators.csrf import csrf_exempt

from soplog.models import *


@csrf_exempt
def testPost(request):    
    if request.FILES.has_key('data'):
        theFile = request.FILES['data'].read()
        a = json.loads(theFile)
        
    return HttpResponse()
        
#     to_return['store_message']= store_message
#     print 'to_return=',to_return
#     to_return['store_message']= store_message
#     serialized = simplejson.dumps(to_return)
    
    
    print "--------------------"
    return HttpResponse("Post exchange complete" + str(request.FILES))
    

def testGet(request):
    s = ""
    for item in request.GET:
        s += item + request.GET[item] + " | "
        True
    return HttpResponse(s)

def latestPost(request):
    f = open( os.getcwd() + "/tempJson", "rb")
    #f = open( "E:\\coding_workspace\\medusa_backend\\tempJson", "rb")
    stringReturn = f.read()
    return HttpResponse(stringReturn)
    

def metaView(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def createList(request):
    return render(request, 'search_form.html')

@csrf_exempt
def upload(request):
    
    dataString = request.FILES.get('data', "empty")
    if dataString == "empty":
        return HttpResponse("Post Data Empty")
    data = json.load(dataString)
    
    
    #FILE WRITER TEMP ############################3333
    f = open("tempJson", "w")
    
    f.write(str(data))
    f.close()
    ################################################3

    userId = data['userId']
    groupId = data['groupId']
    checklistId = data['checklistId']
    steps = data['steps']
    
    newLog = LogChecklist(
                          checklist= Checklist.objects.get(id=checklistId),
                          modifyTime=datetime.datetime.today()
                          )
    newLog.save()
    
    for row in steps:
        
        
        if row['stepType'] == "bool":
            value = False
            if row['value'] == "True":
                value = True
            newBool = LogBool( 
                              checklistLog = LogChecklist.objects.get(id=newLog.id),
                              step = ChecklistStep.objects.get(id=row['stepId']),
                              value = value,
                              modifyTime=datetime.datetime.today()
                              )
            newBool.save()
        elif row['stepType'] == "double":
#             print "-------------"
#             print row
#             print "-------------"
            newDouble = LogDouble(
                                  checklistLog = LogChecklist.objects.get(id=newLog.id),
                                  step = ChecklistStep.objects.get(id=row['stepId']),
                                  value = row['value'],
                                  modifyTime=datetime.datetime.today()
                                  )
            
            newDouble.save()
#             print newDouble.id
        elif row['stepType'] == "text":
            newText = LogText(
                              checklistLog = LogChecklist.objects.get(id=newLog.id),
                              step = ChecklistStep.objects.get(id=row['stepId']),
                              value = row['value'],
                              modifyTime=datetime.datetime.today()
                              )
            newText.save()
        
        
        
    return HttpResponse("List Received")



def showLog(request):
    variables = {}
    variables['checklistLog'] = []
    log = LogChecklist.objects.order_by('modifyTime').reverse()[:10]
    for item in log:
        temp = {}
        temp['id'] = item.id
        temp['checklist'] = item.checklist
        temp['user'] = item.user
        temp['modifyTime'] = item.modifyTime
        variables['checklistLog'].append(temp)
    
    variables['stepLog'] = []
    boolStep = LogBool.objects.order_by('id').reverse()[:50]  
    doubleStep = LogDouble.objects.order_by('id').reverse()[:50]
    textStep = LogText.objects.order_by('id').reverse()[:50]
    
    for item in list(chain(boolStep, doubleStep, textStep)):
        
        temp = {}
        temp['id'] = item.id
        temp['checklistLogId'] = item.checklistLog.id
        temp['stepId'] = item.step
        temp['value'] = item.value
        temp['modifyTime'] = item.modifyTime
        variables['stepLog'].append(temp)
  
    variables['stepLog'] = sorted(variables['stepLog'], key=lambda k: k['checklistLogId'], reverse=True)[:20]
    
    
    t = get_template('showLog.html')
    c = Context(variables)
    return HttpResponse(t.render(c))


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
        temp['order'] = item.order
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
    j['groupId'] = int(groupId)
    j['checklist'] = []
    
    for item in checklists:
        temp = {}
        temp['name'] = item.name
        temp['id'] = item.id
        j['checklist'].append(temp)    
    return HttpResponse(json.dumps(j), content_type="application/json")

def checklistSteps(request, checklistId):
    steps = ChecklistStep.objects.filter(checklist = checklistId).order_by('order')
    j = {}
    j['checklistId'] = int(checklistId)
    j['steps'] = []
    if len(steps) > 0:
        j['checklistName'] = steps[0].checklist.name
    else:
        j['error'] = "No Results"
    for step in steps:
        temp = {}
        temp['name'] = step.name
        temp['id'] = step.id
        temp['order'] = step.order
        temp['type'] = step.stepType.name
        j['steps'].append(temp)
    return HttpResponse(json.dumps(j), content_type="application/json")
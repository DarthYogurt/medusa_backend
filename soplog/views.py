import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import itertools
import json
import os
import smtplib

from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import Context, RequestContext
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

from soplog.models import *


def homepage(request):
    t = get_template('home.html')
    c = Context()
    return HttpResponse(t.render(c))

def checklistSearchByGroupId(request, groupId):
    checklists = List.objects.filter(group=groupId)
    j = {}
    j['groupId'] = int(groupId)
    j['checklist'] = []
    
    if len(checklists) == 0:
        j['error'] = "No Results"
        return HttpResponse(json.dumps(j), content_type="application/json")
    for item in checklists:
        temp = {}
        temp['name'] = item.name
        temp['numOfSteps'] = ListStep.objects.filter(list=List.objects.get(id=item.id)).count()
        temp['id'] = item.id
        
        j['checklist'].append(temp)
    return HttpResponse(json.dumps(j), content_type="application/json")

def checklistSteps(request, checklistId):
    steps = ListStep.objects.filter(list = checklistId).order_by('order')
    j = {}
    j['checklistId'] = int(checklistId)
    j['steps'] = []
    if len(steps) > 0:
        j['checklistName'] = steps[0].list.name
        j['notifyUser'] = steps[0].list.notify.id
    else:
        j['error'] = "No Results"
    
    users = User.objects.all()
    
    j['users'] = []
    
    for user in users:
        temp = {}
        temp['userId'] = user.id
        temp['name'] = user.name
        j['users'].append(temp)
    
    for step in steps:
        temp = {}
        temp['name'] = step.name
        temp['id'] = step.id
        temp['order'] = int(step.order)
        temp['description'] = step.description
        temp['type'] = step.stepType.name
        temp['notifyUserId'] = step.notifyUser.id
       
        temp['requireText'] = step.requireText
        temp['requireImage'] = step.requireImage
                
        if step.ifValueTrue != None:
            temp['ifValueTrue'] = step.ifValueTrue
        
        if step.ifValueFalse != None:
            temp['ifValueFalse'] = step.ifValueFalse
        
        if step.ifGreaterThan != None:
            temp['ifGreaterThan'] = step.ifGreaterThan
        if step.ifLessThan != None:
            temp['ifLessThan'] = step.ifLessThan
        if step.ifEqualTo != None:
            temp['ifEqualTo'] = step.ifEqualTo
        j['steps'].append(temp)
    return HttpResponse(json.dumps(j), content_type="application/json")


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
    
    #print data['timeStarted']
    
    newLog = LogList(
                      list = List.objects.get(id=checklistId),
                      modifyTime=datetime.datetime.today(),
                      startTime= datetime.datetime.strptime(data['timeStarted'], '%m-%d-%y %H:%M:%S' ),
                      endTime = datetime.datetime.strptime(data['timeFinished'], '%m-%d-%y %H:%M:%S')
                      )
    newLog.save()
    for row in steps:
        if row['stepType'] == "bool":
            value = False
            if row['value'] == True:
                value = True
                
            #set extra image
            image = None
            if row.get('extraImage',False):
                newBool = LogBool( 
                                  logList = LogList.objects.get(id=newLog.id),
                                  step = ListStep.objects.get(id=row['stepId']),
                                  value = value,
                                  modifyTime=datetime.datetime.today(),
                                  startTime = datetime.datetime.strptime(row['timeStarted'], '%m-%d-%y %H:%M:%S' ),
                                  endTime = datetime.datetime.strptime(row['timeFinished'], '%m-%d-%y %H:%M:%S' ),
                                  addText = row.get('extraNote',""),
                                  addImage = request.FILES[row.get('extraImage','')]
                                  )
                newBool.save()
            else:  # wasted space. extra else is for addImage if empty clause Fix later
                newBool = LogBool( 
                                  logList = LogList.objects.get(id=newLog.id),
                                  step = ListStep.objects.get(id=row['stepId']),
                                  value = value,
                                  modifyTime=datetime.datetime.today(),
                                  startTime = datetime.datetime.strptime(row['timeStarted'], '%m-%d-%y %H:%M:%S' ),
                                  endTime = datetime.datetime.strptime(row['timeFinished'], '%m-%d-%y %H:%M:%S' ),
                                  addText = row.get('extraNote',"")
                                  )
                newBool.save()                
            
            # Adding to notifyUserId pool
            if row.get('notifyUserId',False):
                newLogBoolNotify = LogBoolNotify(
                                                     logBool = LogBool.objects.get(id=newBool.id),
                                                     user = User.objects.get(id=userId),
                                                     completeBy = datetime.datetime.today(),
                                                     ) 
                newLogBoolNotify.save()
                emailUser(newLogBoolNotify)
                
        elif row['stepType'] == "number":
            newNumber = LogNumber(
                                  logList = LogList.objects.get(id=newLog.id),
                                  step = ListStep.objects.get(id=row['stepId']),
                                  value = row['value'],
                                  modifyTime=datetime.datetime.today(),
                                  startTime = datetime.datetime.strptime(row['timeStarted'], '%m-%d-%y %H:%M:%S' ),
                                  endTime = datetime.datetime.strptime(row['timeFinished'], '%m-%d-%y %H:%M:%S' ),
                                  addText = row.get('extraNote',""),
                                  #addImage = row.get(request.FILES[row['extraImage']],"")
                                  )
            newNumber.save()
        elif row['stepType'] == "text":
            newText = LogText(
                              logList = LogList.objects.get(id=newLog.id),
                              step = ListStep.objects.get(id=row['stepId']),
                              value = row['value'],
                              modifyTime=datetime.datetime.today(),
                              startTime = datetime.datetime.strptime(row['timeStarted'], '%m-%d-%y %H:%M:%S' ),
                              endTime = datetime.datetime.strptime(row['timeFinished'], '%m-%d-%y %H:%M:%S' ),
                              addText = row.get('extraNote',""),
                              )
            newText.save()
        elif row['stepType'] == "image":
            newImage = LogImage(
                                logList = LogList.objects.get(id=newLog.id),
                                step = ListStep.objects.get(id=row['stepId']),
                                file =request.FILES[row['value']],
                                modifyTime = datetime.datetime.today(),
                                startTime = datetime.datetime.strptime(row['timeStarted'], '%m-%d-%y %H:%M:%S' ),
                                endTime = datetime.datetime.strptime(row['timeFinished'], '%m-%d-%y %H:%M:%S' ),
                                addText = row.get('extraNote',""),
                          )
            newImage.save()
            
    return HttpResponse("List Received")

def showLog(request):
    variables = {}
    variables['checklistLog'] = []
    log = LogList.objects.order_by('modifyTime').reverse()[:10]
    for item in log:
        temp = {}
        temp['id'] = item.id
        temp['checklist'] = item.list
        temp['user'] = item.user
        temp['modifyTime'] = item.modifyTime
        variables['checklistLog'].append(temp)
    
    variables['stepLog'] = []
    boolStep = LogBool.objects.order_by('id').reverse()[:50]  
    doubleStep = LogNumber.objects.order_by('id').reverse()[:50]
    textStep = LogText.objects.order_by('id').reverse()[:50]
    
    imageStep = LogImage.objects.order_by("id").reverse()[:50]
    
    variables['imageLog'] = []
    for item in imageStep:
        temp = {}
        temp['id'] = item.id
        temp['checklistLogId'] = item.logList.id
        temp['checklistTemplateName'] = item.logList.list.name
        temp['stepId'] = item.step
        temp['value'] = str(item.file)
        temp['modifyTime'] = item.modifyTime
        variables['imageLog'].append(temp)
        
    for item in list(itertools.chain(boolStep, doubleStep, textStep)):
        temp = {}
        temp['id'] = item.id
        temp['checklistLogId'] = item.logList.id
        temp['checklistTemplateName'] = item.logList.list.name
        temp['stepId'] = item.step
        temp['value'] = item.value
        temp['modifyTime'] = item.modifyTime
        variables['stepLog'].append(temp)
  
    variables['stepLog'] = sorted(variables['stepLog'], key=lambda k: k['checklistLogId'], reverse=True)[:20]   
    t = get_template('showLog.html')
    c = Context(variables)
    return HttpResponse(t.render(c))

def analytics(request):
    groupId = 1
    var = {}
    #var['checklists'] = Checklist.objects.get(group=Group.objects.get(id=groupId)) #Uncomment after getting group to work 
    var['checklist'] = List.objects.all()  #Testing only
    #var['steps'] = ChecklistStep.objects.all()
    #var['stepLog'] = LogChecklist.objects.all()
    #var['logBool'] = LogBool.objects.all()
    
    t = get_template('analytics.html')
    c = Context(var)
    return HttpResponse(t.render(c))

def getLogData(request, checklistId):
    j={}
    j['checklistId'] = checklistId
    j['periodStart'] = ""
    j['periodEnd'] = ""
    j['stepLog'] = []
    
    for step in ListStep.objects.order_by('order').filter(list=List.objects.get(id=checklistId)):
        temp={}
        temp['stepId'] = step.id
        temp['stepName'] = step.name
        temp['order'] = step.order
        temp['stepType'] = step.stepType.name
        
        if step.stepType.name == "bool":
            temp['yes'] = LogBool.objects.filter(step=step.id, value=True).count()
            temp['no'] = LogBool.objects.filter(step=step.id, value=False).count()
        elif step.stepType.name == "number":
            True
            # DO SOMETHING TO NUMBER AND LOG MEDIAN 
        
        j['stepLog'].append(temp)
    return HttpResponse(json.dumps(j), content_type="application/json")


def slate(request):
    var = {}
    var['slate'] = LogBoolNotify.objects.all().order_by('complete','-completedTime')

    t = get_template('slate.html')
    c = Context(var)
    return HttpResponse(t.render(c))


def getSlate(request):
    j = {}
    j['slate'] = []
    
    for slate in LogBoolNotify.objects.order_by('complete', '-completedTime'):
        t = {}
        t['slateId'] = slate.id
        t['checklist'] = slate.logBool.step.list.name
        t['logBoolId'] =slate.logBool.id
        #t['userId'] = slate.user.id
        t['userName'] = slate.user.name
        #t['notifyId'] = slate.logBool.step.notifyUser.id
        t['notifyName'] = slate.logBool.step.notifyUser.name
        t['stepName'] = slate.logBool.step.name
        t['complete'] = slate.complete
        t['addNote'] = slate.logBool.addText
        t['addImage'] = request.get_host()+str(slate.logBool.addImage)
         
        j['slate'].append(t)
        #print slate
        
    return HttpResponse(json.dumps(j), content_type="application/json")

def emailUser(logBoolNotify):
    to = logBoolNotify.user.email
    gmail_user = 'soplogmedusa@gmail.com'
    gmail_pwd = 'supermanfly821'
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: ' + logBoolNotify.logBool.step.name +" id:"+ str(logBoolNotify.id) +'\n'
    header = header.encode("ascii", 'ignore')
    msg = header + "\n\n" + logBoolNotify.logBool.step.name + " on: " + str(logBoolNotify.completeBy) + " : regarding - " +logBoolNotify.logBool.addText
    msg = msg.encode("ascii", "ignore")
    smtpserver.sendmail(gmail_user, to, msg)

    smtpserver.close()
    

@csrf_exempt
def createChecklist(request):
    var = {}
    var['stepType'] = StepType.objects.all()
    var['users'] = User.objects.all()
    var['existingChecklists'] = List.objects.all()
    
    t = get_template('createChecklist.html')
    c = Context(var)
    return HttpResponse(t.render(c))

@csrf_exempt
def listConfirm(request):
    post = request.POST
    #for item in post:
    #    print item, post[item]

    
    checklistName = request.POST.get('checklistName',"")
    groupId = request.POST.get('groupId',1)
    userIdToNotify = request.POST.get('userIdToNotify')
    totalSteps = int(request.POST['totalSteps'])
    
    newChecklist = List(
                             name = checklistName,
                             group = Group.objects.get(id = groupId),
                             notify = User.objects.get(id = userIdToNotify)
                             )
    newChecklist.save()
    
    #print "HERE", type(Checklist.objects.get(id = newChecklist.id))
    for i in range(totalSteps):
        newStep = ListStep(
                                name = request.POST['stepName'+str(i)],
                                order = i+1,
                                description = request.POST['desc'+str(i)],
                                list = List.objects.get(id=newChecklist.id),
                            
                                stepType = StepType.objects.get(name=request.POST['stepType'+str(i)]),
                                notifyUser = User.objects.get(id=request.POST['stepUser'+str(i)]),
                                requireText = request.POST.get('reqText'+str(i), False), #request.POST.get('reqText', False),
                                requireImage = request.POST.get('reqImage'+str(i), False),
                                ifValueTrue = request.POST.get('reqifTrue'+str(i), False),
                                ifValueFalse = request.POST.get('reqifFalse'+str(i), False),                       
                                )
        newStep.save()
        
    return HttpResponse("complete")

@csrf_exempt
def checkOffSlate(request, logBoolNotifyId): #, completedTime):
    logBoolNotify = LogBoolNotify.objects.get(id=logBoolNotifyId)
    if logBoolNotify.complete == True:
        logBoolNotify.complete = False
    elif logBoolNotify.complete == False:
        logBoolNotify.complete = True
        logBoolNotify.completedTime = datetime.datetime.today()
        #datetime.datetime.strptime(completedTime, '%m-%d-%y %H:%M:%S')
    logBoolNotify.save()
    
    #print logBoolNotify.strftime("%Y-%M-%D %H:%M")
    return HttpResponse(logBoolNotify.completedTime)


@csrf_exempt
def showPost(request):
    var =  request.POST
    
    t = get_template('showPost.html')
    c = Context(var)
    return HttpResponse(t.render(c))



def latestPost(request):
    f = open( os.getcwd() + "/tempJson", "rb")
    #f = open( "E:\\coding_workspace\\medusa_backend\\tempJson", "rb")
    stringReturn = f.read()
    return HttpResponse(stringReturn)

@csrf_exempt
def uploadError(request):
    f = open("error.html", "w")
    f.write(request.FILES['error'].read())
    f.close()
    return HttpResponse("")


def latestError(request):
    f = open( os.getcwd() + "/error.html", "rb")
    #f = open( "E:\\coding_workspace\\medusa_backend\\tempJson", "rb")
    stringReturn = f.read()
    return HttpResponse(stringReturn)

# @csrf_exempt
# def testFile(request):
#     print "In Test File"
#     # Handle file upload
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         print
#         print form
#         print request.FILES
#         if form.is_valid():
#             newdoc = LogImage(file = request.FILES['image'])
#             newdoc.save()
#             
#             print newdoc
#             return HttpResponse("None")
#     else:
#         form = ImageForm()
#     # Load documents for the list page
#     documents = LogImage.objects.all()
# 
#     # Render list page with the documents and the form
#     return HttpResponse(documents)



    

def temp(request):
    a = LogBoolNotify.objects.get(id=32)
    emailUser(a)
#     t = get_template('temp.html')
#     c = Context()
    return HttpResponse()
    
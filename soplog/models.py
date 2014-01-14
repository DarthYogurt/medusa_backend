from django.db import models


class User(models.Model):
    ''' currently not connected to Group 
    '''
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name + "-"+ str(self.id)
    
# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name

class Checklist(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    group = models.ForeignKey('Group')
    notify = models.ForeignKey('User')
#     categoryId = models.ForeignKey('Category')
    
    def __unicode__(self):
        return str(self.id) + "-" + self.name + " - " + str(self.group)
    
class ChecklistStep(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField()
    description = models.TextField()
    checklist = models.ForeignKey('Checklist')
    stepType = models.ForeignKey('StepType')
    
    def __unicode__(self):
        return str(self.order) + " " + self.name+"-id:"+str(self.id)
    
class StepType(models.Model):
    name = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.name
 
class LogChecklist(models.Model):
    checklist = models.ForeignKey('Checklist')   # The referencing Checklist
    user = models.ForeignKey('User', null=True)
    startTime = models.DateTimeField(null=True)
    modifyTime = models.DateTimeField()
    endtime = models.DateTimeField(null=True)
     
    def __unicode__(self):
        return str(self.checklist.name) +" - "+ str(self.id) + "-"+ str(self.modifyTime)
 
class LogBool(models.Model):
    checklistLog = models.ForeignKey('LogChecklist')
    step = models.ForeignKey('ChecklistStep')
    value = models.BooleanField()
    modifyTime = models.DateTimeField(null=True)
    
    def __unicode__(self):
        return str(self.checklistLog.checklist.name) + "-" + str(self.step.name) + "-" + str(self.modifyTime)
     
class LogDouble(models.Model):    #Not really double, Django doesn't have double values
    checklistLog = models.ForeignKey('LogChecklist')
    step = models.ForeignKey('ChecklistStep')
    value = models.FloatField()
    modifyTime = models.DateTimeField(null=True)
     
class LogText(models.Model):
    checklistLog = models.ForeignKey('LogChecklist')
    step = models.ForeignKey('ChecklistStep')
    value = models.TextField()
    modifyTime = models.DateTimeField(null=True)
 
class LogFile(models.Model):
    checklistLog = models.ForeignKey('LogChecklist')
    step = models.ForeignKey('ChecklistStep')
    #value = models.CharField(max_length=40)
    modifyTime = models.DateTimeField(null=True)
     
# class LogAudio(models.Model):
#     checklistLog = models.ForeignKey('LogChecklist')
#     value = models.CharField(max_length=40)
#     modifyTime = models.DateTimeField()
#      
# class LogVideo(models.Model):
#     checklistLog = models.ForeignKey('LogChecklist')
#     value = models.CharField(max_length=40)
#     modifyTime = models.DateTimeField()
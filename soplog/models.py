from django.db import models


class User(models.Model):
    ''' currently not connected to Group 
    '''
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name
    
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
#     categoryId = models.ForeignKey('Category')
    
    def __unicode__(self):
        return self.name + " - " + str(self.group)
    
class ChecklistStep(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField()
    description = models.TextField()
    checklist = models.ForeignKey('Checklist')
    stepType = models.ForeignKey('StepType')
    
    def __unicode__(self):
        return str(self.stepNumber) + " " + self.name
    
class StepType(models.Model):
    name = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.name
 
class LogChecklist(models.Model):
    checklist = models.ForeignKey('Checklist')   # The referencing Checklist
    user = models.ForeignKey('User')
    startTime = models.DateTimeField()
    modifyTime = models.DateTimeField()
    endtime = models.DateTimeField()
     
    def __unicode__(self):
        return self.checklist.name
 
class LogBool(models.Model):
    checklistLog = models.ForeignKey('LogChecklist')
    value = models.BooleanField()
    modifyTime = models.DateTimeField()
     
class LogDouble(models.Model):    #Not really double, Django doesn't have double values
    checklistLog = models.ForeignKey('LogChecklist')
    value = models.FloatField()
    modifyTime = models.DateTimeField()
     
class LogText(models.Model):
    checklistLog = models.ForeignKey('LogChecklist')
    value = models.TextField()
    modifyTime = models.DateTimeField()
 
class LogImage(models.Model):
    checklistLog = models.ForeignKey('LogChecklist')
    value = models.CharField(max_length=40)
    modifyTime = models.DateTimeField()
     
class LogAudio(models.Model):
    checklistLog = models.ForeignKey('LogChecklist')
    value = models.CharField(max_length=40)
    modifyTime = models.DateTimeField()
     
class LogVideo(models.Model):
    checklistLog = models.ForeignKey('LogChecklist')
    value = models.CharField(max_length=40)
    modifyTime = models.DateTimeField()
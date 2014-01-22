from django.db import models


class User(models.Model):
    ''' currently not connected to Group 
    '''
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name + "-"+ str(self.id)
    
# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name

#Tempalte Checklist
class List(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    group = models.ForeignKey('Group',blank=True, null=True)
    
    def __unicode__(self):
        return str(self.id) + self.name

class ListNotify(models.Model):
    list = models.ForeignKey('List')
    user = models.ForeignKey('User')
#     categoryId = models.ForeignKey('Category')
    
    #def __unicode__(self):
    #    return str(self.id) + "-" + self.name + " - " + str(self.group)

class ListStep(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField()
    description = models.TextField(blank=True)
    list = models.ForeignKey('List')
    stepType = models.ForeignKey('StepType')
    notifyUser = models.ForeignKey("User")
    requireText = models.BooleanField(blank=True)
    requireImage = models.BooleanField(blank=True)
    ifValueTrue = models.BooleanField(blank=True)
    ifValueFalse = models.BooleanField(blank=True)
    ifGreaterThan = models.FloatField(blank=True)
    ifLessThan = models.FloatField(blank=True)
    ifEqualTo = models.FloatField(blank=True)
    

    def __unicode__(self):
        return str(self.order) + " " + self.name+"-id:"+str(self.id)

'''
class ListStepNotify(models.Model):
    listStep = models.ForeignKey("ListStep")
    user = models.ForeignKey("User",blank=True)
    ifValueTrue = models.BooleanField(blank=True)
    ifValueFalse = models.BooleanField(blank=True)
    ifGreaterThan = models.FloatField(blank=True)
    ifLessThan = models.FloatField(blank=True)
    ifEqualTo = models.FloatField(blank=True)
'''
    
class StepType(models.Model):
    name = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.name
    

    
'''
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
'''   
# class LogAudio(models.Model):
#     checklistLog = models.ForeignKey('LogChecklist')
#     value = models.CharField(max_length=40)
#     modifyTime = models.DateTimeField()
#      
# class LogVideo(models.Model):
#     checklistLog = models.ForeignKey('LogChecklist')
#     value = models.CharField(max_length=40)
#     modifyTime = models.DateTimeField()
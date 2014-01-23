from django.db import models
from django.forms.models import ModelForm


# Create your models here.
class User(models.Model):
    ''' currently not connected to Group 
    '''
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name + "-"+ str(self.id)
    
class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    group = models.ForeignKey('Group',blank=True, null=True)
    
    def __unicode__(self):
        return str(self.id) + self.name

class ListNotify(models.Model):
    list = models.ForeignKey('List')
    user = models.ForeignKey('User')
    
    def __unicode__(self):
        return str(str(self.id) + " - "+ self.list.name + "-" + self.user.name )
    
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
    ifGreaterThan = models.FloatField(blank=True, null=True)
    ifLessThan = models.FloatField(blank=True, null=True)
    ifEqualTo = models.FloatField(blank=True, null=True)
    def __unicode__(self):
        return str(self.order) + " " + self.name+"-id:"+str(self.id)
    
class StepType(models.Model):
    name = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.name
    
class LogList(models.Model):
    list = models.ForeignKey('List')   # The referencing Checklist
    user = models.ForeignKey('User', null=True)
    startTime = models.DateTimeField(null=True)
    modifyTime = models.DateTimeField(null=True)
    endtime = models.DateTimeField(null=True)
     
    def __unicode__(self):
        return str(self.checklist.name) +" - "+ str(self.id) + "-"+ str(self.modifyTime)
 
class LogBool(models.Model):
    logList = models.ForeignKey('LogList')
    step = models.ForeignKey('ListStep')
    value = models.BooleanField()
    modifyTime = models.DateTimeField(null=True)
    
    def __unicode__(self):
        return str(self.checklistLog.checklist.name) + "-" + str(self.step.name) + "-" + str(self.modifyTime)
     
class LogNumber(models.Model):    #Not really double, Django doesn't have double values
    logList = models.ForeignKey('LogList')
    step = models.ForeignKey('ListStep')
    value = models.FloatField()
    modifyTime = models.DateTimeField(null=True)
     
class LogText(models.Model):
    logList = models.ForeignKey('LogList')
    step = models.ForeignKey('ListStep')
    value = models.TextField()
    modifyTime = models.DateTimeField(null=True)
 
# class LogFile(models.Model):
#     logList = models.ForeignKey('LogList')
#     step = models.ForeignKey('ListStep')
#     file = models.FileField(upload_to='../media/%Y/%m/%d')
#     modifyTime = models.DateTimeField(null=True)
#      

# class TestFile(models.Model):
#     image = models.FileField()
#     
# class FileForm(ModelForm):
#     class Meta:
#         model = TestFile
#         fields = ['image']
    
    
    
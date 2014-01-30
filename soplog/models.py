import os

from django import forms
from django.db import models
from django.forms.models import ModelForm


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
        return str(self.id) + "-" + self.name

class List(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    group = models.ForeignKey('Group',blank=True, null=True)
    
    def __unicode__(self):
        return str(self.id) + "-" + self.name

class ListNotify(models.Model):
    list = models.ForeignKey('List')
    user = models.ForeignKey('User')
    
    def __unicode__(self):
        return str(str(self.id) + " - "+ self.list.name + "-" + self.user.name )
    
class ListStep(models.Model):
    name = models.CharField(max_length=255)
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
        return str(self.list.id) + " " + self.name+"-id:"+str(self.id)
    
class StepType(models.Model):
    name = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.name
    
class LogList(models.Model):
    list = models.ForeignKey('List')   # The referencing Checklist
    user = models.ForeignKey('User', null=True)
    startTime = models.DateTimeField(null=True)
    modifyTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)
     
    def __unicode__(self):
        return str(self.list.name) +" - "+ str(self.id) 
 
class LogBool(models.Model):
    logList = models.ForeignKey('LogList')
    step = models.ForeignKey('ListStep')
    value = models.BooleanField()
    startTime = models.DateTimeField(null=True)
    modifyTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)
    
#     def __unicode__(self):
#         return str(self.logList.list.name) + "-" + str(self.step) 
     
class LogNumber(models.Model):    #Not really double, Django doesn't have double values
    logList = models.ForeignKey('LogList')
    step = models.ForeignKey('ListStep')
    value = models.FloatField()
    startTime = models.DateTimeField(null=True)
    modifyTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)
    
#     def __unicode__(self):
#         return str(self.logList.list.name) + "-" + str(self.step) 
     
class LogText(models.Model):
    logList = models.ForeignKey('LogList')
    step = models.ForeignKey('ListStep')
    value = models.TextField()
    startTime = models.DateTimeField(null=True)
    modifyTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)
    
#     def __unicode__(self):
#         return str(self.logList.list.name) + "-" + str(self.step) 

class LogImage(models.Model):
    logList = models.ForeignKey('LogList')
    step = models.ForeignKey("ListStep")
    file = models.FileField(upload_to="/media/%Y/%m/%d")
    startTime = models.DateTimeField(null=True)
    modifyTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)
    
#     def __unicode__(self):
#         return str(self.step) +"-"+ str(file)
# class ImageForm(forms.Form):
#     file = forms.FileField(
#         label='Select a file',
#         help_text='max. 42 megabytes'
#     )
#     return os.path.join('images', str(instance.id), filename)
# def get_image_path(instance, filename):

#      
#         return self.id
#     def __unicode__(self):
#     image = models.ImageField(upload_to="/media/", blank=True, null=True)
# class LogImage(models.Model):
    
 
# class LogFile(models.Model):
#     logList = models.ForeignKey('LogList')
#     step = models.ForeignKey('ListStep')
#     file = models.FileField(upload_to='../media/%Y/%m/%d')
#     modifyTime = models.DateTimeField(null=True)
#      

# class TestFile(models.Model):
#     file = models.FileField(upload_to='../media/%Y/%m/%d')
#      
# class TestFileForm(ModelForm):
#     class Meta:
#         model = TestFile
#         fields = ['file']
    
# class TestFile(models.Model):
#     image = models.FileField(upload_to='../media/%Y/%m/%d')
#     
# class TestFileForm(forms.Form):
#     docfile = forms.FileField(
#         label='Select a file',
#         help_text='max. 42 megabytes'
#     )
#     
#     
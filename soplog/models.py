from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name

class Checklist(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    groupId = models.ForeignKey('Group')
#     categoryId = models.ForeignKey('Category')
    
    def __unicode__(self):
        return self.name + " - " + str(self.groupId)
    
class ChecklistStep(models.Model):
    name = models.CharField(max_length=50)
    stepNumber = models.IntegerField()
    description = models.TextField()
    checklistId = models.ForeignKey('Checklist')
    stepTypeId = models.ForeignKey('StepType')
    
    def __unicode__(self):
        return str(self.stepNumber) + " " + self.name
    
class StepType(models.Model):
    name = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.name

    

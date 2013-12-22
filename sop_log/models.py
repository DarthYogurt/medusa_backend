from django.db import models

''' Models for the Checklists '''

class Checklist(models.Model):
    name = models.CharField(max_length=30)
    group_id = models.ForeignKey('Group')
    #category_id = models.ForeignKey('Category')
    #template_id = models.ForeignKey('Template')
    

class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    
  

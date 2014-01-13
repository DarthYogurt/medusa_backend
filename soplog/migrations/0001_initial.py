# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=30),), ('phone', models.IntegerField(),), ('email', models.CharField(max_length=30),)],
            bases = (models.Model,),
            options = {},
            name = 'User',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=10),)],
            bases = (models.Model,),
            options = {},
            name = 'StepType',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=30),), ('description', models.TextField(),)],
            bases = (models.Model,),
            options = {},
            name = 'Group',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=50),), ('description', models.TextField(),), ('group', models.ForeignKey(to=u'soplog.Group', to_field=u'id'),)],
            bases = (models.Model,),
            options = {},
            name = 'Checklist',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=50),), ('stepNumber', models.IntegerField(),), ('description', models.TextField(),), ('checklist', models.ForeignKey(to=u'soplog.Checklist', to_field=u'id'),), ('stepType', models.ForeignKey(to=u'soplog.StepType', to_field=u'id'),)],
            bases = (models.Model,),
            options = {},
            name = 'ChecklistStep',
        ),
    ]

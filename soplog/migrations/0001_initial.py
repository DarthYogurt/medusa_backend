# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=30),), ('phone', models.CharField(max_length=15),), ('email', models.CharField(max_length=30),)],
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
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=30),), ('description', models.TextField(blank=True),)],
            bases = (models.Model,),
            options = {},
            name = 'Group',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=50),), ('description', models.TextField(blank=True),), ('group', models.ForeignKey(to_field=u'id', blank=True, to=u'soplog.Group', null=True),)],
            bases = (models.Model,),
            options = {},
            name = 'List',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('list', models.ForeignKey(to=u'soplog.List', to_field=u'id'),), ('user', models.ForeignKey(to=u'soplog.User', to_field=u'id'),)],
            bases = (models.Model,),
            options = {},
            name = 'ListNotify',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=50),), ('order', models.IntegerField(),), ('description', models.TextField(blank=True),), ('list', models.ForeignKey(to=u'soplog.List', to_field=u'id'),), ('stepType', models.ForeignKey(to=u'soplog.StepType', to_field=u'id'),), ('notifyUser', models.ForeignKey(to=u'soplog.User', to_field=u'id'),), ('requireText', models.BooleanField(),), ('requireImage', models.BooleanField(),), ('ifValueTrue', models.BooleanField(),), ('ifValueFalse', models.BooleanField(),), ('ifGreaterThan', models.FloatField(null=True, blank=True),), ('ifLessThan', models.FloatField(null=True, blank=True),), ('ifEqualTo', models.FloatField(null=True, blank=True),)],
            bases = (models.Model,),
            options = {},
            name = 'ListStep',
        ),
    ]

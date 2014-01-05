# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0004_logbool')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('checklistLog', models.ForeignKey(to=u'soplog.LogChecklist', to_field=u'id'),), ('value', models.CharField(max_length=40),), ('modifyTime', models.DateTimeField(),)],
            bases = (models.Model,),
            options = {},
            name = 'LogAudio',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('checklistLog', models.ForeignKey(to=u'soplog.LogChecklist', to_field=u'id'),), ('value', models.FloatField(),), ('modifyTime', models.DateTimeField(),)],
            bases = (models.Model,),
            options = {},
            name = 'LogDouble',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('checklistLog', models.ForeignKey(to=u'soplog.LogChecklist', to_field=u'id'),), ('value', models.CharField(max_length=40),), ('modifyTime', models.DateTimeField(),)],
            bases = (models.Model,),
            options = {},
            name = 'LogImage',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('checklistLog', models.ForeignKey(to=u'soplog.LogChecklist', to_field=u'id'),), ('value', models.TextField(),), ('modifyTime', models.DateTimeField(),)],
            bases = (models.Model,),
            options = {},
            name = 'LogText',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('checklistLog', models.ForeignKey(to=u'soplog.LogChecklist', to_field=u'id'),), ('value', models.CharField(max_length=40),), ('modifyTime', models.DateTimeField(),)],
            bases = (models.Model,),
            options = {},
            name = 'LogVideo',
        ),
    ]

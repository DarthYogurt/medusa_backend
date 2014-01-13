# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0009_auto_20140106_1737')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('checklistLog', models.ForeignKey(to=u'soplog.LogChecklist', to_field=u'id'),), ('value', models.CharField(max_length=40),), ('modifyTime', models.DateTimeField(),)],
            bases = (models.Model,),
            options = {},
            name = 'LogAudio',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('checklistLog', models.ForeignKey(to=u'soplog.LogChecklist', to_field=u'id'),), ('value', models.CharField(max_length=40),), ('modifyTime', models.DateTimeField(),)],
            bases = (models.Model,),
            options = {},
            name = 'LogImage',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('checklistLog', models.ForeignKey(to=u'soplog.LogChecklist', to_field=u'id'),), ('value', models.CharField(max_length=40),), ('modifyTime', models.DateTimeField(),)],
            bases = (models.Model,),
            options = {},
            name = 'LogVideo',
        ),
        migrations.DeleteModel(
            'LogFile',
        ),
        migrations.RenameField(
            new_name = 'order',
            model_name = 'checkliststep',
            old_name = 'stepNumber',
        ),
        migrations.AlterField(
            field = models.DateTimeField(),
            name = 'modifyTime',
            model_name = 'logchecklist',
        ),
        migrations.AlterField(
            field = models.DateTimeField(),
            name = 'modifyTime',
            model_name = 'logbool',
        ),
        migrations.AlterField(
            field = models.DateTimeField(),
            name = 'modifyTime',
            model_name = 'logtext',
        ),
        migrations.AlterField(
            field = models.DateTimeField(),
            name = 'modifyTime',
            model_name = 'logdouble',
        ),
    ]

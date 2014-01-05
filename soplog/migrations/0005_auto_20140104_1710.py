# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0004_checkliststep_stepnumber')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=30),), ('phone', models.IntegerField(),), ('email', models.CharField(max_length=30),)],
            bases = (models.Model,),
            options = {},
            name = 'User',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('checklistId', models.ForeignKey(to=u'soplog.Checklist', to_field=u'id'),), ('userId', models.ForeignKey(to=u'soplog.User', to_field=u'id'),), ('startTime', models.DateTimeField(),), ('modifyTime', models.DateTimeField(),), ('endtime', models.DateTimeField(),)],
            bases = (models.Model,),
            options = {},
            name = 'ChecklistLog',
        ),
        migrations.AlterField(
            field = models.CharField(max_length=50),
            name = 'name',
            model_name = 'checklist',
        ),
        migrations.AlterField(
            field = models.CharField(max_length=50),
            name = 'name',
            model_name = 'checkliststep',
        ),
    ]

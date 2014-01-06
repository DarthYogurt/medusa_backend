# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0006_auto_20140105_2038')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('checklistLog', models.ForeignKey(to=u'soplog.LogChecklist', to_field=u'id'),), ('value', models.FileField(upload_to=''),), ('modifyTime', models.DateTimeField(auto_now_add=True),)],
            bases = (models.Model,),
            options = {},
            name = 'LogFile',
        ),
        migrations.DeleteModel(
            'LogImage',
        ),
        migrations.DeleteModel(
            'LogVideo',
        ),
        migrations.DeleteModel(
            'LogAudio',
        ),
    ]

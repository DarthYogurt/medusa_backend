# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0005_logaudio_logdouble_logimage_logtext_logvideo')]

    operations = [
        migrations.AlterField(
            field = models.DateTimeField(auto_now_add=True),
            name = 'modifyTime',
            model_name = 'logimage',
        ),
        migrations.AlterField(
            field = models.FileField(upload_to=''),
            name = 'value',
            model_name = 'logimage',
        ),
        migrations.AlterField(
            field = models.DateTimeField(auto_now_add=True),
            name = 'modifyTime',
            model_name = 'logchecklist',
        ),
        migrations.AlterField(
            field = models.DateTimeField(auto_now_add=True),
            name = 'modifyTime',
            model_name = 'logbool',
        ),
        migrations.AlterField(
            field = models.DateTimeField(auto_now_add=True),
            name = 'modifyTime',
            model_name = 'logtext',
        ),
        migrations.AlterField(
            field = models.DateTimeField(auto_now_add=True),
            name = 'modifyTime',
            model_name = 'logvideo',
        ),
        migrations.AlterField(
            field = models.DateTimeField(auto_now_add=True),
            name = 'modifyTime',
            model_name = 'logdouble',
        ),
        migrations.AlterField(
            field = models.DateTimeField(auto_now_add=True),
            name = 'modifyTime',
            model_name = 'logaudio',
        ),
    ]

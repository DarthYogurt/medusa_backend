# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0010_auto_20140130_1202')]

    operations = [
        migrations.AddField(
            field = models.TextField(null=True, blank=True),
            name = 'addText',
            model_name = 'lognumber',
        ),
        migrations.AddField(
            field = models.TextField(null=True, blank=True),
            name = 'addText',
            model_name = 'logimage',
        ),
        migrations.AddField(
            field = models.TextField(null=True, blank=True),
            name = 'addText',
            model_name = 'logtext',
        ),
        migrations.AddField(
            field = models.FileField(null=True, upload_to='/media/%Y/%m/%d'),
            name = 'addImage',
            model_name = 'logtext',
        ),
        migrations.AddField(
            field = models.FileField(null=True, upload_to='/media/%Y/%m/%d'),
            name = 'addImage',
            model_name = 'logimage',
        ),
        migrations.AddField(
            field = models.FileField(null=True, upload_to='/media/%Y/%m/%d'),
            name = 'addImage',
            model_name = 'lognumber',
        ),
    ]

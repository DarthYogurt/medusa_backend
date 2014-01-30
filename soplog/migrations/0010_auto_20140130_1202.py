# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0009_auto_20140129_1642')]

    operations = [
        migrations.AddField(
            field = models.FileField(null=True, upload_to='/media/%Y/%m/%d'),
            name = 'addImage',
            model_name = 'logbool',
        ),
        migrations.AddField(
            field = models.TextField(null=True, blank=True),
            name = 'addText',
            model_name = 'logbool',
        ),
    ]

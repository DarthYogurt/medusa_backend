# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0008_auto_20140129_1455')]

    operations = [
        migrations.AddField(
            field = models.DateTimeField(null=True),
            name = 'endTime',
            model_name = 'logtext',
        ),
        migrations.AddField(
            field = models.DateTimeField(null=True),
            name = 'endTime',
            model_name = 'logbool',
        ),
        migrations.AddField(
            field = models.DateTimeField(null=True),
            name = 'startTime',
            model_name = 'lognumber',
        ),
        migrations.AddField(
            field = models.DateTimeField(null=True),
            name = 'startTime',
            model_name = 'logimage',
        ),
        migrations.RenameField(
            new_name = 'endTime',
            model_name = 'loglist',
            old_name = 'endtime',
        ),
        migrations.AddField(
            field = models.DateTimeField(null=True),
            name = 'endTime',
            model_name = 'lognumber',
        ),
        migrations.AddField(
            field = models.DateTimeField(null=True),
            name = 'endTime',
            model_name = 'logimage',
        ),
        migrations.AddField(
            field = models.DateTimeField(null=True),
            name = 'startTime',
            model_name = 'logtext',
        ),
        migrations.AddField(
            field = models.DateTimeField(null=True),
            name = 'startTime',
            model_name = 'logbool',
        ),
    ]

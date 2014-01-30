# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0011_auto_20140130_1203')]

    operations = [
        migrations.AlterField(
            field = models.FileField(null=True, upload_to='/media/%Y/%m/%d', blank=True),
            name = 'addImage',
            model_name = 'lognumber',
        ),
        migrations.AlterField(
            field = models.FileField(null=True, upload_to='/media/%Y/%m/%d', blank=True),
            name = 'addImage',
            model_name = 'logtext',
        ),
        migrations.AlterField(
            field = models.FileField(null=True, upload_to='/media/%Y/%m/%d', blank=True),
            name = 'addImage',
            model_name = 'logimage',
        ),
        migrations.AlterField(
            field = models.FileField(null=True, upload_to='/media/%Y/%m/%d', blank=True),
            name = 'addImage',
            model_name = 'logbool',
        ),
    ]

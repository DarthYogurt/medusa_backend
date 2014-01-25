# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0005_auto_20140123_2030')]

    operations = [
        migrations.AlterField(
            field = models.FileField(upload_to='/media/%Y/%m/%d'),
            name = 'file',
            model_name = 'logimage',
        ),
    ]

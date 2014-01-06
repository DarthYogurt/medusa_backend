# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0007_auto_20140105_2042')]

    operations = [
        migrations.RemoveField(
            name = 'value',
            model_name = 'logfile',
        ),
    ]

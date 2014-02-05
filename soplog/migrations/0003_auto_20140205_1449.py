# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0002_auto_20140205_1102')]

    operations = [
        migrations.AlterField(
            field = models.BooleanField(default=False),
            name = 'value',
            model_name = 'logbool',
        ),
    ]

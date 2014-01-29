# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0006_auto_20140124_1350')]

    operations = [
        migrations.AlterField(
            field = models.CharField(max_length=255),
            name = 'name',
            model_name = 'list',
        ),
    ]

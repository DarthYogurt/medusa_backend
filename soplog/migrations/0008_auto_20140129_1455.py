# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0007_auto_20140128_1653')]

    operations = [
        migrations.AlterField(
            field = models.CharField(max_length=255),
            name = 'name',
            model_name = 'liststep',
        ),
    ]

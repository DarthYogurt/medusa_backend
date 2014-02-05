# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0001_initial')]

    operations = [
        migrations.AlterField(
            field = models.NullBooleanField(),
            name = 'ifValueFalse',
            model_name = 'liststep',
        ),
        migrations.AlterField(
            field = models.NullBooleanField(),
            name = 'requireImage',
            model_name = 'liststep',
        ),
        migrations.AlterField(
            field = models.NullBooleanField(),
            name = 'requireText',
            model_name = 'liststep',
        ),
        migrations.AlterField(
            field = models.NullBooleanField(),
            name = 'ifValueTrue',
            model_name = 'liststep',
        ),
    ]

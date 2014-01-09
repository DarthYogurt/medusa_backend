# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0016_auto_20140108_1637')]

    operations = [
        migrations.AlterField(
            field = models.DateTimeField(),
            name = 'modifyTime',
            model_name = 'logchecklist',
        ),
    ]

# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0015_auto_20140108_1636')]

    operations = [
        migrations.AlterField(
            field = models.DateTimeField(auto_now_add=True, null=True),
            name = 'modifyTime',
            model_name = 'logchecklist',
        ),
    ]

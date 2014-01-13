# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0014_auto_20140108_1626')]

    operations = [
        migrations.AlterField(
            field = models.DateTimeField(auto_now_add=True),
            name = 'modifyTime',
            model_name = 'logchecklist',
        ),
    ]

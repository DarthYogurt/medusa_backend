# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0003_auto_20131222_1624')]

    operations = [
        migrations.AddField(
            field = models.IntegerField(default=1),
            preserve_default = False,
            name = 'stepNumber',
            model_name = 'checkliststep',
        ),
    ]

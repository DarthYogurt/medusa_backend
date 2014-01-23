# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0006_logfile')]

    operations = [
        migrations.RenameField(
            new_name = 'ifValueTrue',
            model_name = 'liststep',
            old_name = 'requireOnBooleanValue',
        ),
        migrations.AddField(
            field = models.BooleanField(default=True),
            preserve_default = False,
            name = 'ifValueFalse',
            model_name = 'liststep',
        ),
    ]

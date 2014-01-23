# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0003_auto_20140122_0321')]

    operations = [
        migrations.DeleteModel(
            'TestImage',
        ),
        migrations.RenameField(
            new_name = 'requireOnBooleanValue',
            model_name = 'liststep',
            old_name = 'ifValueTrue',
        ),
        migrations.RemoveField(
            name = 'ifValueFalse',
            model_name = 'liststep',
        ),
    ]

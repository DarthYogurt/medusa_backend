# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0001_initial')]

    operations = [
        migrations.RenameField(
            new_name = 'image',
            model_name = 'testfile',
            old_name = 'docfile',
        ),
    ]

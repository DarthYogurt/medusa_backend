# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0002_testimage')]

    operations = [
        migrations.RenameField(
            new_name = 'image',
            model_name = 'testimage',
            old_name = 'name',
        ),
    ]

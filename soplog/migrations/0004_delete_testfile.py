# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0003_logimage')]

    operations = [
        migrations.DeleteModel(
            'TestFile',
        ),
    ]

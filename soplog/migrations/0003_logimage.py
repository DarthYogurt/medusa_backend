# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0002_auto_20140123_1712')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('file', models.FileField(upload_to='/media/'),)],
            bases = (models.Model,),
            options = {},
            name = 'LogImage',
        ),
    ]

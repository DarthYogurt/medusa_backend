# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0001_initial')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.FileField(upload_to=''),)],
            bases = (models.Model,),
            options = {},
            name = 'TestImage',
        ),
    ]

# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=30),), ('description', models.TextField(),)],
            bases = (models.Model,),
            options = {},
            name = 'Group',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=30),), ('description', models.TextField(),), ('groupId', models.ForeignKey(to=u'soplog.Group', to_field=u'id'),)],
            bases = (models.Model,),
            options = {},
            name = 'Checklist',
        ),
    ]

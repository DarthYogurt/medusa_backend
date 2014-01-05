# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0003_auto_20140104_1910')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('checklistLog', models.ForeignKey(to=u'soplog.LogChecklist', to_field=u'id'),), ('value', models.BooleanField(),), ('modifyTime', models.DateTimeField(),)],
            bases = (models.Model,),
            options = {},
            name = 'LogBool',
        ),
    ]

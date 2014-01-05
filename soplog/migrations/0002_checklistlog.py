# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0001_initial')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('checklist', models.ForeignKey(to=u'soplog.Checklist', to_field=u'id'),), ('user', models.ForeignKey(to=u'soplog.User', to_field=u'id'),), ('startTime', models.DateTimeField(),), ('modifyTime', models.DateTimeField(),), ('endtime', models.DateTimeField(),)],
            bases = (models.Model,),
            options = {},
            name = 'ChecklistLog',
        ),
    ]

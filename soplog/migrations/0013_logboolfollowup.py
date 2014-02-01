# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0012_auto_20140130_1233')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('logBool', models.ForeignKey(to=u'soplog.LogBool', to_field=u'id'),), ('user', models.ForeignKey(to=u'soplog.User', to_field=u'id'),), ('complete', models.BooleanField(default=False),), ('completeBy', models.DateTimeField(null=True, blank=True),), ('completedTime', models.DateTimeField(null=True, blank=True),)],
            bases = (models.Model,),
            options = {},
            name = 'LogBoolFollowUp',
        ),
    ]

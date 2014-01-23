# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0005_logbool_loglist_lognumber_logtext')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('logList', models.ForeignKey(to=u'soplog.LogList', to_field=u'id'),), ('step', models.ForeignKey(to=u'soplog.ListStep', to_field=u'id'),), ('file', models.FileField(upload_to='../media/%Y/%m/%d'),), ('modifyTime', models.DateTimeField(null=True),)],
            bases = (models.Model,),
            options = {},
            name = 'LogFile',
        ),
    ]

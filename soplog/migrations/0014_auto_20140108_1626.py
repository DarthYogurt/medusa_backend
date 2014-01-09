# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0013_auto_20140108_1044')]

    operations = [
        migrations.AlterField(
            field = models.DateTimeField(null=True),
            name = 'startTime',
            model_name = 'logchecklist',
        ),
        migrations.AlterField(
            field = models.ForeignKey(to=u'soplog.User', to_field=u'id', null=True),
            name = 'user',
            model_name = 'logchecklist',
        ),
        migrations.AlterField(
            field = models.DateTimeField(null=True),
            name = 'modifyTime',
            model_name = 'logbool',
        ),
        migrations.AlterField(
            field = models.DateTimeField(null=True),
            name = 'modifyTime',
            model_name = 'logtext',
        ),
        migrations.AlterField(
            field = models.DateTimeField(null=True),
            name = 'modifyTime',
            model_name = 'logdouble',
        ),
        migrations.AlterField(
            field = models.DateTimeField(null=True),
            name = 'endtime',
            model_name = 'logchecklist',
        ),
        migrations.AlterField(
            field = models.DateTimeField(null=True),
            name = 'modifyTime',
            model_name = 'logchecklist',
        ),
        migrations.AlterField(
            field = models.DateTimeField(null=True),
            name = 'modifyTime',
            model_name = 'logfile',
        ),
    ]

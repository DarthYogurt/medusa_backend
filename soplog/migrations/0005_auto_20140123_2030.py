# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0004_delete_testfile')]

    operations = [
        migrations.AddField(
            field = models.ForeignKey(to=u'soplog.ListStep', default=1, to_field=u'id'),
            preserve_default = False,
            name = 'step',
            model_name = 'logimage',
        ),
        migrations.AddField(
            field = models.ForeignKey(to=u'soplog.LogList', default=1, to_field=u'id'),
            preserve_default = False,
            name = 'logList',
            model_name = 'logimage',
        ),
        migrations.AddField(
            field = models.DateTimeField(null=True),
            name = 'modifyTime',
            model_name = 'logimage',
        ),
    ]

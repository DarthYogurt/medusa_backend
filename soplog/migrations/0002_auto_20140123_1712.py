# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0001_initial')]

    operations = [
        migrations.AddField(
            field = models.DateTimeField(null=True),
            name = 'endtime',
            model_name = 'loglist',
        ),
        migrations.AddField(
            field = models.ForeignKey(to=u'soplog.User', to_field=u'id', null=True),
            name = 'user',
            model_name = 'loglist',
        ),
        migrations.AddField(
            field = models.ForeignKey(to=u'soplog.List', default=1, to_field=u'id'),
            preserve_default = False,
            name = 'list',
            model_name = 'loglist',
        ),
        migrations.AddField(
            field = models.DateTimeField(null=True),
            name = 'modifyTime',
            model_name = 'loglist',
        ),
        migrations.AddField(
            field = models.DateTimeField(null=True),
            name = 'startTime',
            model_name = 'loglist',
        ),
    ]

# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0012_logbool_step')]

    operations = [
        migrations.AddField(
            field = models.ForeignKey(to=u'soplog.ChecklistStep', default=1, to_field=u'id'),
            preserve_default = False,
            name = 'step',
            model_name = 'logtext',
        ),
        migrations.AddField(
            field = models.ForeignKey(to=u'soplog.ChecklistStep', default=1, to_field=u'id'),
            preserve_default = False,
            name = 'step',
            model_name = 'logfile',
        ),
        migrations.AddField(
            field = models.ForeignKey(to=u'soplog.ChecklistStep', default=1, to_field=u'id'),
            preserve_default = False,
            name = 'step',
            model_name = 'logdouble',
        ),
    ]

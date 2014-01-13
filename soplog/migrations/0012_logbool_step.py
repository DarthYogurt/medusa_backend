# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0011_auto_20140106_1800')]

    operations = [
        migrations.AddField(
            field = models.ForeignKey(to=u'soplog.ChecklistStep', default=1, to_field=u'id'),
            preserve_default = False,
            name = 'step',
            model_name = 'logbool',
        ),
    ]

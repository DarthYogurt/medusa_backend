# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0002_checkliststep')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=10),)],
            bases = (models.Model,),
            options = {},
            name = 'StepType',
        ),
        migrations.AddField(
            field = models.ForeignKey(to=u'soplog.StepType', default=1, to_field=u'id'),
            preserve_default = False,
            name = 'stepTypeId',
            model_name = 'checkliststep',
        ),
    ]

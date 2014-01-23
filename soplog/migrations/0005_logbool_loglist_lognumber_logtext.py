# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('soplog', '0004_auto_20140122_1514')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('list', models.ForeignKey(to=u'soplog.List', to_field=u'id'),), ('user', models.ForeignKey(to=u'soplog.User', to_field=u'id', null=True),), ('startTime', models.DateTimeField(null=True),), ('modifyTime', models.DateTimeField(null=True),), ('endtime', models.DateTimeField(null=True),)],
            bases = (models.Model,),
            options = {},
            name = 'LogList',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('logList', models.ForeignKey(to=u'soplog.LogList', to_field=u'id'),), ('step', models.ForeignKey(to=u'soplog.ListStep', to_field=u'id'),), ('value', models.BooleanField(),), ('modifyTime', models.DateTimeField(null=True),)],
            bases = (models.Model,),
            options = {},
            name = 'LogBool',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('logList', models.ForeignKey(to=u'soplog.LogList', to_field=u'id'),), ('step', models.ForeignKey(to=u'soplog.ListStep', to_field=u'id'),), ('value', models.FloatField(),), ('modifyTime', models.DateTimeField(null=True),)],
            bases = (models.Model,),
            options = {},
            name = 'LogNumber',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('logList', models.ForeignKey(to=u'soplog.LogList', to_field=u'id'),), ('step', models.ForeignKey(to=u'soplog.ListStep', to_field=u'id'),), ('value', models.TextField(),), ('modifyTime', models.DateTimeField(null=True),)],
            bases = (models.Model,),
            options = {},
            name = 'LogText',
        ),
    ]

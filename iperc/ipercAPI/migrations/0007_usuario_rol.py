# Generated by Django 2.2.5 on 2019-09-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipercAPI', '0006_auto_20190912_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.IntegerField(choices=[(0, 'Administrdor'), (1, 'Obrero')], default=0, null=True),
        ),
    ]

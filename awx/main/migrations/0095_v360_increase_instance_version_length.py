# Generated by Django 2.2.4 on 2019-10-04 00:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0094_v360_webhook_mixin2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='version',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-24 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_merge_20200422_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_content',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
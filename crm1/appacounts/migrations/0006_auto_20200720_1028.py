# Generated by Django 3.0.8 on 2020-07-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appacounts', '0005_auto_20200718_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

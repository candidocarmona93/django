# Generated by Django 3.0.8 on 2020-07-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appacounts', '0003_auto_20200718_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='tag',
            field=models.ManyToManyField(to='appacounts.Tag'),
        ),
    ]

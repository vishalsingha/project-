# Generated by Django 2.1 on 2021-01-03 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmhealth', '0010_auto_20210103_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='data_saved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.DeleteModel(
            name='pic_saved',
        ),
    ]

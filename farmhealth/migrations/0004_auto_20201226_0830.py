# Generated by Django 2.1 on 2020-12-26 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmhealth', '0003_tomato_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='tomato_plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=100)),
                ('disease_treatments', models.TextField(max_length=3000)),
                ('disease_control', models.TextField(max_length=3000)),
            ],
        ),
        migrations.DeleteModel(
            name='tomato_description',
        ),
    ]
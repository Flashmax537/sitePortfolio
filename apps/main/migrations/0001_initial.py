# Generated by Django 2.2.2 on 2019-06-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('tagline', models.CharField(max_length=500, verbose_name='tagline')),
                ('icon', models.CharField(max_length=255, verbose_name='icon')),
            ],
        ),
    ]

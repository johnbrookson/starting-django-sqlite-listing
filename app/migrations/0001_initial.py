# Generated by Django 3.0.7 on 2020-07-05 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('url_link', models.CharField(max_length=255, null=True)),
                ('url_img', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]

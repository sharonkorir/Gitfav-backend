# Generated by Django 4.0.4 on 2022-05-14 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('gh_username', models.CharField(max_length=120)),
                ('bio', models.TextField()),
                ('profile_pic_path', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_url', models.URLField()),
                ('api_url', models.URLField()),
                ('owner', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=120)),
                ('languages_url', models.URLField()),
            ],
        ),
    ]

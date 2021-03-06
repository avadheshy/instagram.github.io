# Generated by Django 4.0.5 on 2022-07-16 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_user_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='password',
        ),
        migrations.RemoveField(
            model_name='person',
            name='user_data',
        ),
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='picture',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pictures', verbose_name='DP'),
        ),
        migrations.AddField(
            model_name='person',
            name='website',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

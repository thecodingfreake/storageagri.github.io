# Generated by Django 4.1 on 2023-03-25 05:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0006_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='comment',
        ),
        migrations.AddField(
            model_name='contacts',
            name='message',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sivangangai',
            name='image',
            field=models.CharField(default=django.utils.timezone.now, max_length=2080),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='thanjavur',
            name='image',
            field=models.CharField(default=django.utils.timezone.now, max_length=2080),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='thiruvallur',
            name='image',
            field=models.CharField(default=django.utils.timezone.now, max_length=2080),
            preserve_default=False,
        ),
    ]
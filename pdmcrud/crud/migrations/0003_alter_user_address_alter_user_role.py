# Generated by Django 5.0.7 on 2024-08-01 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_user_address_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('administrator', 'Administrator'), ('editor', 'Editor'), ('reader', 'Reader')], default='reader', max_length=50, verbose_name='Role'),
        ),
    ]

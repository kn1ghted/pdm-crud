# Generated by Django 5.0.7 on 2024-07-31 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('AD', 'Administrator'), ('ED', 'Editor'), ('RE', 'Reader')], default='RE', max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
    ]
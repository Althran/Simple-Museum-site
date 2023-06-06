# Generated by Django 4.1.3 on 2023-06-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=56)),
                ('body', models.TextField()),
                ('slug', models.SlugField(max_length=256)),
            ],
        ),
    ]

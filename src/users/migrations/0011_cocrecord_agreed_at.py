# Generated by Django 3.0.2 on 2020-02-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_cocrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocrecord',
            name='agreed_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='agreed at'),
        ),
    ]

# Generated by Django 4.1 on 2023-12-07 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_anonymouscomplain_complain_is_anonymous'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complain',
            name='is_anonymous',
        ),
        migrations.DeleteModel(
            name='AnonymousComplain',
        ),
    ]

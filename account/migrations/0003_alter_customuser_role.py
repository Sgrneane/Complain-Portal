# Generated by Django 4.1 on 2023-12-08 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_customuser_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'USER'), (2, 'ADMIN'), (3, 'SUPERADMIN'), (4, 'COMPLAIN REVIEWER')], default=1),
        ),
    ]

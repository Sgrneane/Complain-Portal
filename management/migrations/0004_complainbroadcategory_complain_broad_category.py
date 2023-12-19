# Generated by Django 4.1 on 2023-12-15 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_remove_complain_broad_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplainBroadCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.CharField(max_length=50, unique=True)),
                ('nepali_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='complain',
            name='broad_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='broad_category', to='management.complainbroadcategory'),
        ),
    ]
# Generated by Django 4.1 on 2023-12-14 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='abc', max_length=50)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_no', models.CharField(max_length=20)),
                ('complain_title', models.CharField(max_length=300)),
                ('complain_description', models.TextField()),
                ('complain_image', models.ImageField(upload_to='')),
                ('province', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('municipality', models.CharField(max_length=20)),
                ('ward_no', models.CharField(max_length=5)),
                ('tole', models.CharField(max_length=30, null=True)),
                ('complain_status', models.PositiveBigIntegerField(choices=[(1, 'Pending'), (2, 'Processing'), (3, 'Responsed'), (4, 'Rejected')], default=1)),
                ('complain_priority', models.PositiveBigIntegerField(choices=[(1, 'Normal'), (2, 'Urgent'), (3, 'Very Urgent')], default=1)),
                ('complain_secrecy', models.BooleanField(default=False)),
                ('admin_message', models.CharField(max_length=200, null=True)),
                ('assigned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_complain', to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='is_available', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ComplainBroadCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ComplainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_description', models.TextField()),
                ('response_image', models.ImageField(null=True, upload_to='')),
                ('complain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='management.complain')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ComplainSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complainsubcategories', to='management.complaincategory')),
            ],
        ),
        migrations.AddField(
            model_name='complain',
            name='broad_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='broad_category', to='management.complainbroadcategory'),
        ),
        migrations.AddField(
            model_name='complain',
            name='complain_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complain', to='management.complaincategory'),
        ),
        migrations.AddField(
            model_name='complain',
            name='complain_sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complain_sub_category', to='management.complainsubcategory'),
        ),
        migrations.AddField(
            model_name='complain',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_complains', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='complain',
            name='is_anonymous',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.anonymoususer'),
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('communication_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to=settings.AUTH_USER_MODEL)),
                ('communication_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to=settings.AUTH_USER_MODEL)),
                ('complain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complain_communication', to='management.complain')),
            ],
        ),
    ]

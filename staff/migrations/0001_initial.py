# Generated by Django 4.2 on 2023-04-10 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtherDets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StaffLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=300)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=300)),
                ('staff_dept', models.CharField(max_length=200)),
                ('staff_login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Staff', to='staff.stafflogin')),
            ],
        ),
    ]

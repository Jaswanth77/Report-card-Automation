# Generated by Django 4.2 on 2023-04-10 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_pastotherexams_year_of_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastotherexams',
            name='year_of_exam',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]

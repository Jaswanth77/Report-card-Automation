# Generated by Django 4.2 on 2023-04-10 10:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyDets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('relationship', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=200)),
                ('occupation_address', models.CharField(max_length=300)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PastAcademics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_completion', models.DateField()),
                ('past_academic_type', models.CharField(max_length=50)),
                ('cut_off', models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True)),
                ('cgpa', models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True)),
                ('percentage', models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PastOtherExams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=100)),
                ('year_of_exam', models.IntegerField()),
                ('exam_name', models.CharField(max_length=100)),
                ('result', models.DecimalField(decimal_places=6, max_digits=15)),
                ('total', models.DecimalField(decimal_places=6, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='StudentLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.CharField(db_index=True, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('batch_from', models.IntegerField()),
                ('batch_to', models.IntegerField()),
                ('study_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('section', models.CharField(blank=True, max_length=2, null=True)),
                ('dob', models.DateField()),
                ('contact_no', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=600)),
                ('is_hostelite', models.BooleanField()),
                ('family_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Student', to='student.familydets')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentees', to='staff.staff')),
                ('past_academics', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Student', to='student.pastacademics')),
            ],
        ),
        migrations.CreateModel(
            name='SemesterPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_no', models.IntegerField(validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('subject_code', models.CharField(max_length=10)),
                ('grade', models.CharField(choices=[('O', 'O GRADE'), ('A+', 'A+ GRADE'), ('A', 'A GRADE'), ('B+', 'B+ GRADE'), ('B', 'B GRADE'), ('C', 'C GRADE'), ('U', 'FAIL'), ('AB', 'ABSENT'), ('MM', 'MALPRACTICE')], max_length=2)),
                ('cgpa', models.DecimalField(decimal_places=3, max_digits=5)),
                ('roll_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='SemesterPerformance', to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('organisation', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=200)),
                ('certificate', models.FileField(upload_to='')),
                ('roll_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Projects', to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='PlacementDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('results', models.BooleanField()),
                ('package', models.DecimalField(decimal_places=2, max_digits=6)),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PlacementDetails', to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='InternalPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_no', models.IntegerField(validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('exam_type', models.CharField(max_length=100)),
                ('eaxm_number', models.CharField(max_length=100)),
                ('scored_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('percentage_scored', models.DecimalField(decimal_places=2, max_digits=5)),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AcademicDetails', to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('semester_held', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('description', models.CharField(max_length=100)),
                ('document', models.FileField(blank=True, null=True, upload_to='disiplinary/')),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DisiplinaryDetails', to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('total_working_days', models.IntegerField()),
                ('present_working_days', models.IntegerField()),
                ('present_percentage', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True)),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Attendance', to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_held', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('date', models.DateField()),
                ('organization', models.CharField(max_length=300)),
                ('event_name', models.CharField(max_length=200)),
                ('document', models.FileField(blank=True, null=True, upload_to='achievements/')),
                ('status', models.CharField(choices=[('win-1', 'winner'), ('win-2', 'runner'), ('win-3', 'second-runner'), ('participated', 'partcipated')], max_length=30)),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Achievements', to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='AbsentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('absent_type', models.CharField(choices=[('Leave', 'Leave'), ('Absent', 'Absent'), ('OD', 'OD'), ('Late', ' Late')], max_length=20)),
                ('desc', models.CharField(max_length=200)),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AbsentDetails', to='student.student')),
            ],
        ),
    ]

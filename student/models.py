from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
  
class Student(models.Model):
    regno = models.CharField(blank=False,null=False,primary_key=True,db_index=True,unique=True,max_length=10)
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    dob = models.DateField()
    contact_no = models.CharField(max_length=30)
    address = models.CharField(max_length=600)
    is_hostelite = models.BooleanField()
    family_details = models.OneToOneField('student.FamilyDets',on_delete=models.CASCADE,related_name='Student')
    past_academics = models.OneToOneField('student.PastAcademics',on_delete=models.CASCADE,related_name='Student')
    # attendance = models.OneToOneField('student.Attendance',on_delete=models.CASCADE,related_name='student')

class FamilyDets(models.Model):
    name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=100)
    occupation = models.CharField(max_length = 200)
    occupation_address = models.CharField(max_length=300)
    salary = models.DecimalField(max_digits=15,decimal_places=2)
    phone = models.CharField(max_length=30)

class PastAcademics(models.Model):
    year_of_completion = models.DateField()
    past_academic_type = models.CharField(max_length=50)
    cut_off = models.DecimalField(max_digits=15,decimal_places=6,blank = True,null=True)
    cgpa = models.DecimalField(max_digits  = 15,decimal_places=6,blank = True , null=True)
    percentage = models.DecimalField(max_digits= 15, decimal_places=6, blank = True, null=True)

class PastOtherExams(models.Model):
    roll_no= models.ForeignKey('student.Student',on_delete=models.CASCADE,related_name='PastOtherExams')
    year_of_exam = models.DateField()
    exam_name = models.CharField(max_length=100)
    result = models.DecimalField(max_digits=15,decimal_places=6)
    total = models.DecimalField(max_digits=15,decimal_places=6)

class Attendance(models.Model):
    roll_no = models.ForeignKey('student.Student',on_delete=models.CASCADE,related_name='Attendance')
    semester = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(12)])
    # entry_no = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    total_working_days = models.IntegerField()
    present_working_days = models.IntegerField()
    present_percentage = models.DecimalField(max_digits=6,decimal_places=4,blank=True,null=True)
    

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        self.present_percentage = (self.present_working_days/self.total_working_days) * 100
       
class AbsentDetails(models.Model):
    absent_type_choices = [
        ("Leave" , "Leave"),
        ("Absent" , "Absent"),
        ("OD" , "OD"),
        ("Late" , " Late")
    ]
    roll_no = models.ForeignKey('student.Student',on_delete=models.CASCADE,related_name='AbsentDetails')
    semester = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])
    date_from = models.DateField()
    date_to = models.DateField()
    absent_type = models.CharField(max_length=20,choices=absent_type_choices)
    desc = models.CharField(max_length=200)
    
# ####
class InternalPerformance(models.Model):
    roll_no=models.ForeignKey('student.student',on_delete=models.CASCADE,related_name='AcademicDetails')
    semester_no=models.IntegerField(validators=[MaxValueValidator(12),MinValueValidator(1)])
    exam_type = models.CharField(max_length=100)
    eaxm_number = models.CharField(max_length=100)
    scored_marks = models.DecimalField(max_digits=5,decimal_places=2)
    total_marks = models.DecimalField(max_digits=5,decimal_places=2)
    percentage_scored = models.DecimalField(max_digits=5,decimal_places=2)
    
    def save(self,*args,**kwargs):
        super.save(*args,**kwargs)
        self.percentage_scored = (self.scored_marks/self.total_marks) * 100

class SemesterPerformance(models.Model):
    grade_choices=[
        ('O','O GRADE'),
        ('A+','A+ GRADE'),
        ('A','A GRADE'),
        ('B+','B+ GRADE'),
        ('B','B GRADE'),
        ('C','C GRADE'),
        ('U','FAIL'),
        ('AB','ABSENT'),
        ('MM','MALPRACTICE')
    ]
    roll_no = models.OneToOneField('student.AcademicDetails',on_delete=models.CASCADE,related_name='SemesterPerformance')
    semester_no=models.IntegerField(validators=[MaxValueValidator(12),MinValueValidator(1)])
    subject_code=models.CharField(max_length=10)
    grade=models.CharField(max_length=2,choices=grade_choices)
    cgpa = models.DecimalField(max_digits=5,decimal_places=3)


class Projects(models.Model):
    roll_no = models.OneToOneField('student.Student',on_delete=models.CASCADE,related_name='Projects')
    start_Date=models.DateField()
    end_Date=models.DateField()
    organisation=models.CharField(max_length=100)
    specialization=models.CharField(max_length=200)
    certificate=models.FileField()


class Achievements(models.Model):
    status_choices=(
        ('win-1','winner'),
        ('win-2','runner'),
        ('win-3','second-runner'),
        ('participated','partcipated'),
    )
    roll_no = models.ForeignKey('student.Student',on_delete=models.CASCADE,related_name='Achievements')
    date=models.DateField()
    organisation=models.CharField(max_length=300)
    event_name=models.CharField(max_length=200)
    document=models.FileField(upload_to = '/achievements',blank=True,null=True)
    status=models.CharField(max_length=10,choices=status_choices)


class PlacementDetails(models.Model):
    roll_no=models.ForeignKey('student.Student',on_delete=models.CASCADE,related_name='PlacementDetails')
    company_name=models.CharField(max_length=300)
    date=models.DateField()
    results=models.BooleanField()
    package=models.DecimalField()


class DisciplinaryDetails(models.Model):
    roll_no=models.ForeignKey('student.Student',on_delete=models.CASCADE,related_name='DisiplinaryDetails')
    date=models.DateField()
    description=models.CharField(max_length=100)
    document = models.FileField(upload_to='/disiplinary',blank=True,null=True)







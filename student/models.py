from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
  
class Student(models.Model):
    regno = models.IntegerField(blank=False,null=False,primary_key=True,db_index=True)
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    dob = models.DateField()
    contact_no = models.CharField(max_length=30)
    address = models.CharField(max_length=600)
    is_hostelite = models.BooleanField()
    family_details = models.OneToOneField('student.FamilyDets',on_delete=models.CASCADE,related_name='student')
    past_academics = models.OneToOneField('student.PastAcademics',on_delete=models.CASCADE,related_name='student')
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
    other_exams = models.OneToOneField('student.PastOtherExams',on_delete=models.CASCADE)

class PastOtherExams(models.Model):
    year_of_exam = models.DateField()
    exam_name = models.CharField(max_length=100)
    result = models.DecimalField(max_digits=15,decimal_places=6)
    total = models.DecimalField(max_digits=15,decimal_places=6)

class Attendance(models.Model):
    student = models.ForeignKey('student.Student',on_delete=models.CASCADE,related_name='Attendance')
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
    attendance = models.OneToOneField('student.Attendance',on_delete=models.CASCADE,related_name='attendance')
    semester = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])
    date_from = models.DateField()
    date_to = models.DateField()
    absent_type = models.CharField(max_length=20,choices=absent_type_choices)
    desc = models.CharField(max_length=200)
    







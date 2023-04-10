from django.db import models


class Staff(models.Model):
    staff_id = models.CharField(primary_key=True,max_length=300)
    staff_name = models.CharField(max_length=300)
    staff_dept = models.CharField(max_length=200)
    staff_login = models.ForeignKey('staff.StaffLogin',on_delete=models.CASCADE,related_name='Staff')

class StaffLogin(models.Model):
    login_id = models.CharField(max_length=200)
    password = models.CharField(max_length=300)
    desc = models.CharField(max_length=100)

class OtherDets(models.Model):
    desc = models.CharField(max_length=200)

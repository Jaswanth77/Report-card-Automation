from django.db import models


class Staff(models.Model):
    staff_id = models.CharField(primary_key=True,max_length=300)
    staff_name = models.CharField(max_length=300)
    staff_dept = models.CharField(max_length=200)

class StaffLogin(models.Model):
    login_id = models.CharField(max_length=200)
    password = models.CharField(max_length=300)


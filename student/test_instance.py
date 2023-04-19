# Class to provide dummy instances and data for student app
from staff.models import Staff
from .models import Student,FamilyDets,PastAcademics,Attendance
# to create an instance, 
class StudentTestUtil():
    def __init__(self):
        self.staff_data = {
            "staff_id" : "new12344",
            "staff_name"  : "Joel",
            "staff_dept" : "CSE"
        }
        self.student_data = {
            "roll_no": "10fa1",
            "mentor": "new12344",
            "name": "John Doe",
            "course": "B.Tech",
            "department": "CSE",
            "batch_from": 2020,
            "batch_to": 2024,
            "study_year": 2,
            "section": "A",
            "dob": "2001-01-01",
            "contact_no": "9876543210",
            "address": "1234, Main St, City",
            "is_hostelite": True,
            "family_details": {
                "name": "Jane Doe",
                "relationship": "Mother",
                "occupation": "Teacher",
                "occupation_address": "4567, High St, City",
                "salary": "50000.00",
                "phone": "9876543210"
            },
            "past_academics": {
                "year_of_completion": "2019-05-01",
                "past_academic_type": "12th Standard",
                "cut_off": "95.6",
                "cgpa": "9.5",
                "percentage": "95.6"
            }  
        }  
    def getStaffData(self):
        return self.staff_data
    
    def getStaffInstance(self):
        staff_instance = Staff.objects.create(**self.staff_data)
        return staff_instance
    
    def getStudentData(self):
        return self.student_data
    
    def getStudentInstance(self):
        # create dummy data and change its primary key to make a copy out of it
        student_dummy = self.student_data.copy()
        student_dummy['roll_no'] = '123qwas'
        staff_instance = self.getStaffInstance()
        family_dets_instance = FamilyDets.objects.create(**student_dummy.pop('family_details'))
        past_academics_instance = PastAcademics.objects.create(**student_dummy.pop('past_academics'))
        # remove mentor data from student_dummy as it's instance is created and placed to create student instance
        student_dummy.pop('mentor')
        student_instance = Student.objects.create(mentor = staff_instance,family_details = family_dets_instance,
                                                  past_academics = past_academics_instance,**student_dummy)
        return student_instance

class AttendanceTestUtil():
    def __init__(self):
        self.student_util = StudentTestUtil()
        self.student_test_instance = self.student_util.getStudentInstance()
        self.attendance_data = {
            'roll_no' : self.student_test_instance.roll_no,
            'semester' : 2,
            'total_working_days' : 100,
            'present_working_days' : 50
        }
    def getAttendanceData(self):
        return self.attendance_data
    
    def getAttendanceInstance(self):
        # create attendance data copy and remove roll_no to insert instance
        attendance_dummy = self.attendance_data.copy()
        attendance_dummy.pop('roll_no')
        attendance_instance = Attendance.objects.create(roll_no = self.student_test_instance,
                                                        **attendance_dummy)
        return attendance_instance


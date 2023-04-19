from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Student, FamilyDets, PastAcademics,Attendance
from .serializers import StudentSerializer
from .test_instance import StudentTestUtil,AttendanceTestUtil
from staff.models import Staff
client = APIClient()
# create Student module 
class StudentTestCase(TestCase):
    def setUp(self):
        student_test_instance = StudentTestUtil()
        self.student_data = student_test_instance.getStudentData()
        self.student = student_test_instance.getStudentInstance()
        # self.staff_data={
        #     "staff_id" : "new12344",
        #     "staff_name"  : "Joel",
        #     "staff_dept" : "CSE"
        # }
        # self.staff = Staff.objects.create(**self.staff_data)
        # self.student_data = {
        #     "roll_no": "10fa1",
        #     "mentor": self.staff.staff_id,
        #     "name": "John Doe",
        #     "course": "B.Tech",
        #     "department": "CSE",
        #     "batch_from": 2020,
        #     "batch_to": 2024,
        #     "study_year": 2,
        #     "section": "A",
        #     "dob": "2001-01-01",
        #     "contact_no": "9876543210",
        #     "address": "1234, Main St, City",
        #     "is_hostelite": True,
        #     "family_details": {
        #         "name": "Jane Doe",
        #         "relationship": "Mother",
        #         "occupation": "Teacher",
        #         "occupation_address": "4567, High St, City",
        #         "salary": "50000.00",
        #         "phone": "9876543210"
        #     },
        #     "past_academics": {
        #         "year_of_completion": "2019-05-01",
        #         "past_academic_type": "12th Standard",
        #         "cut_off": "95.6",
        #         "cgpa": "9.5",
        #         "percentage": "95.6"
        #     }  
        # }  
        # self.test_student_data = self.student_data.copy()
        # self.test_student_data['roll_no'] = '1234as'
        # self.family_dets_data = self.test_student_data.pop('family_details')
        # self.past_academics_data = self.test_student_data.pop('past_academics')
        # self.test_student_data.pop('mentor')
        # self.family_dets = FamilyDets.objects.create(**self.family_dets_data)
        # self.past_academics = PastAcademics.objects.create(**self.past_academics_data)
        # self.student=Student.objects.create(family_details=self.family_dets,
        #                                     past_academics = self.past_academics,**self.test_student_data,
        #                                     mentor = self.staff)
    def test_create_student(self): 
        student_response = client.post('/student/student/{}'.format('1234w'), self.student_data, format='json')
        self.assertEqual(student_response.status_code,status.HTTP_201_CREATED)

    def test_retrieve_student(self):
        response = client.get('/student/student/{}'.format(self.student.roll_no))
        self.assertEqual(response.data['roll_no'],self.student.roll_no)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_student(self):
        updated_data = {
    'roll_no': self.student.roll_no,
    'mentor': self.student.mentor.staff_id,
    'name': 'jash',
    'course': self.student.course,
    'department': self.student.department,
    'batch_from': self.student.batch_from,
    'batch_to': self.student.batch_to,
    'study_year': self.student.study_year,
    'section': self.student.section,
    'dob': self.student.dob,
    'contact_no': self.student.contact_no,
    'address': self.student.address,
    'is_hostelite': self.student.is_hostelite,
    'family_details': {
        'name': self.student.family_details.name,
        'relationship': self.student.family_details.relationship,
        'occupation': self.student.family_details.occupation,
        'occupation_address': self.student.family_details.occupation_address,
        'salary': self.student.family_details.salary,
        'phone': self.student.family_details.phone,
    },
    'past_academics': {
        'year_of_completion': self.student.past_academics.year_of_completion,
        'past_academic_type': self.student.past_academics.past_academic_type,
        'cut_off': self.student.past_academics.cut_off,
        'cgpa': self.student.past_academics.cgpa,
        'percentage': self.student.past_academics.percentage,
    },
}
        updated_data['name'] = 'jash VCET'
        response = client.put('/student/student/{}'.format(updated_data['roll_no']), updated_data, format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        updated_student = Student.objects.get(roll_no=self.student.roll_no)
        self.assertEqual(updated_student.name, 'jash VCET')

    def test_partial_update_student(self):
        partial_data = {"name": "hariShankar VELAMMAL"}
        response = client.patch('/student/student/{}'.format(self.student.roll_no), partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_student = Student.objects.get(roll_no=self.student.roll_no)
        self.assertEqual(updated_student.name, 'hariShankar VELAMMAL')

    def test_delete_student(self):
        response = client.delete('/student/student/{}'.format(self.student.roll_no))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Student.objects.filter(roll_no=self.student.roll_no).exists())

class AttendanceTestCase(TestCase):
    def setUp(self):
        attendance_test_instance = AttendanceTestUtil()
        self.attendance = attendance_test_instance.getAttendanceInstance()
        self.attendance_data = attendance_test_instance.getAttendanceData()

    def test_insert_attendance(self):
        attendance_response = client.post('/student/attendance/{}'.format(self.attendance_data['roll_no']),self.attendance_data,format='json')
        print(attendance_response.data)
        self.assertEqual(attendance_response.status_code,status.HTTP_201_CREATED)

    def test_get_attendance(self):
         # we get a list of attendance instances from get
        attendance_response = client.get('/student/attendance/{}'.format(self.attendance_data['roll_no']),format='json')
        # check if the instance from response is present in DB
        self.assertTrue(Attendance.objects.filter(id=attendance_response.data[0]['id']).exists())
        self.assertEqual(attendance_response.status_code,status.HTTP_200_OK)
    
    def test_update_attendance(self):
        # to update a particular attendance instance, we would require its id
        attendance_id = self.attendance.id
        attendance_response = client.put('/student/attendance/{}'.format(self.attendance_id))
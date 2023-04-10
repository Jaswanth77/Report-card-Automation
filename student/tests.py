from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Student
from .serializers import StudentSerializer

class StudentViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student_data = {
            "roll_no": "21CSE115",
            "mentor": "201A",
            "name": "John Doe",
            "course": "B.Tech",
            "department": "Computer Science",
            "batch_from": 2020,
            "batch_to": 2024,
            "study_year": 2,
            "section": "A",
            "dob": "2000-01-01",
            "contact_no": "9876543210",
            "address": "123 Main Street, Anytown USA",
            "is_hostelite": True,
            "family_dets": {
                "name": "Jane Doe",
                "relationship": "Mother",
                "occupation": "Teacher",
                "occupation_address": "456 Elm Street, Anytown USA",
                "salary": 50000,
                "phone": "1234567890"
            },
            "past_academics": {
                "year_of_completion": "2019-05-01",
                "past_academic_type": "High School",
                "cut_off": 95.5,
                "cgpa": 8.5,
                "percentage": 85.0,
                "past_other_exams": {
                    "roll_no" : "2001A001",
                    "year_of_exam" : "2000-04-20",
                    "exam_name": "JEE Mains",
                    "result" : 85.0,
                    "total" : 100.00
                }
            }
        }
        self.response = self.client.post(
            reverse('student:StudentInit', kwargs={'roll_no': '21CSE115'}),
            data=self.student_data,
            format='json'
        )

    def test_create_student(self):
        print(Student.objects.all())
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().name, self.student_data['name'])

    # def test_get_student(self):
    #     student = Student.objects.get()
    #     response = self.client.get(reverse('student:studentInit', kwargs={'roll_no': student.roll_no}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     serializer = StudentSerializer(student)
    #     self.assertEqual(response.data, serializer.data)

    # def test_update_student(self):
    #     student = Student.objects.get()
    #     updated_data = {
    #         'name': 'Updated Name',
    #         'study_year': 'Fourth Year'
    #     }
    #     response = self.client.put(
    #         reverse('student-detail', kwargs={'roll_no': student.roll_no}),
    #         data=updated_data,
    #         format='json'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     student.refresh_from_db()
    #     self.assertEqual(student.name, updated_data['name'])
    #     self.assertEqual(student.study_year, updated_data['study_year'])

    # def test_delete_student(self):
    #     student = Student.objects.get()
    #     response = self.client.delete(reverse('student:studentInit', kwargs={'roll_no': student.roll_no}))
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(Student.objects.count(), 0)

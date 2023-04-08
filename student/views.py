from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView

from .serializers import StudentSerializer,AbsentDetailsSerializer,PastOtherExamsSerializer,AttendanceSerializer
from .serializers import InternalPerformanceSerializer,SemesterPerformanceSerializer,ProjectsSerializer,AchievementsSerializer
from .serializers import PlacementDetailsSerializer,DisciplinaryDetailsSerializer

from . models import Student,AbsentDetails,PastOtherExams,Attendance,InternalPerformance
from . models import SemesterPerformance,Projects,Achievements,PlacementDetails,DisciplinaryDetails

class StudentView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'roll_no'

class AbsentDetailsView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    queryset = AbsentDetails.objects.all()
    serializer_class = AbsentDetailsSerializer
    lookup_field = 'roll_no'

class PastOtherExamsVIew(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    queryset = PastOtherExams.objects.all()
    serializer_class = PastOtherExamsSerializer
    lookup_field = 'roll_no'

class AttendanceView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    lookup_field = 'roll_no'

class InternalPerformanceView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    queryset = InternalPerformance.objects.all()
    serializer_class = InternalPerformanceSerializer
    lookup_field = 'roll_no'

class SemesterPerformanceView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    queryset = SemesterPerformance
    serializer_class = SemesterPerformanceSerializer
    lookup_field = 'roll_no'

class ProjectsView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'roll_no'
    
class AchievementsView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer
    lookup_field = 'roll_no'

class PlacementDetailsView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    queryset = PlacementDetails.objects.all()
    serializer_class = PlacementDetailsSerializer
    lookup_field = 'roll_no'

class DisiplinaryDetailsView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    queryset = DisciplinaryDetails.objects.all()
    serializer_class = DisciplinaryDetailsSerializer
    lookup_field = 'roll_no'


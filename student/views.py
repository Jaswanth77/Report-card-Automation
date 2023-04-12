from rest_framework import filters
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListAPIView

from .serializers import StudentSerializer,AbsentDetailsSerializer,PastOtherExamsSerializer,AttendanceSerializer
from .serializers import InternalPerformanceSerializer,SemesterPerformanceSerializer,ProjectsSerializer,AchievementsSerializer
from .serializers import PlacementDetailsSerializer,DisciplinaryDetailsSerializer,StudentLoginSerializer

from . models import Student,AbsentDetails,PastOtherExams,Attendance,InternalPerformance,StudentLogin
from . models import SemesterPerformance,Projects,Achievements,PlacementDetails,DisciplinaryDetails

from rest_framework.response import Response
class StudentLoginView(CreateAPIView):
    queryset = StudentLogin.objects.all()
    serializer_class = StudentLoginSerializer
    
class StudentView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'roll_no'
    filter_backends = [filters.SearchFilter]
    search_fields = ['roll_no','course','department','batch_from','batch_to','is_hostelite','study_year','section']
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data = request.data)
    #     if not serializer.is_valid():
    #         print(serializer.errors)
    #     self.perform_create(serializer)
    #     return Response(serializer.data,status=200)

class PastOtherExamsView(CreateAPIView,UpdateAPIView,DestroyAPIView,ListAPIView):
    queryset = PastOtherExams.objects.all()
    serializer_class = PastOtherExamsSerializer()
    lookup_field = 'roll_no'
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        print(serializer.is_valid())
        self.perform_create(serializer)
        return Response(serializer.data,status=200)


class AbsentDetailsView(CreateAPIView,UpdateAPIView,DestroyAPIView,ListAPIView):
    queryset = AbsentDetails.objects.all()
    serializer_class = AbsentDetailsSerializer
    lookup_field = 'id'
    search_fields =  ['roll_no','semester','date_from','date_to',
                     'absent_type','roll_no__course','roll_no__department' ,'roll_no__batch_from',
                     'roll_no__batch_to','roll_no__study_year','roll_no__section','roll_no__is_hostelite']
    
    def get_queryset(self):
        queryset = AbsentDetails.objects.all()
        filter_params = {
                    'roll_no': self.request.query_params.get('roll_no', None),
                    'semester': self.request.query_params.get('semester', None),
                    'date_from': self.request.query_params.get('date_from', None),
                    'date_to': self.request.query_params.get('date_to', None),
                    'absent_type': self.request.query_params.get('absent_type', None),
                    'roll_no__course': self.request.query_params.get('course', None),
                    'roll_no__department': self.request.query_params.get('department', None),
                    'roll_no__batch_from': self.request.query_params.get('batch_from', None),
                    'roll_no__batch_to': self.request.query_params.get('batch_to', None),
                    'roll_no__study_year': self.request.query_params.get('study_year', None),
                    'roll_no__section': self.request.query_params.get('section', None),
                    'roll_no__is_hostelite': self.request.query_params.get('is_hostelite', None)
                    }
        absent_filters = {}
        for key in filter_params.keys():
            if(filter_params[key] is not None):
                absent_filters[key] = filter_params[key]
        queryset = queryset.filter(**absent_filters)
        return queryset


class PastOtherExamsView(CreateAPIView,UpdateAPIView,DestroyAPIView,ListAPIView):
    queryset = PastOtherExams.objects.all()
    serializer_class = PastOtherExamsSerializer
    lookup_field = 'roll_no'
    filter_backends = [filters.SearchFilter]
    search_fields = ['roll_no']
    

class AttendanceView(CreateAPIView,UpdateAPIView,DestroyAPIView,ListAPIView):
    queryset =Attendance.objects.all()
    serializer_class = AttendanceSerializer
    lookup_field = 'id'
    search_fields = ['roll_no','semester','roll_no__course','roll_no__department',
                     'roll_no__batch_from','roll_no__batch_to','roll_no__study_year','roll_no__section',
                     'roll_no__is_hostelite']
    
    def get_queryset(self):
        queryset = Attendance.objects.all()
        filter_params = {
                    'roll_no': self.request.query_params.get('roll_no', None),
                    'semester': self.request.query_params.get('semester', None),
                    'roll_no__course': self.request.query_params.get('course', None),
                    'roll_no__department': self.request.query_params.get('department', None),
                    'roll_no__batch_from': self.request.query_params.get('batch_from', None),
                    'roll_no__batch_to': self.request.query_params.get('batch_to', None),
                    'roll_no__study_year': self.request.query_params.get('study_year', None),
                    'roll_no__section': self.request.query_params.get('section', None),
                    'roll_no__is_hostelite': self.request.query_params.get('is_hostelite', None)
        }
        filter_attendance = {}
        for key in filter_params.keys():
            if(filter_params[key] is not None):
                filter_attendance[key] = filter_params[key]
        queryset = queryset.filter(**filter_attendance)
        return queryset
        

class InternalPerformanceView(CreateAPIView,UpdateAPIView,DestroyAPIView,ListAPIView):
    queryset = InternalPerformance.objects.all()
    serializer_class = InternalPerformanceSerializer
    lookup_field = 'id'
    search_fields = ['roll_no','semester_no','exam_type','exam_number','roll_no__course','roll_no__department',
                     'roll_no__batch_from','roll_no__batch_to','roll_no__study_year','roll_no__section']

    def get_queryset(self):
        queryset = InternalPerformance.objects.all()
        filter_params = {
            'roll_no': self.request.query_params.get('roll_no', None),
            'semester_no': self.request.query_params.get('semester_no', None),
            'exam_type': self.request.query_params.get('exam_type', None),
            'exam_number': self.request.query_params.get('exam_number', None),
            'roll_no__course': self.request.query_params.get('course', None),
            'roll_no__department': self.request.query_params.get('department', None),
            'roll_no__batch_from': self.request.query_params.get('batch_from', None),
            'roll_no__batch_to': self.request.query_params.get('batch_to', None),
            'roll_no__study_year': self.request.query_params.get('study_year', None),
            'roll_no__section': self.request.query_params.get('section', None)
        }
        filter_kwargs = {}
        for key in filter_params.keys():
            if filter_params[key] is not None:
                filter_kwargs[key] = filter_params[key]
        queryset = queryset.filter(**filter_kwargs)
        return queryset
    
class SemesterPerformanceView(CreateAPIView,UpdateAPIView,DestroyAPIView,ListAPIView):
    queryset = SemesterPerformance
    serializer_class = SemesterPerformanceSerializer
    lookup_field = 'id'
    search_fields = ['roll_no','semester_no','subject_code','grade','roll_no__course','roll_no__department',
                     'roll_no__batch_from','roll_no__batch_to','roll_no__study_year','roll_no__section']
    def get_queryset(self):
        queryset = SemesterPerformance.objects.all()
        filter_params = {
            'roll_no': self.request.query_params.get('roll_no', None),
            'semester_no': self.request.query_params.get('semester_no', None),
            'subject_code': self.request.query_params.get('subject_code', None),
            'grade': self.request.query_params.get('grade', None),
            'roll_no__course': self.request.query_params.get('course', None),
            'roll_no__department': self.request.query_params.get('department', None),
            'roll_no__batch_from': self.request.query_params.get('batch_from', None),
            'roll_no__batch_to': self.request.query_params.get('batch_to', None),
            'roll_no__study_year': self.request.query_params.get('study_year', None),
            'roll_no__section': self.request.query_params.get('section', None)
        }
        filter_kwargs = {}
        for key in filter_params.keys():
            if filter_params[key] is not None:
                filter_kwargs[key] = filter_params[key]
        queryset = queryset.filter(**filter_kwargs)
        return queryset
    

class ProjectsView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'id'
    search_fields = ['roll_no','start_date','end_date','organization','specialization','certificate',
                     'roll_no__course','roll_no__department',
                     'roll_no__batch_from','roll_no__batch_to','roll_no__study_year','roll_no__section']
    
    def get_queryset(self):
        queryset = Projects.objects.all()
        filter_params = {
            'roll_no': self.request.query_params.get('roll_no', None),
            'start_date': self.request.query_params.get('start_date', None),
            'end_date': self.request.query_params.get('end_date', None),
            'organization': self.request.query_params.get('organization', None),
            'specialization': self.request.query_params.get('specialization', None),
            'certificate': self.request.query_params.get('certificate', None),
            'roll_no__course': self.request.query_params.get('course', None),
            'roll_no__department': self.request.query_params.get('department', None),
            'roll_no__batch_from': self.request.query_params.get('batch_from', None),
            'roll_no__batch_to': self.request.query_params.get('batch_to', None),
            'roll_no__study_year': self.request.query_params.get('study_year', None),
            'roll_no__section': self.request.query_params.get('section', None)
        }
        filter_kwargs = {}
        for key in filter_params.keys():
            if filter_params[key] is not None:
                filter_kwargs[key] = filter_params[key]
        queryset = queryset.filter(**filter_kwargs)
        return queryset
        
    
class AchievementsView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListAPIView):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer
    lookup_field = 'id'
    search_fields = ['roll_no','semester','date','organization','event_name','status',
                     'roll_no__course','roll_no__department','roll_no__batch_from',
                     'roll_no__batch_to','roll_no__study_year','roll_no__section']
    
    def get_queryset(self):
        queryset = Attendance.objects.all()
        filter_params = {
            'roll_no': self.request.query_params.get('roll_no', None),
            'semester': self.request.query_params.get('semester', None),
            'date': self.request.query_params.get('date', None),
            'organization': self.request.query_params.get('organization', None),
            'event_name': self.request.query_params.get('event_name', None),
            'status': self.request.query_params.get('status', None),
            'roll_no__course': self.request.query_params.get('course', None),
            'roll_no__department': self.request.query_params.get('department', None),
            'roll_no__batch_from': self.request.query_params.get('batch_from', None),
            'roll_no__batch_to': self.request.query_params.get('batch_to', None),
            'roll_no__study_year': self.request.query_params.get('study_year', None),
            'roll_no__section': self.request.query_params.get('section', None)
        }
        filter_kwargs = {}
        for key in filter_params.keys():
            if filter_params[key] is not None:
                filter_kwargs[key] = filter_params[key]
        queryset = queryset.filter(**filter_kwargs)
        return queryset
    
class PlacementDetailsView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListAPIView):
    queryset = PlacementDetails.objects.all()
    serializer_class = PlacementDetailsSerializer
    lookup_field = 'id'
    search_fields =['roll_no','company_name','date','results','roll_no__course',
                    'roll_no__department','roll_no__batch_from',
                    'roll_no__batch_to','roll_no__study_year','roll_no__section']
    
    def get_queryset(self):
        queryset = PlacementDetails.objects.all()
        filter_params = {
            'roll_no': self.request.query_params.get('roll_no', None),
            'company_name': self.request.query_params.get('company_name', None),
            'date': self.request.query_params.get('date', None),
            'results': self.request.query_params.get('results', None),
            'roll_no__course': self.request.query_params.get('course', None),
            'roll_no__department': self.request.query_params.get('department', None),
            'roll_no__batch_from': self.request.query_params.get('batch_from', None),
            'roll_no__batch_to': self.request.query_params.get('batch_to', None),
            'roll_no__study_year': self.request.query_params.get('study_year', None),
            'roll_no__section': self.request.query_params.get('section', None)
        }
        filter_kwargs = {}
        for key in filter_params.keys():
            if filter_params[key] is not None:
                filter_kwargs[key] = filter_params[key]
        queryset = queryset.filter(**filter_kwargs)
        return queryset

class DisiplinaryDetailsView(CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListAPIView):
    queryset = DisciplinaryDetails.objects.all()
    serializer_class = DisciplinaryDetailsSerializer
    lookup_field = 'id'
    search_fields = ['roll_no','date','semester_held','roll_no__course',
                     'roll_no__department','roll_no__batch_from',
                     'roll_no__batch_to','roll_no__study_year','roll_no__section']
    
    def get_queryset(self):
        queryset = DisciplinaryDetails.objects.all()
        filter_params = {
            'roll_no': self.request.query_params.get('roll_no', None),
            'date': self.request.query_params.get('date', None),
            'semester_held': self.request.query_params.get('semester_held', None),
            'roll_no__course': self.request.query_params.get('course', None),
            'roll_no__department': self.request.query_params.get('department', None),
            'roll_no__batch_from': self.request.query_params.get('batch_from', None),
            'roll_no__batch_to': self.request.query_params.get('batch_to', None),
            'roll_no__study_year': self.request.query_params.get('study_year', None),
            'roll_no__section': self.request.query_params.get('section', None)
        }
        filter_kwargs = {}
        for key in filter_params.keys():
            if filter_params[key] is not None:
                filter_kwargs[key] = filter_params[key]
        queryset = queryset.filter(**filter_kwargs)
        return queryset

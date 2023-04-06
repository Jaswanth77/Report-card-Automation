from rest_framework import serializers
from . models import Attendance,AbsentDetails,FamilyDets
from . models import PastAcademics,PastOtherExams,Student
from .models import InternalPerformance,SemesterPerformance,Projects,Achievements
from .models import PlacementDetails,DisciplinaryDetails
# partial = True for serializer.save()


#insert family details only with student init data
class FamilyDetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyDets
        fields = '__all__'
        exclude = ['id']

#insert Past academic details only with student init data
class PastAcademicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastAcademics
        fields = '__all__'
        exclude = ['id']
        


# Enter student init data along with family_details and past_academics
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['id']
    family_dets = FamilyDetsSerializer(many=False)
    past_academics = PastAcademicsSerializer(many=False)


    def create(self,validated_data):
        family_dets = validated_data.pop('family_dets')
        past_academics = validated_data.pop('past_academics')
        past_other_exams = past_academics.pop('past_other_exams')
        family_instance = FamilyDets.objects.create(**family_dets)
        past_academics_instance = PastAcademics.objects.create(**past_academics)
        student_instance = Student.objects.create(family_details = family_instance,
                                                  past_academics = past_academics_instance,
                                                    **validated_data)
        PastOtherExams.objects.create(roll_no = student_instance,**past_other_exams)
        return student_instance


# insert absent Details without attendance entry
class AbsentDetailsSerializer(serializers.ModelSerializer):
    student_instance = StudentSerializer()
    class Meta:
        model = AbsentDetails
        fields = '__all__'
        exclude = ['id']

#insert Past other exams only with student init data
class PastOtherExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastOtherExams
        fields = '__all__'
        exclude = ['id']

# to view and insert attendance 
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        exclude = ['id']

class InternalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalPerformance
        fields = "__all__"
        exclude = ['id']
    
class SemesterPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterPerformance
        fields = "__all__"
        exclude = ['id']

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"
        exclude = ['id']

class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = "__all__"
        exclude = ['id']
class PlacementDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementDetails
        fields = "__all__"
        exclude = ['id']

class DisciplinaryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplinaryDetails
        fields = "__all__"
        exclude = ['id']
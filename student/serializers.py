from rest_framework import serializers
from . models import Attendance,AbsentDetails,FamilyDets,PastAcademics,PastOtherExams,Student
# partial = True for serializer.save()

# insert absent Details without attendance entry
class AbsentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbsentDetails
        fields = '__all__'
        exclude = ['id']

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
#insert Past other exams only with student init data
class PastOtherExams(serializers.ModelSerializer):
    class Meta:
        model = PastOtherExams
        fields = '__all__'
        exclude = ['id']

# to view and insert attendance and absent reason together
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        exclude = ['id']

    # Insert attendance data along with absent reason
    absent_dets = AbsentDetailsSerializer(many=False)
    def create(self, validated_data):
        absent_details = validated_data.pop('absent_details')
        student_attendance = Attendance.objects.create(**validated_data)
        AbsentDetails.objects.create(attendance = student_attendance , **absent_details)
        return student_attendance

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
        # past_other_exams = validated
        family_instance = FamilyDets.objects.create(**family_dets)
        past_other_exams_instance = PastOtherExams.objects.create(**past_other_exams)
        past_academics_instance = PastAcademics.objects.create(other_exams = past_other_exams_instance,**past_academics)
        student_instance = Student.objects.create(family_details = family_instance,past_academics = past_academics_instance, **validated_data)
        return student_instance

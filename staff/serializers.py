from rest_framework import serializers
from .models import Staff,StaffLogin,OtherDets


class StaffLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffLogin
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    staff_login = StaffLoginSerializer(many=False)
    class Meta:
        model = Staff
        fields = '__all__'
    def create(self, validated_data):
        print('\n\n\n\n',validated_data,'\n\n\n')
        staff_login_data = validated_data.pop('staff_login')
        other_dets_data = validated_data.pop('other_dets')
        staff_login_instance = StaffLogin.objects.create(**staff_login_data)
        staff_instance = Staff.objects.create(staff_login = staff_login_instance,**validated_data)
        OtherDets.objects.create(**other_dets_data)  
        return staff_instance  
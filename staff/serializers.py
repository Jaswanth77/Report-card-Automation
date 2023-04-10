from rest_framework import serializers
from .models import Staff,StaffLogin


class StaffLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffLogin
        fields = '__all__'
    def create(self, validated_data):
        print(validated_data,'lkhjk')
        desc_data = validated_data.pop('desc')
        staff_login_instance = StaffLogin.objects.create(**validated_data,desc=desc_data)
        return staff_login_instance

class StaffSerializer(serializers.ModelSerializer):
    staff_login = StaffLoginSerializer(many=True)
    class Meta:
        model = Staff
        fields = '__all__'
    def create(self, validated_data):
        print('\n\n',validated_data,'mnbvft')
        staff_login_data = validated_data.pop('staff_login_data')
        staff_login_instance = StaffLogin.objects.create(**staff_login_data)
        staff_instance = Staff.objects.create(staff_login = staff_login_instance,**validated_data)
        return staff_instance


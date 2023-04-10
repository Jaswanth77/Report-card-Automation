from rest_framework import serializers
from .models import Staff,StaffLogin,OtherDets


class StaffLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffLogin
        fields = '__all__'

class OtherDetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherDets
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    staff_login = StaffLoginSerializer()
    class Meta:
        model = Staff
        fields = '__all__'
    
    def create(self, validated_data):
        staff_login_data = validated_data.pop('staff_login')
        staff_login_instance = StaffLogin.objects.create(**staff_login_data)
        staff_instance = Staff.objects.create(staff_login = staff_login_instance,**validated_data)
        return staff_instance

        
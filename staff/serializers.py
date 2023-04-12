from rest_framework import serializers
from .models import Staff,StaffLogin

class StaffLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffLogin
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

        
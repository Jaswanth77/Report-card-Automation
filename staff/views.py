from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from .serializers import StaffLoginSerializer,StaffSerializer
from .models import Staff,StaffLogin
from rest_framework import parsers
class StaffView(CreateAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    parser_classes = [parsers.JSONParser]

class StaffLoginView(CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    parser_classes = [parsers.JSONParser]
    serializer_class = StaffLoginSerializer
    queryset = StaffLogin.objects.all()
    lookup_field = 'staff_id'

    
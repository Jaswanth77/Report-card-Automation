from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from .serializers import StaffLoginSerializer,StaffSerializer,OtherDetsSerializer
from .models import Staff,StaffLogin,OtherDets
from rest_framework import parsers
from rest_framework.response import Response

class StaffLoginView(CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class = StaffLoginSerializer
    queryset = StaffLogin.objects.all()
    parser_classes = [parsers.JSONParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        print('asfd',serializer)
        print(serializer.is_valid())
        self.perform_create(serializer)
        print('this is a demo','\n\n\n\n',serializer.data)
        return Response(serializer.data,status=200)
    

class StaffView(CreateAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    parser_classes = [parsers.JSONParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        print('a\ne\ni',serializer)
        print(serializer.is_valid())
        self.perform_create(serializer)
        print('this is a demo','\n\n\n\n',serializer.data)
        return Response(serializer.data,status=200)
    
class OtherDetsViews(CreateAPIView):
    serializer_class = OtherDetsSerializer
    queryset = OtherDets.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        print('a\ne\ni',serializer)
        print(serializer.is_valid())
        self.perform_create(serializer)
        print('this is a demo','\n\n\n\n',serializer.data)
        return Response(serializer.data,status=200)


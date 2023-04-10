from django.contrib import admin
from django.urls import path
from .views import StaffView,StaffLoginView,OtherDetsViews

urlpatterns = [
    path('otherDets/',OtherDetsViews.as_view()),
    path('staff/',StaffView.as_view()),
    path('staffLogin/',StaffLoginView.as_view())
]

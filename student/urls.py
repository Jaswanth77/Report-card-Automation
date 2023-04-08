from django.contrib import admin
from django.urls import path
from .views import StudentView,AbsentDetailsView,PastOtherExamsVIew,AttendanceView,InternalPerformanceView
from .views import SemesterPerformanceView,ProjectsView,AchievementsView,PlacementDetailsView,DisiplinaryDetailsView

urlpatterns = [
    path('student/<str:roll_no>', StudentView.as_view()),
    path('absentDetails/<str:roll_no>',AbsentDetailsView.as_view()),
    path('pastOtherExams/<str:roll_no>',PastOtherExamsVIew.as_view()),
    path('attendance/<str:roll_no>',AttendanceView.as_view()),
    path('internalPerformance/<str:roll_no>',InternalPerformanceView.as_view()),
    path('semesterPerformance/<str:roll_no>',SemesterPerformanceView.as_view()),
    path('projects/<str:roll_no>',ProjectsView.as_view()),
    path('achievements/<str:roll_no>',AchievementsView.as_view()),
    path('placementDetails/<str:roll_no>',PlacementDetailsView.as_view()),
    path('disiplinaryDetails/<str:roll_no>',DisiplinaryDetailsView.as_view())
]

from django.urls import path
from school.api import views


urlpatterns = [
    path('promote-student/', views.studentPromoteView, name='studentPromote')
]

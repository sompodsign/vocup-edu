from django.urls import path
from . import views
from django.urls import include
from rest_framework import routers

app_name = 'courses'

router = routers.DefaultRouter()
router.register(r'courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    # path('courses/<pk>/enroll/', views.CourseEnrollView.as_view(), name='course_enroll'),

]

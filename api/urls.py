from django.urls import path
from Myapp import views

urlpatterns = [
    path('student/',views.manage_student),
    path('room/',views.manage_room),
    path('payment/',views.manage_payment),
    path('complaint/',views.manage_complaint),
]

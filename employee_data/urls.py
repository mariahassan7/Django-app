from django.urls import path
from employee_data import views

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path("<int:id>/", views.employee, name='employee'),
]
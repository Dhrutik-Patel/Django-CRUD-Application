from CRUD_APP import views
from django.urls import path

urlpatterns = [
    path('', views.employee_form, name='employee_form'),
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('delete/<int:id>', views.employee_delete, name='employee_delete'),
    path('list/', views.employee_list, name='employee_list'),
]
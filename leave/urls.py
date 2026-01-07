from django.urls import path
from .views import *
urlpatterns = [
    
    path('dashboard_page/', dashboard_page, name='dashboard_page'),
    path('leave_api/', LeaveView.as_view(), name='leave_api'),
    path('leave_api/<int:pk>/', LeaveView.as_view(), name='leave_api_with_id'),

]

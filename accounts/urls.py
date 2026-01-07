from django.urls import path
from accounts.views import *

urlpatterns = [
    path('', login_page, name='login_page'),
    path('login_api/', LoginView.as_view(), name='login_api'),
    path('registration_page/', registration_page, name='registration_page'),
    path('registration_api/', RegistrationView.as_view(), name='registration_api'),

]
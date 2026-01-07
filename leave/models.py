from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User

# Create your models here.


class LeaveRequest(models.Model):
    leave_type = models.CharField(max_length=30)
    leave_reason = models.CharField(max_length=200)
    leave_start_date = models.DateTimeField()
    leave_end_date = models.DateTimeField()
    leave_status = models.CharField(max_length=20, null=True, default='Pending')
    leave_remark = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, related_name='user_leaverequest', on_delete=models.CASCADE)
    
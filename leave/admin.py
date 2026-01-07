from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'leave_type', 'leave_reason', 'leave_start_date', 'leave_end_date', 'leave_status', 'leave_remark', 'user']




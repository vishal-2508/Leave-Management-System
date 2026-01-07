from rest_framework import serializers
from .models import LeaveRequest



class LeaveSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = LeaveRequest
        fields = "__all__"
        include = ["username"]

        

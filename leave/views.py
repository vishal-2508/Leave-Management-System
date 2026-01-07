from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import LeaveRequest
from .serializers import LeaveSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def dashboard_page(request):
    return render(request, 'leave/dashboard.html')


class LeaveView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_object = request.user
        user_type = user_object.user_type
        if user_type == "Employee":
            leaverequest_detail = LeaveRequest.objects.filter(user=user_object).order_by("-id")
        else:
            leaverequest_detail = LeaveRequest.objects.all().order_by("-id")
        serializer = LeaveSerializer(leaverequest_detail, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialize = LeaveSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk is None:
            return Response({'massage':'leaverequest id is compulsory requied.'})
        try:
            leaverequest_object = LeaveRequest.objects.get(id = pk)
        except Exception as e:
            return Response({"massage" : str(e)})
        serialize = LeaveSerializer(leaverequest_object, data=request.data, partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is None:
            return Response({'massage':'leaverequest id is compulsory requied.'})
        try:
            leaverequest_object = LeaveRequest.objects.get(id = pk)
            leaverequest_object.delete()
            return Response({'success':'delete successfully..'})
        except Exception as e:
            return Response({'massage': str(e)})
        

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import QAndAnswers
from .serializers import QAndAnswersSerializer

class QAndAnsList(APIView):
    """view to list all qs and ans in database"""

    def get(self,request):
        qAndAns = QAndAnswers.objects.all()
        data = QAndAnswersSerializer(qAndAns,many=True).data
        return Response(data)

    def post(self,request):
        serializer = QAndAnswersSerializer(data =request.data )
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data,status =status.HTTP_201_CREATED)

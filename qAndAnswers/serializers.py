from rest_framework import serializers
from .models import QAndAnswers

class QAndAnswersSerializer(serializers.ModelSerializer):
     """"serializes the Q and Ans object"""
    
     class Meta:
        model = QAndAnswers
        fields = '__all__'
        lookup_field = 'slug'
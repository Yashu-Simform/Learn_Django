from rest_framework import serializers
from .models import StudentProfile

class StudentBaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentProfile
        fields = '__all__'
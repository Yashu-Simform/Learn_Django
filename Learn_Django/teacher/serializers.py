from rest_framework import serializers
from .models import TeacherProfile
from django.contrib.auth.models import User
from rest_framework.reverse import reverse

class TeacherBaseSerializer(serializers.ModelSerializer):
    
    url = serializers.SerializerMethodField(read_only=True)
    hyperlink = serializers.HyperlinkedIdentityField(
        view_name='teacher-detail',
        lookup_field = 'teacher_id'
    )
    
    class Meta:
        model = TeacherProfile
        fields = '__all__'

    def get_url(self, obj):
        request = self.context.get('request')   #get the self.request

        if request is None:
            return None
        
        # return reverse('teacher-detail', kwargs={'teacher_id': obj.teacher_id}, request=request)
        return reverse('teacher-detail', kwargs={'teacher_id': obj.teacher_id}, request=request)
    
    # Custom validations
    def validate_mobile_number(self, value):
        if len(value) != 10:
            raise serializers.ValidationError(f'Validation Error: {value} is not a valid mobile number!')
        
        if not value.isdigit():
            raise serializers.ValidationError(f'Type error: {value} contains character other than number.')
        
        return value
    
class TeacherSerializer(serializers.ModelSerializer):
    pass
from rest_framework import viewsets, mixins

from .serializers import TeacherBaseSerializer
from .models import TeacherProfile


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherBaseSerializer
    lookup_field = 'teacher_id'

class TeacherGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherBaseSerializer
    lookup_field = 'teacher_id'


teacher_list_view = TeacherGenericViewSet.as_view({'get': 'list'})
teacher_detail_view = TeacherGenericViewSet.as_view({'get': 'retrieve'})
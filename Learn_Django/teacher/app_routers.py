from rest_framework.routers import DefaultRouter

from .app_viewset import TeacherViewSet

router = DefaultRouter()
router.register('teacher-abc', TeacherViewSet, basename='teacher')
# router.register('teacher-list', teacher_list_view, basename='teacherlist')

print(router.urls)

urlpatterns = router.urls
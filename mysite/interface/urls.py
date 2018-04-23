from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.department, name='department'),
    path('chapters/<int:course_id>', views.chapters, name='chapters'),
    path('course/<int:department_id>', views.course, name='course')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
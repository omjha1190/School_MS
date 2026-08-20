from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school_admin/', include('school_admin.urls')),
    path('teachers/', include('teachers.urls')),
    path('students/', include('students.urls')),
    path('academics/', include('academics.urls')),
    path('attendance/', include('attendance.urls')),
    path('examination/', include('examinations.urls')),
    path('notices/', include('notices.urls')),
    path('transport/', include('transport.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
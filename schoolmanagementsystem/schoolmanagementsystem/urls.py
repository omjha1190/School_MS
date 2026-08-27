from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school_admin/', include('school_admin.urls')),
    path('teachers/', include('teachers.urls')),
    path('students/', include('students.urls')),
    path('academics/', include('academics.urls')),
    path('attendance/', include('attendance.urls')),
    path('notices/', include('notices.urls')),
    path('examination/', include('examination.urls')),
    path('fees/', include('fees.urls')),
    path('transport/', include('transport.urls')),
    path('staff/', include('staffs.urls')),
    path('payments/', include('staffpayments.urls')),
    path('assignments/', include('assignments.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
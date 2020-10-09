
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
# views
from reportService.views import ReportViewSet

# registrar urls
router = routers.DefaultRouter()
router.register('api',ReportViewSet,basename='reporting')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('',include(router.urls)),

]

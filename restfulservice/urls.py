from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

from apply_rest_service import views
from db_tables.models import Player,Items

router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'items', views.ItemsViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^frontend/', include('frontend.urls')),
]

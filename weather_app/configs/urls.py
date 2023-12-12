from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from weather_api.views import (
    homeviews,
    weather_history,
)

router = DefaultRouter()

# Routers para chamada das views
router.register(r'weather_history', weather_history.PrevisaoTempoHistoryViewSet, basename='weather_history')


urlpatterns = [
    path('', homeviews.index, name="index"),
    path('api/', include(router.urls)),
]
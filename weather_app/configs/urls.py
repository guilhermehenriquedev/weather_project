from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from weather_api.views import (
    homeviews,
    weather_history,
    weather_forecast
)

router = DefaultRouter()

# Routers para chamada das views
router.register(r'weather_history', weather_history.PrevisaoTempoHistoryViewSet, basename='weather_history')
router.register(r'weather_forecast', weather_forecast.WeatherForecastViewSet, basename='weather_forecast')

urlpatterns = [
    path('', homeviews.index, name="index"),
    path('api/', include(router.urls)),
]
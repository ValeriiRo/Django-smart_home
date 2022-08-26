from django.urls import path
from measurement.views import SensorViewAll, SensorView, MeasurementsAdd
urlpatterns = [
    path('sensor/', SensorViewAll.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementsAdd.as_view()),
]

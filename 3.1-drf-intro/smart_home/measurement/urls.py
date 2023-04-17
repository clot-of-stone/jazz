from django.urls import path
from .views import CreateSensorView, ChangeSensorView, CreateMeasurementView, \
    SensorDetailsView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/<pk>/', SensorDetailsView.as_view()),
    path('sensors/create/', CreateSensorView.as_view()),
    path('sensors/change/<pk>/', ChangeSensorView.as_view()),
    path('measurements/', CreateMeasurementView.as_view()),
    path('measurements/view/<pk>/', MeasurementView.as_view()),
]

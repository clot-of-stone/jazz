from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='sensor',
                               on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

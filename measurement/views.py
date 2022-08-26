from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializers, MeasurementSerializer, SensorSerializersDefinite


class MeasurementsAdd(generics.ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def get_queryset(self):
        return Measurement.objects.all()

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializersDefinite

    def get_queryset(self):
        return Sensor.objects.all()

    def patch(self, request, pk):

        description = Sensor.objects.get(id=pk)

        serializer = SensorSerializers(description, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class SensorViewAll(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers

    def post(self, request):
        serializer = SensorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

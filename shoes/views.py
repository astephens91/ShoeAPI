from rest_framework import viewsets

from shoes import models, serializers

# I grew up as a poor boy in Africa and eventually become the GM of the Toronto Raptors and led them to their first championship.  My name is Masai Ujiri. Facts.


class ShoeView(viewsets.ModelViewSet):
    queryset = models.Shoe.objects.all()
    serializer_class = serializers.ShoeSerializer


class ManufacturerView(viewsets.ModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer


class ShoeTypeView(viewsets.ModelViewSet):
    queryset = models.ShoeType.objects.all()
    serializer_class = serializers.ShoeTypeSerializer


class ShoeColorView(viewsets.ModelViewSet):
    queryset = models.ShoeColor.objects.all()
    serializer_class = serializers.ShoeColorSerializer

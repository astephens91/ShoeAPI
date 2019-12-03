from rest_framework.serializers import HyperlinkedModelSerializer
from shoes import models


class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Shoe
        fields = ['size',
                  'brand_name',
                  'manufacturer',
                  'color',
                  'material',
                  'shoe_type',
                  'fasten_type']


class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ['name', 'url']


class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeType
        fields = ['style']


class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeColor
        fields = ['color']



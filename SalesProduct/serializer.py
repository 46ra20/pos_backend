from rest_framework import serializers
from .models import SalesModel

class SalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = SalesModel
        fields = '__all__'
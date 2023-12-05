from rest_framework import serializers

class SeviceSerializer(serializers.Serializer):
    serviceno=serializers.IntegerField()
    servicename=serializers.CharField(max_length=64)
    servicerate=serializers.FloatField()
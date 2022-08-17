from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    """For testing serializers and understanding how they work"""
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

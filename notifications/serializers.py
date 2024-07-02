from rest_framework import serializers


class NotificationsOutputSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=500)
    is_read = serializers.BooleanField()

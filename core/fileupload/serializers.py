from datetime import datetime
from rest_framework import serializers

from .models import File


class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    uploaded_at = serializers.DateTimeField(default=datetime.now)
    processed = serializers.BooleanField(default=False)

    class Meta:
        model = File
        fields = "__all__"


class FileListSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    uploaded_at = serializers.DateTimeField(default=datetime.now)
    processed = serializers.BooleanField(default=False)

    class Meta:
        model = File
        fields = "__all__"

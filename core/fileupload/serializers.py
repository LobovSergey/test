from datetime import datetime
from rest_framework import serializers

from .models import File


class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)

    class Meta:
        model = File
        fields = "__all__"


class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import File
from .serializers import *
from rest_framework.generics import CreateAPIView, ListAPIView


class BaseView(View):

    @staticmethod
    def get(request):
        return JsonResponse({"status": "ok"}, status=200)


class FileUploadView(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileUploadSerializer


class FileListView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileListSerializer

# models.py (if needed)
from django.db import models

# No models needed for this example


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from .serializers import FileUploadSerializer

class FileUploadView(APIView):
    serializer_class = FileUploadSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            uploaded_file = serializer.validated_data['file']
            files = {"file": uploaded_file}

            response = requests.post("https://exifmeta.com/api/upload", files=files)

            if response.status_code == 200:
                response_data = response.json()
                return Response({"message": "file uploaded successfully", "data": response_data}, status=status.HTTP_200_OK)
            else:
                return Response({"message": f"Error uploading file. Status code: {response.status_code}"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



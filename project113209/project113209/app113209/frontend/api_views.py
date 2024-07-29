# app113209/frontend/api_views.py
from rest_framework import viewsets
from app113209.models import FrontendSpecificModel
from app113209.serializers import FrontendSpecificModelSerializer
from rest_framework.permissions import IsAuthenticated

class FrontendSpecificModelViewSet(viewsets.ModelViewSet):
    queryset = FrontendSpecificModel.objects.all()
    serializer_class = FrontendSpecificModelSerializer
    permission_classes = [IsAuthenticated]

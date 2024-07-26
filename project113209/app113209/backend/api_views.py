import logging
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from app113209.models import User, Module, Role, RolePermission
from app113209.serializers import UserSerializer, ModuleSerializer, RoleSerializer, RolePermissionSerializer

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'success': True, 'data': serializer.data}, status=201, headers=headers)

    def delete(self, request, pk=None):
        try:
            module = self.get_object()
            module.is_deleted = True
            module.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Module.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.filter(is_deleted=False)
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        logger.debug('創建角色請求數據: %s', request.data)
        try:
            response = super().create(request, *args, **kwargs)
            logger.debug('角色創建成功: %s', response.data)
            return response
        except Exception as e:
            logger.error('創建角色時發生錯誤: %s', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def toggle_status(self, request, pk=None):
        role = self.get_object()
        role.is_active = not role.is_active
        role.save()
        return Response({'success': True})

    @action(detail=True, methods=['post'])
    def delete(self, request, role_id=None):
        try:
            role = Role.objects.get(id=role_id)
            role.is_deleted = True
            role.save()
            return Response({'success': True})
        except Role.DoesNotExist:
            return Response({'error': 'Role not found'}, status=404)

class RoleCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            role = serializer.save()
            return Response(RoleSerializer(role).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = RolePermission.objects.filter(is_deleted=False)
    serializer_class = RolePermissionSerializer
    permission_classes = [IsAuthenticated]

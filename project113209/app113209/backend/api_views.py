import logging
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app113209.models import User, Module, Role, RolePermission
from app113209.serializers import UserSerializer, ModuleSerializer, RoleSerializer, RolePermissionSerializer

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def assign_role_and_module(self, request, pk=None):
        user = self.get_object()
        module = request.data.get('module')
        role = request.data.get('role')
        user.module_id = module
        user.role_id = role
        user.save()
        return Response({'success': True})
    
    @action(detail=False, methods=['get'])
    def get_role_users(self, request, role_id=None):
        role_id = request.query_params.get('role_id')
        users = User.objects.filter(roles__id=role_id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

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
        
    @action(detail=False, methods=['get'])
    def get_modules(self, request):
        modules = Module.objects.all()
        serializer = self.get_serializer(modules, many=True)
        return Response(serializer.data)
        
    def list(self, request, *args, **kwargs):
        modules = Module.objects.all()
        serializer = self.get_serializer(modules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
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

    @action(detail=False, methods=['get'])
    def get_roles_by_module(self, request, pk=None):
        if pk is not None:
            roles = Role.objects.filter(module_id=pk)
            serializer = self.get_serializer(roles, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def toggle_status(self, request, pk=None):
        role = self.get_object()
        role.is_active = not role.is_active
        role.save()
        return Response({'success': True})

    @action(detail=True, methods=['post'])
    def delete(self, request, pk=None):
        role = self.get_object()
        role.is_deleted = True
        role.save()
        return Response({'success': True})

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        # Add the users and module information
        data['users'] = UserSerializer(instance.users.all(), many=True).data
        data['module'] = ModuleSerializer(instance.module).data if instance.module else None
        return Response(data)

class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = RolePermission.objects.filter(is_deleted=False)
    serializer_class = RolePermissionSerializer
    permission_classes = [IsAuthenticated]

class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RolePermissionListCreateView(generics.ListCreateAPIView):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer

class RolePermissionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer

class ModuleListCreateView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ModuleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

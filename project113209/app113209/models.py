from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import pyotp

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, null=False, blank=False, default='0000000000')
    verification_code = models.CharField(max_length=6, unique=True, null=True, blank=True)
    expiry_time = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    department_id = models.CharField(max_length=50, blank=True, null=True)
    position_id = models.CharField(max_length=50, blank=True, null=True)
    branch_id = models.CharField(max_length=50, blank=True, null=True)
    module = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)  # 确保这里字段名正确
    otp_secret = models.CharField(max_length=32, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)  # Add this field for soft delete

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email

    def generate_otp_secret(self):
        if not self.otp_secret:
            self.otp_secret = pyotp.random_base32()
            self.save()

    def verify_otp(self, otp):
        totp = pyotp.TOTP(self.otp_secret)
        return totp.verify(otp)

class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_deleted = models.BooleanField(default=False)  # Add this field for soft delete

    class Meta:
        db_table = 'module'

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=20, unique=True)
    users = models.ManyToManyField(User, related_name='roles')
    is_active = models.BooleanField(default=False)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)  # Add this field for soft delete

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.name

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission_name = models.CharField(max_length=100, default=False)
    can_add = models.BooleanField(default=False)
    can_query = models.BooleanField(default=False)
    can_view = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    can_print = models.BooleanField(default=False)
    can_export = models.BooleanField(default=False)
    can_maintain = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)  # Add this field for soft delete

    class Meta:
        db_table = 'rolepermission'
        unique_together = ('role', 'permission_name')  # 添加唯一約束

    def __str__(self):
        return f"{self.role.name} - {self.permission_name}"

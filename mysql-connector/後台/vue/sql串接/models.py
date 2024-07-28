from django.db import models
from django.utils import timezone

class DjangoAdminLog(models.Model):
    user_id = models.CharField(max_length=255)
    action_flag = models.CharField(max_length=255)
    change_message = models.TextField()
    action_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'django_admin_log'

class UserActivityLogs(models.Model):
    user = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    email = models.EmailField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'user_activitylogs'


from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

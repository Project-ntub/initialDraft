from django.core.management.base import BaseCommand
from myapp.models import DjangoAdminLog, UserActivityLogs  # Ensure you have these models defined in myapp/models.py

class Command(BaseCommand):
    help = 'Delete records from django_admin_log and user_activitylogs tables for specific users'

    def handle(self, *args, **kwargs):
        users_to_delete = ['張三', '李四']  # Users to delete

        for user in users_to_delete:
            self.delete_from_django_admin_log(user)
            self.delete_from_user_activitylogs(user)

    def delete_from_django_admin_log(self, user):
        try:
            records_deleted, _ = DjangoAdminLog.objects.filter(user_id=user).delete()
            if records_deleted > 0:
                self.stdout.write(f"django_admin_log 中 user_id 為 {user} 的紀錄已刪除")
            else:
                self.stdout.write(f"django_admin_log 中 user_id 為 {user} 的紀錄不存在")
        except Exception as e:
            self.stdout.write(f"Error: {e}")

    def delete_from_user_activitylogs(self, user):
        try:
            records_deleted, _ = UserActivityLogs.objects.filter(user=user).delete()
            if records_deleted > 0:
                self.stdout.write(f"user_activitylogs 中 user 為 {user} 的紀錄已刪除")
            else:
                self.stdout.write(f"user_activitylogs 中 user 為 {user} 的紀錄不存在")
        except Exception as e:
            self.stdout.write(f"Error: {e}")

# Make sure you have defined your models correctly
# in myapp/models.py
from django.db import models

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(null=True, blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField(null=True, blank=True)
    content_type_id = models.IntegerField(null=True, blank=True)
    user_id = models.BigIntegerField()

    class Meta:
        db_table = 'django_admin_log'

    def __str__(self):
        return f"{self.id} - {self.action_time} - {self.object_repr} - {self.action_flag}"

class UserActivityLogs(models.Model):
    user = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    email = models.EmailField()
    timestamp = models.DateTimeField(default=models.timezone.now)

    class Meta:
        db_table = 'user_activitylogs'

    def __str__(self):
        return f"{self.user} - {self.activity} - {self.email} - {self.timestamp}"

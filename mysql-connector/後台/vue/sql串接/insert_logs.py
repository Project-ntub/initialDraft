from django.core.management.base import BaseCommand
from django.utils import timezone
from myapp.models import DjangoAdminLog, UserActivityLogs  # Ensure you have these models defined in myapp/models.py

class Command(BaseCommand):
    help = 'Insert logs for specific users'

    def handle(self, *args, **kwargs):
        records = [
            ('張三', '新增角色', 'zhangsan@example.com'),
            ('李四', '刪除角色', 'lisi@example.com')
        ]

        activities = [
            ('張三', '新增角色', 'zhangsan@example.com'),
            ('李四', '刪除角色', 'lisi@example.com')
        ]

        for record in records:
            self.insert_into_django_admin_log(*record)
        
        for activity in activities:
            self.insert_into_user_activitylogs(*activity)

    def insert_into_django_admin_log(self, user, action, email):
        try:
            timestamp = timezone.now()
            DjangoAdminLog.objects.create(
                user_id=user,
                content_type_id=None,
                object_id=None,
                object_repr=None,
                action_flag=action,
                change_message=email,
                action_time=timestamp
            )
            self.stdout.write("紀錄已插入到 django_admin_log")
        except Exception as e:
            self.stdout.write(f"Error: {e}")

    def insert_into_user_activitylogs(self, user, activity, email):
        try:
            timestamp = timezone.now()
            UserActivityLogs.objects.create(
                user=user,
                activity=activity,
                email=email,
                timestamp=timestamp
            )
            self.stdout.write("紀錄已插入到 user_activitylogs")
        except Exception as e:
            self.stdout.write(f"Error: {e}")

from django.core.management.base import BaseCommand
from django.utils import timezone
from myapp.models import DjangoAdminLog, UserActivityLogs  # Ensure you have these models defined in myapp/models.py

class Command(BaseCommand):
    help = 'Update logs for specific users'

    def handle(self, *args, **kwargs):
        modifications = [
            ('張三', '更新角色', 'new_zhangsan@example.com'),
            ('李四', '更新角色', 'new_lisi@example.com')
        ]

        for user, new_action, new_email in modifications:
            self.update_django_admin_log(user, new_action, new_email)
            self.update_user_activitylogs(user, new_action, new_email)

    def update_django_admin_log(self, user, new_action, new_email):
        try:
            timestamp = timezone.now()
            log = DjangoAdminLog.objects.get(user_id=user)
            log.action_flag = new_action
            log.change_message = new_email
            log.action_time = timestamp
            log.save()
            self.stdout.write(f"django_admin_log 中 user_id 為 {user} 的紀錄已修改")
        except DjangoAdminLog.DoesNotExist:
            self.stdout.write(f"django_admin_log 中 user_id 為 {user} 的紀錄不存在")

    def update_user_activitylogs(self, user, new_activity, new_email):
        try:
            timestamp = timezone.now()
            log = UserActivityLogs.objects.get(user=user)
            log.activity = new_activity
            log.email = new_email
            log.timestamp = timestamp
            log.save()
            self.stdout.write(f"user_activitylogs 中 user 為 {user} 的紀錄已修改")
        except UserActivityLogs.DoesNotExist:
            self.stdout.write(f"user_activitylogs 中 user 為 {user} 的紀錄不存在")

from django.core.management.base import BaseCommand
from myapp.models import DjangoAdminLog, UserActivityLogs  # Ensure you have these models defined in myapp/models.py

class Command(BaseCommand):
    help = 'Query records from django_admin_log and user_activitylogs tables'

    def handle(self, *args, **kwargs):
        self.query_django_admin_log()
        self.query_user_activitylogs()

    def query_django_admin_log(self):
        try:
            records = DjangoAdminLog.objects.all()
            self.stdout.write("django_admin_log 紀錄:")
            for record in records:
                self.stdout.write(str(record))
        except Exception as e:
            self.stdout.write(f"Error: {e}")

    def query_user_activitylogs(self):
        try:
            records = UserActivityLogs.objects.all()
            self.stdout.write("user_activitylogs 紀錄:")
            for record in records:
                self.stdout.write(str(record))
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

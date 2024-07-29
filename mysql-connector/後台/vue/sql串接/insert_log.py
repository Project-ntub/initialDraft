from django.core.management.base import BaseCommand
from django.db import connections, OperationalError
from django.utils import timezone
from myapp.models import DjangoAdminLog  # Ensure you have this model defined in myapp/models.py

class Command(BaseCommand):
    help = 'Insert a record into the django_admin_log table'

    def handle(self, *args, **kwargs):
        try:
            with connections['default'].cursor() as cursor:
                # SQL statement to create the django_admin_log table
                create_table_query = '''
                CREATE TABLE IF NOT EXISTS django_admin_log (
                    id INT NOT NULL AUTO_INCREMENT,
                    action_time DATETIME(6) NOT NULL,
                    object_id LONGTEXT,
                    object_repr VARCHAR(200) NOT NULL,
                    action_flag SMALLINT UNSIGNED NOT NULL,
                    change_message LONGTEXT,
                    content_type_id INT,
                    user_id BIGINT,
                    PRIMARY KEY (id)
                ) ENGINE=InnoDB;
                '''

                cursor.execute(create_table_query)
                self.stdout.write(self.style.SUCCESS("Table 'django_admin_log' created successfully."))

                # SQL statement to insert a row into the django_admin_log table
                insert_data_query = '''
                INSERT INTO django_admin_log (action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
                '''

                # Example data to insert
                data = (
                    timezone.now(),       # action_time
                    '12345',              # object_id
                    'Example Object',     # object_repr
                    1,                    # action_flag
                    'Initial creation',   # change_message
                    1,                    # content_type_id
                    31                    # user_id
                )

                cursor.execute(insert_data_query, data)
                self.stdout.write(self.style.SUCCESS("Data inserted successfully."))

        except OperationalError as err:
            self.stdout.write(self.style.ERROR(f"OperationalError: {err}"))

        except Exception as err:
            self.stdout.write(self.style.ERROR(f"Error: {err}"))

# Make sure you have defined your model correctly
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

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import User  # 確保這裡的 app 名稱正確

class Command(BaseCommand):
    help = 'Insert user records into the user table'

    def handle(self, *args, **kwargs):
        users = [
            {
                'username': 'user1',
                'email': 'user1@example.com',
                'phone': '1234567890',
                'verification_code': '123456',
                'is_verified': True,
                'is_approved': True,
                'department_id': 'dept01',
                'position_id': 'pos01',
                'branch_id': 'branch01',
                'gender': 'Male',
                'is_staff': True,
                'is_active': True,
                'otp_secret': 'otpsecret',
                'font_size': 'medium',
                'notifications_enabled': True,
                'auto_login_enabled': False,
                'authentication_enabled': True,
                'module_id': 1
            },
            # 可以添加更多的用戶
        ]

        for user_data in users:
            self.insert_user(**user_data)

    def insert_user(self, **kwargs):
        try:
            User.objects.create(**kwargs)
            self.stdout.write(f"User {kwargs['username']} 已插入到 user 表中")
        except Exception as e:
            self.stdout.write(f"Error: {e}")

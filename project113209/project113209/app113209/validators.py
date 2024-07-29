import re
from django.core.exceptions import ValidationError

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError("密碼長度必須至少為8個字。")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("密碼必須包含至少一個大寫字母。")
        if not re.search(r'[a-z]', password):
            raise ValidationError("密碼必須包含至少一個小寫字母")
        if not re.search(r'\d', password):
            raise ValidationError("密碼必須包含至少一個數字。")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("密碼必須包含至少一個特殊字元。")

    def get_help_text(self):
        return "您的密碼長度必須至少為8個字。，並且包含至少一個大寫字母、一個小寫字母、一個數字和一个特殊字元。"

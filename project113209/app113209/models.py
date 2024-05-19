from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    modifyPassword = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    departmentID = models.IntegerField(default=1)  # 添加默認值
    positionID = models.CharField(max_length=50)
    branchID = models.IntegerField(default=1)  # 添加默認值
    module = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    class Meta:
        db_table = 'users'  # 指定資料表名稱

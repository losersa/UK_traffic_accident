from django.db import models

# Create your models here.

class Users(models.Model):

    user_name = models.CharField("用户账号", max_length=32)
    user_email = models.CharField("用户邮箱", max_length=32)
    user_password = models.CharField("用户密码", max_length=32)

    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.user_name


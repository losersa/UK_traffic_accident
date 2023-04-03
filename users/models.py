from django.db import models
from django.utils.translation import gettext_lazy, gettext as _


# Create your models here.

class Users(models.Model):
    user_name = models.CharField("用户账号", max_length=32)
    user_email = models.CharField("用户邮箱", max_length=32, unique=True)
    user_password = models.CharField("用户密码", max_length=32)
    user_location = models.CharField("用户地址", max_length=64, null=True)
    preferences_language = models.CharField("用户偏好语言", max_length=32, default="中文")
    time_zone = models.CharField("时区", max_length=32, default="东八区（UTC+8）")
    currency = models.CharField("货币", max_length=32, default="CNY ¥ ")
    email_subscription = models.CharField("电子邮箱订阅", max_length=10, default="Off")
    sms_notifications = models.CharField("短讯通知", max_length=10, default="On")
    credit = models.CharField("信用卡/银行卡", max_length=32, null=True)
    paypal = models.CharField("第三方支付", max_length=32, null=True)

    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.user_name


# class translate(models.Model):
#     name = models.CharField(max_length=50, help_text=_('This is the help text'))
#     langue = models.CharField(max_length=50, help_text=_('This is the help text'))
#
#     class Meta:
#         verbose_name = 'Translate'
#         db_table = 'translate'

from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, verbose_name="用户名")
    password = models.CharField(max_length=120, verbose_name="密码")
    gender = models.BooleanField(default=False, verbose_name='性别')
    age = models.IntegerField(default=18, verbose_name='年龄')
    # null=True：生成数据表时，数据表的对应字段允许为NULL
    mobile = models.CharField(max_length=11, null=True, verbose_name='手机号')

    class Meta:
        db_table = "tb_users"
        verbose_name = "用户表"

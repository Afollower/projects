from django.db import models

# Create your models here.

class User(models.Model):
    # 用户表
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(verbose_name="用户名", max_length=128, unique=True)  # unique表示唯一
    password = models.CharField(verbose_name="密码", max_length=256)
    email = models.EmailField(verbose_name="邮箱", unique=True)
    sex = models.CharField(verbose_name="性别", max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'



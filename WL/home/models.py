from django.db import models

# Create your models here.

class exam_entry_table(models.Model):
    #考点信息表
    exam_id = models.CharField(verbose_name="考试编号",max_length=10)
    exam_type = models.CharField(verbose_name="考试类别",max_length=128)
    exam_point = models.CharField(verbose_name="考点",max_length=128)
    exam_time = models.CharField(verbose_name="考试时间",max_length=128)
    number = models.IntegerField(verbose_name="容量")
    entry_number = models.IntegerField(verbose_name="已报名数量",default=0)

    def __str__(self):
        return self.exam_point

    class Meta:
        # ordering = ['c_time']
        verbose_name = '考点'
        verbose_name_plural = '考点信息表'



class user_entry_table(models.Model):
    #用户考试信息表
    email = models.EmailField(verbose_name="邮箱")
    exam_id = models.CharField(verbose_name="考试编号",max_length=10)
    exam_point = models.CharField(verbose_name="考点",max_length=128)


    def __str__(self):
        return self.email
    class Meta:
        # ordering = ['c_time']
        verbose_name = '用户考试信息'
        verbose_name_plural = '用户考试信息表'

class user_data(models.Model):
    #用户信息表
    user_name = models.CharField(verbose_name="用户名",max_length=128, unique=True)
    user_true_name = models.CharField(verbose_name="真实姓名",max_length=128, null=True)
    user_id = models.CharField(verbose_name="身份证号",max_length=18, null=True)
    # user_img =
    user_school = models.CharField(verbose_name="在读学校",max_length=128)
    user_f_score = models.IntegerField(verbose_name="四级成绩", default=0)
    user_s_score = models.IntegerField(verbose_name="六级成绩", default=0)

    def __str__(self):
        return self.user_name

    class Meta:
        # ordering = ['c_time']
        verbose_name = '用户名'
        verbose_name_plural = '用户信息表'



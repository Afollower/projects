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


class Order(models.Model):
    # 订单表
    order_id = models.CharField(verbose_name="订单编号", max_length=50, primary_key=True)
    order_kind = models.CharField(verbose_name="订单类别", max_length=32, blank=True, null=True)
    weight = models.FloatField(verbose_name="重量", blank=True, null=True)
    order_status = models.CharField(verbose_name="订单状态", max_length=20, blank=True, null=True)
    order_loc = models.CharField(verbose_name="订单地址", max_length=255, blank=True, null=True)

    # 寄件人信息
    sender_name = models.CharField(verbose_name="寄件人姓名", max_length=255, blank=True, null=True)
    sender_id = models.CharField(verbose_name="寄件人身份证", max_length=20, null=True)
    sender_phone = models.CharField(verbose_name="寄件人电话", max_length=20, null=True)
    sender_loc = models.CharField(verbose_name="寄件人地址", max_length=255, blank=True, null=True)

    # 收件人信息
    recipient_name = models.CharField(verbose_name="收件人姓名", max_length=255, blank=True, null=True)
    recipient_id = models.CharField(verbose_name="收件人身份证", max_length=20, null=True)
    recipient_phone = models.CharField(verbose_name="收件人电话", max_length=20, null=True)
    recipient_loc = models.CharField(verbose_name="收件人地址", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.order_id

    class Meta:
        # managed = False
        verbose_name = '订单'
        db_table = 'order'


class Staff(models.Model):
    # 职工表 用电话和密码登录
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    is_pass = (
        ('pass', '通过'),
        ('not_pass', '未通过'),
    )
    staff_id = models.CharField(verbose_name="职工编号", max_length=20, primary_key=True)
    staff_department = models.CharField(verbose_name="部门", max_length=32, blank=True, null=True)
    work_loc = models.CharField(verbose_name="工作地点", max_length=255, blank=True, null=True)

    staff_name = models.CharField(verbose_name="姓名", max_length=32, blank=True, null=True)
    sex = models.CharField(verbose_name="性别", max_length=32, choices=gender, default='男')
    staff_phone = models.CharField(verbose_name="电话", max_length=20, blank=True, null=True)
    staff_loc = models.CharField(verbose_name="地址", max_length=128, blank=True, null=True)
    staff_password = models.CharField(verbose_name="密码", max_length=32, blank=True, null=True)
    staff_pass = models.CharField(verbose_name="审批结果", max_length=20, choices=is_pass, default='未通过')

    class Meta:
        # managed = False
        verbose_name = '职工'
        db_table = 'staff'


class Trsptool(models.Model):
    tool_id = models.IntegerField(verbose_name="工具编号", primary_key=True)
    tool_name = models.CharField(verbose_name="名称", max_length=32, blank=True, null=True)
    tool_phone = models.CharField(verbose_name="负责人电话", max_length=20, blank=True, null=True)
    tool_license = models.CharField(verbose_name="许可证", max_length=128, blank=True, null=True)
    staff = models.ForeignKey(Staff, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        verbose_name = '工具'
        db_table = 'trsptool'


class Warehouse(models.Model):
    warehouse_id = models.IntegerField(verbose_name="仓库编号", primary_key=True)
    warehouse_loc = models.CharField(verbose_name="位置", max_length=255, blank=True, null=True)
    warehouse_phone = models.CharField(verbose_name="联系电话", max_length=20, blank=True, null=True)
    staff = models.ForeignKey(Staff, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        verbose_name = '仓库'
        db_table = 'warehouse'
from django import forms
import re
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    # department = (
    #     ('1', "人事管理部门"),
    #     ('2', "基础部门"),
    #     ('3', "仓库部门"),
    #     ('4', "运输部门")
    # )
    # 手机号码
    staff_id = forms.CharField(label="职工编号", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    staff_department = forms.CharField(label="部门", max_length=32,
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    work_loc = forms.CharField(label="工作地点", max_length=255,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    name = forms.CharField(label="姓名", max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    username = forms.CharField(label="电话号码", max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    staff_loc = forms.CharField(label="地址", max_length=128,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=32,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=32,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class OrderForm(forms.Form):

    order_id = forms.CharField(label="订单编号", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    order_kind = forms.CharField(label="订单类别", max_length=32,
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    weight = forms.FloatField(label="重量", widget=forms.TextInput(attrs={'class': 'form-control'}))

    order_status = forms.CharField(label="订单状态", max_length=20,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    order_loc = forms.CharField(label='订单地址', max_length=255,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    # 寄件人信息
    sender_name = forms.CharField(label="寄件人姓名", max_length=255,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    sender_id = forms.CharField(label="寄件人身份证", max_length=20,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    sender_phone = forms.CharField(label="寄件人电话", max_length=20,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    sender_loc = forms.CharField(label="寄件人地址", max_length=255,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    # 收件人信息
    recipient_name = forms.CharField(label="收件人姓名", max_length=255,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    recipient_phone = forms.CharField(label="收件人电话", max_length=20,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    recipient_loc = forms.CharField(label="收件人地址", max_length=255,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_sender_id(self):
        sender_id = self.cleaned_data['sender_id']
        sender_id_regex = r'^\d{17}\d|x$'
        ir = re.compile(sender_id_regex)
        if ir.match(sender_id):
            return sender_id
        else:
            raise forms.ValidationError('身份证输入非法', code='invalid sender_id')

    def clean_sender_phone(self):
        sender_phone = self.cleaned_data['sender_phone']
        sender_phone_regex = r'^1[34578]\d{9}$'
        spr = re.compile(sender_phone_regex)
        if spr.match(sender_phone):
            return sender_phone
        else:
            raise forms.ValidationError('电话号码输入非法', code='invalid sender phone number')

    def clean_recipient_phone(self):
        recipient_phone = self.cleaned_data['recipient_phone']
        recipient_phone_regex = r'^1[34578]\d{9}$'
        rpr = re.compile(recipient_phone_regex)
        if rpr.match(recipient_phone):
            return recipient_phone
        else:
            raise forms.ValidationError('电话号码输入非法', code='invalid recipient phone number')

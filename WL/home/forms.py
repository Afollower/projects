from django import forms
from captcha.fields import CaptchaField


class user_entry(forms.Form):
    user_name = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_true_name = forms.CharField(label="真实姓名", max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_id = forms.CharField(label="身份证号", max_length=18, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    exam_point = forms.CharField(label="考点", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))

class user_datas(forms.Form):
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_true_name = forms.CharField(label="真实姓名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_id = forms.CharField(label="身份证号", max_length=18, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # user_img =
    user_school = forms.CharField(label="所在学校", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # user_f_score = forms.CharField(label="四级成绩", max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # user_s_score = forms.CharField(label="六级成绩", max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))

from django.shortcuts import render, redirect
from . import models
from .forms import UserForm, RegisterForm, OrderForm
# Create your views here.


def check(request):
    pass
    return render(request, 'login/hello.html')


def index(request):
    pass
    return render(request, 'login/index.html')


def order_get(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        message = "请检查填写的内容！"
        if order_form.is_valid():
            order_kind = order_form.cleaned_data['o']

        return render(request, 'login/order_get.html', locals())

    order_form = OrderForm()
    return render(request, 'login/order_get.html', locals())


# 加入session
def login(request):
    # 不允许重复登录
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.Staff.objects.get(staff_phone=username)
                if user.staff_pass == 'pass':
                    if user.staff_password == password:
                        # 往session字典内写入用户状态和数据
                        request.session['is_login'] = True
                        request.session['user_id'] = user.staff_id
                        request.session['user_name'] = user.staff_name
                        return redirect('/index/')
                    else:
                        message = "密码不正确！"
                else:
                    message = "请联系管理员审批通过！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            staff_id = register_form.cleaned_data['staff_id']
            staff_department = register_form.cleaned_data['staff_department']
            work_loc = register_form.cleaned_data['work_loc']

            name = register_form.cleaned_data['name']
            sex = register_form.cleaned_data['sex']
            username = register_form.cleaned_data['username']
            staff_loc = register_form.cleaned_data['staff_loc']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']

            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_staff_id = models.Staff.objects.filter(staff_id=staff_id)
                if same_staff_id:  # 员工编号唯一
                    message = '员工编号已经注册，请重新确认！'
                    return render(request, 'login/register.html', locals())
                same_username = models.Staff.objects.filter(staff_phone=username)
                if same_username:  # 电话唯一
                    message = '该电话已被注册，请确认是否重复注册或联系管理员！'
                    return render(request, 'login/register.html', locals())
                message = "注册成功！"
                # 当一切都OK的情况下，创建新用户
                # 创建员工表
                new_staff = models.Staff.objects.create()
                new_staff.staff_id = staff_id                       # id
                new_staff.staff_department = staff_department       # 部门
                new_staff.work_loc = work_loc                       # 工作地点

                new_staff.staff_name = name                         # 姓名
                new_staff.sex = sex                                 # 性别
                new_staff.staff_phone = username                    # 电话
                new_staff.staff_loc = staff_loc                     # 地址
                new_staff.staff_password = password1                # 登录密码
                new_staff.staff_pass = 'not_pass'                   # 账号审核
                new_staff.save()

                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())
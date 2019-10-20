from django.shortcuts import render, redirect
from . import models
from .forms import user_entry, user_datas
from django.http import HttpResponse,HttpResponseRedirect
# from django.contrib.auth.models import User
from login.models import User

# Create your views here.

def test(request):
    pass
    return render(request, 'home/test.html')

# 我的信息
def mydate(request):
    username = request.session.get('user_name', None)
    account = User.objects.get(name=username)           # 用户登录注册表
    user = models.user_data.objects.get(user_name= username)
    return  render(request,"home/myself.html",{"user":user, "account":account})


# 修改我的信息
def updata(request):
    username = request.session.get('user_name', None)
    # print("-----------------------")
    # print(username)
    # print("-----------------------")
    user_da = models.user_data.objects.get(user_name=username)
    user = User.objects.get(name=username)  # login_user表
    if request.method == "POST":
        userdata = user_datas(request.POST)
        # print(userdata)
        if userdata.is_valid():
            user_das = userdata.cleaned_data
            # user.user_name = user_da['user_name'] #用户无法修改用户名
            user.email = user_das['email']
            user_da.user_true_name = user_das['user_true_name']
            user_da.user_id = user_das['user_id']
            user_da.user_school = user_das['user_school']
            user_da.save()
            user.save()
            # 四六级成绩无法修改
            # user_datas.user_f_score = user_da['user_f_score']
            # user_datas.user_s_score = user_da['user_s_score']
            return redirect('/homepage/my_data/')
    else:
        userdata = user_datas(initial={"email": user.email, "user_name": user_da.user_name, "user_true_name": user_da.user_true_name,
                                       "user_id": user_da.user_id, "user_school": user_da.user_school})
        return render(request, 'home/change_mydata.html', {"userdata": userdata})


# 查询考试信息 还没完成，优化，条件判断
def query(request):
    username = request.session.get('user_name',None)
    user = User.objects.get(name=username)
    # 用于判断用户是否报名
    user_en = models.user_entry_table.objects.filter(email=user.email)
    # print("********************")
    # print(user_en)
    # print(user_en[0])
    if user_en:
        # print(len(user_en))
        if len(user_en)==1:
            user_entry = models.user_entry_table.objects.get(email=user.email)
            user_point = user_entry.exam_point
            user_eid = user_entry.exam_id
            exam_entry = models.exam_entry_table.objects.get(exam_point=user_point, exam_id=user_eid)
            return render(request, 'home/query1.html', {"exam_entry": exam_entry})
        else:
            user_entry4 = models.user_entry_table.objects.get(email=user.email, exam_id=0)
            user_entry6 = models.user_entry_table.objects.get(email=user.email, exam_id=1)
            user_point4 = user_entry4.exam_point
            user_point6 = user_entry6.exam_point
            exam_entry4 = models.exam_entry_table.objects.get(exam_point=user_point4, exam_id=0)
            exam_entry6 = models.exam_entry_table.objects.get(exam_point=user_point6, exam_id=1)
            return render(request, 'home/query2.html', {"exam_entry4": exam_entry4, "exam_entry6":exam_entry6})
    else:
        # message = "你还未报名！请先报名之后再来查看！"
        # return render(request, 'login/index.html', locals())
        user_da = models.user_data.objects.get(user_name=user.name)
        school = user_da.user_school
        if school=='无':
            message = "请先更新你的学校信息！"
            return render(request, 'login/index.html', locals())
        else:
            point = models.exam_entry_table.objects.filter(exam_point=school)
            if point:
                if len(point)==1:
                    exam = models.exam_entry_table.objects.get(exam_point=school)
                    return render(request, 'home/exam1.html', {"exam": exam})
                else:
                    exam4 = models.exam_entry_table.objects.get(exam_point=school, exam_id=0)
                    exam6 = models.exam_entry_table.objects.get(exam_point=school, exam_id=1)
                    return render(request, 'home/exam2.html', {"exam4": exam4, "exam6": exam6})
            else:
                message="你的学校还未开放报名！详情请咨询学校相关部门！"
                return render(request, 'login/index.html', locals())


# 四级报名
def cet_4(request):
    username = request.session.get('user_name', None)
    # 用户信息表,用户表，获取信息判断资格
    user_da = models.user_data.objects.get(user_name=username)
    user = User.objects.get(name=username)
    if request.method == "POST":
        cet4_form = user_entry(request.POST)
        if cet4_form.is_valid():
            # 四级考试对分数无要求
            # 只需要获取报考考点信息即可
            # email = cet4_form.cleaned_data['email']
            exam_id = '0'
            exam_point = cet4_form.cleaned_data['exam_point']
            #用与下面的考点判断
            point = models.exam_entry_table.objects.filter(exam_point=exam_point, exam_id='0')
            # 用与下面的是否重复报名判断
            entryer = models.user_entry_table.objects.filter(email=user.email, exam_id=exam_id)
            #判断个人信息是否完善
            if user_da.user_true_name=='无'or user_da.user_id=='无':
                message="请先完善个人真实信息之后再来报名！"
                return render(request, 'home/cet_4.html', locals())
            # 判断是否重复报名
            # print("判断是否重复报名")
            elif entryer:
                message = "请勿重复报名！"
                return render(request, 'home/cet_4.html', locals())
            elif point:
                # 考点存在
                # print("没有重复报名")
                message = "报名成功！请按时参加考试！"
                # 创建一条数据
                new_user = models.user_entry_table.objects.create()
                new_user.email = user.email
                new_user.exam_id = exam_id
                new_user.exam_point = exam_point
                new_user.save()
                # 考点容量减1,报考人数加1
                exam_entry = models.exam_entry_table.objects.get(exam_point=exam_point, exam_id=exam_id)
                exam_entry.number -= 1
                exam_entry.entry_number += 1
                exam_entry.save()
                return render(request, 'home/cet_4.html', locals())
            else:
                message = "该学校还未开放报名！详情请咨询学校相关部门！"
                return render(request, 'home/cet_4.html', locals())
    cet4_form = user_entry(initial={"email": user.email, "user_name": user_da.user_name, "user_true_name": user_da.user_true_name,
                  "user_id": user_da.user_id})
    return render(request, 'home/cet_4.html', locals())


# 六级报名：
def cet_6(request):
    username = request.session.get('user_name', None)
    # 用户信息表,用户表，获取信息判断资格
    user_da = models.user_data.objects.get(user_name=username)
    user = User.objects.get(name=username)
    if request.method == "POST":
        cet6_form = user_entry(request.POST)
        if cet6_form.is_valid():
            # 只需要获取报考考点信息即可
            # email = cet4_form.cleaned_data['email']
            exam_id = '1'
            exam_point = cet6_form.cleaned_data['exam_point']
            f_score = user_da.user_f_score
            # 用与下面的考点判断
            point = models.exam_entry_table.objects.filter(exam_point=exam_point, exam_id=exam_id)
            # 用与下面的是否重复报名判断
            entryer = models.user_entry_table.objects.filter(email=user.email, exam_id=exam_id)
            # 判断个人信息是否完善
            if user_da.user_true_name=='无'or user_da.user_id=='无':
                message="请先完善个人真实信息之后再来报名！"
                return render(request, 'home/cet_6.html', locals())
                # 判断是否重复报名
            elif entryer:
                # print("判断是否重复报名")
                message = "请勿重复报名！"
                return render(request, 'home/cet_6.html', locals())
            # 判断考点是否存在
            elif point:
                # 考点存在
                #判断四级成绩是否合格
                if f_score >= 425:
                    # print("报名成功！请按时参加考试！")
                    # 创建一条数据
                    message = "报名成功！请按时参加考试！"
                    new_user = models.user_entry_table.objects.create()
                    new_user.email = user.email
                    new_user.exam_id = exam_id
                    new_user.exam_point = exam_point
                    new_user.save()
                    # 考点容量减1,报考人数加1
                    exam_entry = models.exam_entry_table.objects.get(exam_point=exam_point, exam_id=exam_id)
                    exam_entry.number -= 1
                    exam_entry.entry_number += 1
                    exam_entry.save()
                    return render(request, 'home/cet_6.html', locals())
                else:
                    message = "四级成绩大于425才能报名六级考试！"
                    return render(request, 'home/cet_6.html', locals())
            else:
                message = "该学校还未开放报名！详情请咨询学校相关部门！"
                return render(request, 'home/cet_6.html', locals())

    cet6_form = user_entry(
        initial={"email": user.email, "user_name": user_da.user_name, "user_true_name": user_da.user_true_name,
                 "user_id": user_da.user_id})
    return render(request, 'home/cet_6.html', locals())
import json

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader, Template, Context
from django.utils.translation import gettext_lazy, gettext
from django.utils.translation import gettext as _
from django.views import View

from .models import Users
from django.conf import settings

# res = Users.objects.all().values('id', 'user_name', 'user_email', 'user_password')

# def index(request):
#     latest_user_list = Users.objects.order_by('-user_name')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_user_list': latest_user_list,
#     }
#     return HttpResponse(template.render(context, request))


# def index(request):
#     latest_user_list = Users.objects.order_by('-user_name')[:5]
#     context = {'latest_user_list': latest_user_list}
#     return render(request, 'polls/index.html', context)
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# def index(request):
#     latest_users_list = Users.objects.order_by('-user_name')[:5]
#     output = ', '.join([q.question_text for q in latest_users_list])
#     return HttpResponse(output)


def error_404(request):
    return render(request, "traffic/404.html")




class account(View):

    def get(self, request):
        return render(request, "traffic/account.html")

    def post(self, request):
        # res = Users.objects.all().values('id', 'user_name', 'user_email', 'user_password')
        context = {}
        # # if res.first().user_email == email:
        # name = res.first().get('user_name')
        # user_email = res.first().get('user_email')
        # user_password = res.first().get('user_password')
        user_email = request.session['email']

        res = Users.objects.filter(user_email=user_email)
        user_name = res.first().user_name
        user_password = res.first().user_password

        context["name"] = user_name
        context["email"] = user_email
        context["password"] = user_password
        context["location"] = res.first().user_location
        context["language"] = res.first().preferences_language
        context["time_zone"] = res.first().time_zone
        context["currency"] = res.first().currency
        context["email_subscription"] = res.first().email_subscription
        context["sms_notifications"] = res.first().sms_notifications
        context["credit "] = res.first().credit
        context["paypal"] = res.first().paypal

        return render(request, "traffic/account.html", context)

def charts(request):
    return render(request, "traffic/charts.html")


def docs(request):
    context = {}
    return render(request, "traffic/docs.html", context)


def help(request):
    return render(request, "traffic/help.html")

def global_setting(request):
    """
    settings中全局变量
    ：param request:
    :return:
    """
    return {
        "LANGUAGE": settings.LANGUAGE_CODE,
    }

def index(request):
    context = {}
    # request.session['language'] = 'en'

    return render(request, "traffic/index.html", context)


class login(View):

    def get(self, request):
        return render(request, "traffic/login.html")

    def post(self, request):
        email = request.POST.get("signin-email")
        password = request.POST.get("signin-password")
        context = {}

        res = Users.objects.filter(user_email=email)  # 筛选数据库里是否存在登录的邮箱号

        if res.first() != None:
            # user_name = res.first().user_name
            user_email = res.first().user_email
            user_password = res.first().user_password
            if user_email == email and user_password == password:
                context["login"] = "登录成功"
                request.session['email'] = user_email
                request.session['_language'] = 'zh-hans'
            else:
                context["login"] = "邮箱或密码输入错误"
        else:
            context["login"] = "该邮箱还未注册账号"

        return render(request, "traffic/login.html", context)


def notifications(request):
    return render(request, "traffic/notifications.html")


def orders(request):
    return render(request, "traffic/orders.html")


def reset_password(request):
    return render(request, "traffic/reset-password.html")


def settings(request):
    return render(request, "traffic/settings.html")


class signup(View):
    def get(self, request):
        render(request, "traffic/signup.html")

    def post(self, request):
        name = request.POST.get("signup-name")
        email = request.POST.get("signup-email")
        password = request.POST.get("signup-password")
        confirm_password = request.POST.get("confirm-password")

        # print(name, email, password)
        context = {}

        if confirm_password != password:
            # context["confirm_password"] = "两次输入密码不一致"
            context["confirm_password"] = _("The password is entered twice inconsistently")
        elif name != None and email != None and password != None:
            res = Users.objects.filter(user_email=email)
            if res.first() == None:
                Users.objects.create(user_name=name, user_email=email, user_password=password)
            else:
                # context["email_already_exists"] = "邮箱已存在！请尝试登录"
                context["email_already_exists"] = _("Email already exists! Try signing in")

        return render(request, "traffic/signup.html", context)




def translate(request):
    # if user.is_active:
        # _("已激活") 标示对该字符串进行国际化翻译, 如果是前后端分离,使用 gettext_lazy() 进行国际化翻译以后, 就可以转换成json数据向前台返回了
    context = {"text": _("已激活")}


    # 进行模板渲染,响应用户请求.如果前后分离,可以直接返回json数据给前端,由前端在js中进行国际化
    return render(request, "traffic/index.html", context)

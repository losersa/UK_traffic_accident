import json

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader,Template,Context

from .models import Users

def index(request):
    latest_user_list = Users.objects.order_by('-user_name')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_user_list': latest_user_list,
    }
    return HttpResponse(template.render(context, request))

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

def account(request):
    return render(request, "traffic/account.html")

def charts(request):
    return render(request, "traffic/charts.html")

def docs(request):
    return render(request, "traffic/docs.html")

def help(request):
    return render(request, "traffic/help.html")

def index(request):
    context = {}
    context["hello"] = "你好,模板"
    return render(request, "traffic/index.html", context)

def login(request):


    res = Users.objects.all().values('id', 'user_name')

    return render(request, "traffic/login.html")

def notifications(request):
    return render(request, "traffic/notifications.html")

def orders(request):
    return render(request, "traffic/orders.html")

def reset_password(request):
    return render(request, "traffic/reset-password.html")

def settings(request):
    return render(request, "traffic/settings.html")

def signup(request):

    name = request.POST.get("signup-name")
    email = request.POST.get("signup-email")
    password = request.POST.get("signup-password")
    confirm_password = request.POST.get("confirm-password")

    # print(name, email, password)
    context = {}

    if confirm_password != password:
        context["confirm_password"] = "两次输入密码不一致"

    if name!=None and email!=None and password!=None:
        res = Users.objects.filter(user_email=email)
        if res.first() == None:
            Users.objects.create(user_name=name, user_email=email, user_password=password)
        else:
            context["email_already_exists"] = "邮箱已存在！请尝试登录"

    return render(request, "traffic/signup.html", context)




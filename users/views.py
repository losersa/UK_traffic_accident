import json
import os
import random


import urlquote as urlquote
from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
# Create your views here.
from django.template import loader, Template, Context
from django.utils.translation import gettext_lazy, gettext
from django.utils.translation import gettext as _
from django.views import View

from .forms import FileForm
from .models import Users, FileModel
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



# class docs(View):
#     def get(self, request):
#         return render(request, "traffic/docs.html")
#     def post(self, request):
#
#         file = request.FILES.get("file")
#         print(f"文件上传的文件名为：{file.name}，文件大小为：{file.file}")
#         # 判断是否有重命名情况
#         if file.name in os.listdir(settings.MEDIA_ROOT):
#             filename = os.path.join(settings.MEDIA_ROOT,
#                                     str(random.randint(0, 100) * random.randint(0, 100) - random.randint(0,
#                                                                                                          5)) + file.name)
#         else:
#             filename = os.path.join(settings.MEDIA_ROOT, file.name)
#         print(f"文件所在地址为：{filename}")
#         with open(filename, 'wb') as f:
#             f.write(file.file.read())
#         # return HttpResponse("文件上传成功！")
#
#
#         context = {
#             'status': 'Success'
#         }
#         return render(request, "traffic/docs.html", context)


# 自动保存文件的方法
def save_file(file):
    destination = open(os.path.join("./media", file.name), 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()


def upload(request):
    """
    上传文件
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # 选择的文件
            files = request.FILES.getlist('file')

            # 遍历写入到数据库中
            for file in files:
                # 写入到数据库中
                file_model = FileModel(file_name=file.name, file_path=os.path.join('./media', file.name), file_size=file.size, file_type=file.content_type)
                file_model.save()

                # 写入到服务器本地
                save_file(file)

            # 提示上传成功
            return HttpResponse('上传成功!')
    else:
        form = FileForm()
        return render(request, 'traffic/docs.html', locals())




class docs(View):

    """
    上传文件
    :param request:
    :return:
    """
    def get(self, request):
        form = FileForm()
        return render(request, 'traffic/docs.html', locals())
    def post(self, request):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # 选择的文件
            files = request.FILES.getlist('file')

            # 遍历写入到数据库中
            for file in files:
                # 写入到数据库中
                file_model = FileModel(file_name=file.name, file_path=os.path.join('./media', file.name), file_size=file.size, file_type=file.content_type)
                file_model.save()

                # 写入到服务器本地
                save_file(file)

            # 提示上传成功
            return render(request, "traffic/docs.html", {'form': form})
        else:
            return HttpResponse("error!")


def attachment_upload(request):
    att_file = request.FILES.get('attachment', None)
    doc_uuid = request.POST.get('doc_uuid', None)
    if att_file:
        # 保存文件到硬盘中
        file_dir = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'upload_files'), att_file.name)
        f = open(file_dir, 'wb')
        for i in att_file.chunks():
            f.write(i)
        f.close()
        # 下载和预览的url
        url = settings.MEDIA_URL + att_file.name
        import re
        file_type = re.search(r'[^.]+\w$', att_file.name).group() # 提前文件后缀名　　　　 # 文件类型，可自行增删
        img_list = ['jpg', 'jpeg', 'jpe', 'gif', 'png', 'pns', 'bmp', 'png', 'tif']
        pdf_list = ['pdf']
        text_list = ['txt', 'md', 'csv', 'nfo', 'ini', 'json', 'php', 'js', 'css']

        # bootstrap fileinput 上传文件的回显参数，initialPreview（列表），initialPreviewConfig（列表）
        initialPreview = [] # 根据上传的文件类型，生成不同的HTML，
        if file_type in img_list:
            initialPreview.append("<img src='" + url + "' class='file-preview-image' style='max-width:100%;max-height:100%;'>")
        elif file_type in pdf_list:
            initialPreview.append("<div class='file-preview-frame'><div class='kv-file-content'><embed class='kv-preview-data file-preview-pdf' src='" + url +
                                  "' type='application/pdf' style='width:100%;height:160px;'></div></div>")
        elif file_type in text_list:
            initialPreview.append("<div class='file-preview-frame'><div class='kv-file-content'><textarea class='kv-preview-data file-preview-text' title='" + att_file.name +
                                  "' readonly style='width:213px;height:160px;'></textarea></div></div>")
        else:
            initialPreview.append("<div class='file-preview-other'><span class='file-other-icon'><i class='glyphicon glyphicon-file'></i></span></div>")

        initialPreviewConfig = [{
            'caption': att_file.name, # 文件标题
            'type': file_type, # 文件类型
            'downloadUrl': url, # 下载地址
            'url': '/del_doc_file/', # 预览中的删除按钮的url
            'size': os.path.getsize(file_dir), # 文件大小
            'extra': {'doc_uuid': doc_uuid}, # 删除文件携带的参数
            'key': att_file.name, # 删除时ajax携带的参数
        }] # 返回json数据，initialPreview initialPreviewConfig 会替换初始化插件时的这两个参数 append:True 将内容添加到初始化预览
        return HttpResponse(json.dumps({'initialPreview':initialPreview, 'initialPreviewConfig':initialPreviewConfig,'append': True}))
    else:
        return HttpResponse(json.dumps({'status': False}))










def download_view(request, id):
    """
    下载文件
    :param request:
    :param id:文件id
    :return:
    """
    file_result = FileModel.objects.filter(id=id)

    # 如果文件存在，就下载文件
    if file_result:

        file = list(file_result)[0]

        # 文件名称及路径
        name = file.name
        path = file.path

        # 读取文件
        file = open(path, 'rb')
        response = FileResponse(file)

        # 使用urlquote对文件名称进行编码
        response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(name)

        return response
    else:
        return HttpResponse('文件不存在!')




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
                return render(request, "traffic/index.html", context)
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
        return render(request, "traffic/signup.html")

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
                return render(request, "traffic/index.html", context)
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

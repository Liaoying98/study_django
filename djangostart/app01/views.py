from django.shortcuts import render, HttpResponse

# Create your views here.


def demo(request):
    # 字符串转为http响应，需导包HttpResponse
    return HttpResponse("HelloWorld")


def demo01(request):
    # html文件转http响应，需要render( request, "html文件路径" )
    # 此处不能直接return html, 必须返回一个HttpResponse对象
    # request，html模版，传递到html页面的信息 =》字典格式
    return render(request, 'app01/demo01.html')


def demo02_form(request):
    username = request.GET.get("email")
    password = request.GET.get("password")
    # request，html模版，传递到html页面的信息 =》字典格式
    return render(request,
                  'app01/demo02_form.html',
                  {"user": username, "password": password})


def demo02_form2(request):
    if request.method == "POST":
        username = request.POST.get("email")
        # request，html模版，传递到html页面的信息 =》字典格式
        return HttpResponse(f"<h2>欢迎你，{username}</h2>")
    return render(request, 'app01/demo02_form2.html')


def demo02_form3(request):
    userlist = {"a@a.com": "123123"}
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        if username in userlist and password == userlist[username]:
            # request，html模版，传递到html页面的信息 =》字典格式
            return HttpResponse(f"<h2>欢迎你，{username}</h2>")
    return render(request, 'app01/demo02_form2.html')


from .models import UserInfo


def demo02_form_db(request):
    msg = ""
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        try:
            result = UserInfo.objects.get(email=username)
            if result and result.password == password:
                # request，html模版，传递到html页面的信息 =》字典格式
                return HttpResponse(f"<h2>欢迎你，{username}</h2>")
            else:
                msg = "用户名或密码错误！"
        except Exception as ex:
            msg = "用户名不存在！"
    kwgs = {
        "msg": msg,
    }
    return render(request, 'app01/demo02_form_db.html', kwgs)


def login(request):

    return render(request, 'app01/login.html')
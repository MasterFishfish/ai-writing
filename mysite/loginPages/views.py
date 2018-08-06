import json

from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.template import loader, RequestContext
from django.template.context_processors import csrf
from django.utils import timezone

from loginPages.models import user

def login(request):
    templates = loader.get_template(template_name="login/login.html")
    return HttpResponse(templates.render({"A": 1}, request))

def regist(request):
    templates = loader.get_template(template_name="login/regist.html")
    return HttpResponse(templates.render({"a": 1}, request))

def do_login(request):
    userId = ''
    password = ''
    data = {}
    if request.method == 'GET':
        userId = request.GET.get('userId','')
        password = request.GET.get('userpassword','')
    if request.method == 'POST':
        userId = request.POST.get('userId','')
        password = request.POST.get('userpassword','')
    try:
        theUser = user.objects.get(pk=userId)
        print(theUser)
        print(type(theUser))
        userInfo = theUser.toJSON()
    except user.DoesNotExist:
        theUser = None
    templates = loader.get_template(template_name="login/login_result.html")
    if theUser is not None:
        if password == theUser.user_password:
            #return HttpResponse(templates.render({"theUser": theUser}, request))
            data = {"theUser":userInfo, "state": True}
        else:
            #return HttpResponse(templates.render({'theUser': "用户名和密码不匹配"}, request))
            data = {"theUser":None, "state": False}
    else:
        #return HttpResponse(templates.render({'theUser': "用户名和密码不匹配"}, request))
        data = {"theUser": None, "state": False}
    return JsonResponse(data)
    #return render_to_response('login/login_result.html',c,context_instance=RequestContext(request))

def do_regist(request):
    #传入格式？
    userId = ''
    username = ''
    userpassword = ''
    state = ''
    if request.method == 'GET':
        userId = request.GET.get('userId','')
        userpassword = request.GET.get('userpassword','')
        username = request.GET.get('username', '')
    if request.method == 'POST':
        userId = request.POST.get('userId','')
        userpassword = request.POST.get('userpassword','')
        username = request.POST.get('username', '')
    try:
        theUser = user.objects.get(pk=userId)
    except user.DoesNotExist:
        theUser = None
    if theUser is not None:
        state = False
    else:
        newUser = user(user_id = userId, user_name = username, user_password = userpassword,
                    registDate = timezone.now())
        newUser.save()
        state = True
    theInfo = {}
    theInfo["state"] = state
    return JsonResponse(theInfo)

def login_results(request):
    return render(request, 'login/login_result.html', {'theUser': "AAA"})




import json

from django import forms
from django.shortcuts import render, get_object_or_404, render_to_response, redirect

# Create your views here.
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.template import loader, RequestContext
from django.utils import timezone
import logging
from loginPages.models import user

registlogger = logging.getLogger("register")
loginlogger = logging.getLogger("login")

def login(request):
    templates = loader.get_template(template_name="login/login.html")
    return HttpResponse(templates.render({"A": 1}, request))

def regist(request):
    templates = loader.get_template(template_name="login/regist.html")
    return HttpResponse(templates.render({"a": 1}, request))

def do_login(request):
    # userId = ''
    # password = ''
    # data = {}
    # if request.method == 'GET':
    #     userId = request.GET.get('userId','')
    #     password = request.GET.get('userpassword','')
    # if request.method == 'POST':
    #     userId = request.POST.get('userId','')
    #     password = request.POST.get('userpassword','')
    # try:
    #     theUser = user.objects.get(pk=userId)
    #     print(theUser)
    #     print(type(theUser))
    #     userInfo = theUser.toJSON()
    # except user.DoesNotExist:
    #     theUser = None
    # templates = loader.get_template(template_name="login/login_result.html")
    # if theUser is not None:
    #     if password == theUser.user_password:
    #         data = {"theUser":userInfo, "state": True}
    #     else:
    #         data = {"theUser":None, "state": False}
    # else:
    #     data = {"theUser": None, "state": False}
    # return JsonResponse(data)
    userId = ''
    password = ''
    if request.method == 'GET':
        userId = request.GET.get('userId','')
        password = request.GET.get('userpassword','')
    if request.method == 'POST':
        userId = request.POST.get('userId','')
        password = request.POST.get('userpassword','')
    loginlogger.info('%s try login' % userId)
    try:
        theUser = user.objects.get(pk=userId)
        print(theUser)
        print(type(theUser))
        userInfo = theUser.toJSON()
        print(userInfo)
    except user.DoesNotExist:
        theUser = None
        userInfo = None
        loginlogger.info('%s logining failed' % userId)
    if theUser is not None:
        if password == theUser.user_password:
            state = 1
            request.session['userId'] = userId
            print(request.session.get('userId', userId))
            loginlogger.info("%s login success" % userId)
        else:
            state = 0
    else:
        state =  0
    content = {}
    content["state"] = state
    content["theUser"] = userInfo
    print(content)
    print(JsonResponse(content))
    return JsonResponse(content)

def do_regist(request):
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

def do_logout(request):
    userId = ''
    if request.method == 'GET':
        userId = request.GET.get('userId','')
    if request.method == 'POST':
        userId = request.POST.get('userId','')
    print(request.session.get('userId', userId))
    try:
        del request.session["userId"]
        state = "1"
    except:
        state = "0"
    theInfo = {}
    theInfo["state"] = state
    return JsonResponse(theInfo)

def login_results(request):
    return render(request, 'login/login_result.html', {'theUser': "AAA"})




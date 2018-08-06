#!/usr/bin/python
# coding=utf-8
# Create your views here.
from urllib import parse

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template import loader

from loginPages.models import user
from personalpage.keyextract.keyextract import keysextract
from personalpage.spider.baikeSpider import baidubaikespider

def welcomepage(request):
    templates = loader.get_template('users/welcome.html')
    return HttpResponse(templates.render({"A": 1}, request))

def personalpage(request, user_id):
    templates = loader.get_template('users/personal.html')
    theUser = user.objects.get(pk=user_id)
    a = {"user_id": theUser.user_id}
    return render(request, 'users/personal.html', a)

def personal_materials_recommend(request, user_id):
    strs = ""
    if request.method  == 'GET':
        strs = request.GET.get('str', '')
        strs = parse.unquote(strs)
        print(strs)
    if request.method == 'POST':
        strs = request.POST.get('str', '')
        strs = parse.unquote(strs)
        print(strs)
    extractor = keysextract(strs, 3)
    keywords = extractor.getKeywords_tfidf()
    baiduspider = baidubaikespider(keywords)
    keywordsInfo = baiduspider.getinfomation()
    print(keywordsInfo)
    return JsonResponse(keywordsInfo)



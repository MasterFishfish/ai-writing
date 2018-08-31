import json
from urllib import parse

from django.shortcuts import render

# Create your views here.
from rest_framework import request, status
from rest_framework.views import APIView

from algorithm.keyextract.keyextract import keysextract
from algorithm.spider.baikeSpider import baidubaikespider
from undefined.helpers import JSONResponse, InputErrorMessage


def search_keyword(request):
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
    #print(keywordsInfo)
    result = {}
    result["result"] = keywordsInfo
    print(result)
    return JSONResponse(result)

class Search_keyword(APIView):
    def post(self):
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return InputErrorMessage(
                "Invalid JSON body",
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        if "str" not in data:
            return InputErrorMessage("strings not provide.")
        strs = data["str"]
        extractor = keysextract(strs, 3)
        keywords = extractor.getKeywords_tfidf()
        baiduspider = baidubaikespider(keywords)
        keywordsInfo = baiduspider.getinfomation()
        # print(keywordsInfo)
        result = {}
        result["result"] = keywordsInfo
        print(result)
        return JSONResponse(result)


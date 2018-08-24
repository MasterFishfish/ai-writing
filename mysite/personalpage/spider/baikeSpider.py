#!/usr/bin/python
# coding=utf-8
import random
from urllib import parse

import re
import requests
from lxml import etree

baikeurl = "https://baike.baidu.com/item/"


class baidubaikespider():
    def __init__(self, keywords):
        self.__urls = baikeurl
        self.__keywords = keywords

    def get_one_page(self, url):
        headerArray = [
            'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0;en-US)',
            'Mozilla/5.0 (Window NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
            'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1'
        ]
        try:
            headers = {
                'User-Agent': random.choice(headerArray)
            }
            response = requests.get(url, headers=headers)
            response.encoding = 'UTF-8'
            if response.status_code == 200 or response.status_code == 302:
                return response.text, response.url
            else:
                return None
        except:
            return None

    def parse_one_page(self, text):
        # print(text)
        html = etree.HTML(text)
        result = etree.tostring(html)
        # a = parse.unquote(result.decode('utf-8'))
        # print(a)
        summaryStrings = html.xpath("//div[@class='lemma-summary']//text()")
        summaryStrings = "".join(summaryStrings)
        summaryStrings = summaryStrings.split("\n")
        summaryStrings = "".join(summaryStrings)
        summaryStrings = summaryStrings.replace('\xa0'," ")
        results = re.findall('.*?(\[\d\]).*?', summaryStrings)
        if len(results) != 0:
            for result in results:
                summaryStrings = summaryStrings.replace(result, "")
        print(summaryStrings)
        return summaryStrings

    def getinfomation(self):
        result = []
        for keyword in self.__keywords:
            thisword = {}
            url = self.__urls + keyword
            htmltext, thisurl = self.get_one_page(url)
            keywordInfo = self.parse_one_page(htmltext)
            thisword["keyword"] = keyword
            thisword["str"] = keywordInfo
            thisword["url"] = thisurl
            result.append(thisword)
        return result




if __name__ == "__main__":
    url = "https://baike.baidu.com/item/%E8%8B%8F%E8%8F%B2%C2%B7%E7%8E%9B%E7%B4%A2/822003?fromtitle=%E8%8B%8F%E8%8F%B2%E7%8E%9B%E7%B4%A2&fromid=11156560&fr=aladdin#5"
    #text = get_one_page(url)
    #parse_one_page(text)
    #print(parse_one_page(text))


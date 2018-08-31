# coding=utf-8
import sys, codecs
import pandas as pd
import numpy as np
import jieba.posseg
import jieba.analyse
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

from algorithm.keyextract.stopkey import stopkey



class keysextract():
    def __init__(self, text, topK):
        self.__text = text
        self.__stopkey = stopkey
        self.__topK = topK

    def dataPrepos(self, text, stopkey):
        l = []
        pos = ['n', 'nz', 'nr', 'nt']
        seg = jieba.cut(text, cut_all=False)
        for i in seg:
            #if i.word not in stopkey and i.flag in pos:
                #l.append(i.word)
            if i not in stopkey:
                l.append(i)
        return l

    def getKeywords_tfidf(self):
        strings = self.__text
        stopkey = self.__stopkey
        topK = self.__topK
        # 1. 提取输入字符串中的一串名词，储存在同一字符串中，并以空格键隔开
        corpus = []
        text = self.dataPrepos(strings, stopkey)
        text = " ".join(text)
        corpus.append(text)

        # 2. 构建词频矩阵
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(corpus)  # 词频矩阵,a[i][j]:表示j词在第i个文本中的词频

        # 3. 统计每一个词的tf-idf权值
        transformer = TfidfTransformer()
        tfidf = transformer.fit_transform(X)

        # 4. 获取词袋模型中的关键词
        word = vectorizer.get_feature_names()
        print(word)

        # 5. 获取tf-idf矩阵，a[i][j]表示j词在i篇文本中的tf-idf权重
        weight = tfidf.toarray()
        print(len(weight[0]))

        # 6. 将tf-idf矩阵的值和词袋模型中的关键词对应起来，并且按照tfidf降序排列
        df_word = []
        df_weight = []
        for j in range(len(word)):
            # print (word[j],weight[i][j])
            df_word.append(word[j])
            df_weight.append(weight[0][j])
        df_word = pd.DataFrame(df_word, columns=['word'])
        df_weight = pd.DataFrame(df_weight, columns=['weight'])
        word_weight = pd.concat([df_word, df_weight], axis=1)  # 拼接词汇列表和权重列表
        word_weight = word_weight.sort_values(by="weight", ascending=False)  # 按照权重值降序排列
        keyword = np.array(word_weight['word'])  # 选择词汇列并转成数组格式
        print("keyword len", len(keyword))
        print(topK)
        if topK >= len(keyword):
            topK = len(keyword)
        print(topK)
        word_split = [keyword[x] for x in range(topK)]  # 抽取前topK个词汇作为关键词
        print(word_split)
        return word_split
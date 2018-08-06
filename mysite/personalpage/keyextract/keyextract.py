#!/usr/bin/python
# coding=utf-8
import sys, codecs
import pandas as pd
import numpy as np
import jieba.posseg
import jieba.analyse
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

from personalpage.keyextract.stopWord import stopkey



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
        word_split = [keyword[x] for x in range(0, topK)]  # 抽取前topK个词汇作为关键词
        print(word_split)
        return word_split


if __name__ == '__main__':
    data = "谁家的清笛渐响渐远，" \
           "不在断壁残垣下苦等一圈又一圈的轮回。何处的寒鸦栖枝复惊，不在枯藤老树下遥望阔别已久的故人。" \
           "时间的沙掩埋了一切细碎过往，只有一声轻叹仍在耳畔回响。" \
           "浮沉各异势，昔人更行更远，相见知何日？怕是碧落黄泉，两处难寻。" \
           "每每下象棋，我总是选执黑色一方，在棋盘上调兵遣将，作这一方小小天地的王。" \
           "红黑两军对垒，仿佛再现了那场千年前的楚汉之争。" \
           "手中冰凉的棋子积郁着霸王不屈的站魂，心中的愤懑和不甘化作棋子落盘时的声声闷响。" \
           "每动一子，心情复杂。我不知道乌江河畔，霸王为何不肯过江东。" \
           "我不知道霸王托付心爱战马时又是何种心情。" \
           "我不知道霸王看虞姬起舞时，有没有读懂她精致妆容暗藏的哀伤与绝望。" \
           "亡者长眠，生者久哀。那无边无际的长恨和无奈穿越时光之河，在我心头拍打出翻滚波浪。" \
           "仍记得小时候第一次听到项羽故事时的感触，也是从那时起，对霸王的敬仰与日俱增，可随着年龄的增加，我更深一层的了解霸王。" \
           "他的自傲，独尊霸王，四处封侯;他的英雄情怀，国恨家仇，个个必报;他的残暴，火烧阿房，屠城绝患;" \
           "他的勇猛，破釜沉舟，大破秦兵;他的目光短浅，气走范增，垓下之围命丧黄泉。" \
           "这些交织的在我心中存在，然少年心中的英雄容不的有半点瑕疵。" \
           "渐渐的，开始讨厌他，怨恨他，一种被欺骗的感觉深深占据了脑海。敬之深，恨之切。固执的认为他是自作自受。" \
           "将他和对他的崇敬深深锁在心底黑暗牢笼。下棋时，虽仍执黑棋，却充满了厌弃。" \
           "昔日里心中霸王的无敌形象，土崩瓦解。暗想昔人已逝，永不再来。"
    dataA = "苏菲玛索是法国独具个性、充满传奇色彩的女明星，她的成功、她的爱情选择都充分地体现着法兰西民族的个性。当有人问苏菲·玛索，她在片中常演出大胆激情场面时心态如何时，苏菲·玛索说，生活中本就充满了“爱”与“神秘”，我只是将人生片段带入电影中，不在乎裸露"
    thekeysextract = keysextract(text=dataA, topK=4)
    thekeysextract.getKeywords_tfidf()
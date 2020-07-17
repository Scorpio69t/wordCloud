import numpy as np
import matplotlib.pyplot as plt
#pip install WordCloud
from wordcloud import WordCloud,STOPWORDS
from PIL import Image
from os import path
import cv2
import matplotlib.pyplot as plt
#用来正常显示中文
plt.rcParams["font.sans-serif"]=["SimHei"]
#用来正常显示负号
plt.rcParams["axes.unicode_minus"]=False
import os
#pip install jieba
import random,jieba

'''
绘制单个词一个圆形的词云（设置每个值的权重）
'''
def single_wordColud_1():
    text = {"第一":0.1,"第二":0.2,"第三":0.3,"第四":0.4}
    #产生一个以(150,150)为圆心,半径为130的圆形mask
    x,y = np.ogrid[:300,:300]
    mask = (x-150) ** 2 + (y-150) ** 2 > 130 ** 2
    mask = 255 * mask.astype(int)
    wc = WordCloud(background_color="white",font_path='./simkai.ttf',repeat=True,mask=mask)
    wc.generate_from_frequencies(text) 
    #将x轴和y轴坐标隐藏
    plt.axis("off")
    plt.imshow(wc,interpolation="bilinear")
    plt.show()
    
'''
绘制单个词一个圆形的词云
'''
def single_wordColud():
    text = "第一 第二 第三 第四"
    #产生一个以(150,150)为圆心,半径为130的圆形mask
    x,y = np.ogrid[:300,:300]
    mask = (x-150) ** 2 + (y-150) ** 2 > 130 ** 2
    mask = 255 * mask.astype(int)
    wc = WordCloud(background_color="white",font_path='./simkai.ttf',repeat=True,mask=mask)
    wc.generate(text)

    #将x轴和y轴坐标隐藏
    plt.axis("off")
    plt.imshow(wc,interpolation="bilinear")
    plt.show()    

def grey_color_func(word,font_size,position,orientation,random_state=None,**kwargs):
    return "hsl(0,0%%,%d%%)"%random.randint(60,100)


'''
从文件中读取停用词
'''
def get_stopwords():
    dir_path = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    #获取停用词的路径
    stopwords_path = os.path.join(dir_path,"txt/stopwords.txt")
    #创建set集合来保存停用词
    stopwords = set()
    #读取文件
    f = open(stopwords_path,"r",encoding="utf-8")
    line_contents = f.readline()
    while line_contents:
        #去掉回车
        line_contents = line_contents.replace("\n","").replace("\t","").replace("\u3000","")
        stopwords.add(line_contents)
        line_contents = f.readline()
    return stopwords

'''
中文分词
'''
def segment_words(text):
    article_contents = ""
    #使用jieba（结巴）进行分词
    words = jieba.cut(text,cut_all=False)
    for word in words:
        #使用空格来分割词
        article_contents += word+" "
    return article_contents



def drow_mask_wordColud():
    #获取当前文件的父目录
    #d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    #mask = np.array(Image.open(path.join(d,"img/test.jpg")))
    
    #以下用咱们刚刚另存为的图就可以（必须是白色背景）
    mask = cv2.imread("img/1.jpg")
    
    #test.txt内容随便写
    text = open(path.join("txt/test.txt"),"r",encoding="utf-8").read().replace("\n","").replace("\t","").replace("\u3000","")
    #text = "甜心 美丽 漂亮 性感 贤惠 温柔 可爱 宝宝 排长"
    
    print(text)
    #对文本进行分词
    text = segment_words(text)
    #获取停用词
    stopwords = get_stopwords()
    #创建词云
    '''
    字体路径 ：simkai.ttf 简体字，解决汉字出现框框的问题 这个文件只要你安装了WordCloud第三方库就有的了，如果不知道路径，Everything直接搜索（简单粗暴）  
    scale:条件生成词云的清晰度，值越大越清晰 默认是1
    max_words:显示词的数量
    mask:背景
    stopwords:停用词,是一个set集合 有的话就自己定义就行了，或者用内置的STOPWORDS stopwords=STOPWORDS  或者直接不设置
    margin:词之间的间隔
    background_color:词云图片背景颜色
    repeat:为词是否可重复 true 为可重复  默认false 不可重复
    '''
    wc = WordCloud(scale=4,max_words=300,mask=mask,background_color="white",font_path='./simkai.ttf',stopwords=stopwords,margin=10,random_state=1).generate(text)
    default_colors = wc.to_array()
    # #保存词云图片（自定义）
    wc.to_file("img/test.png")
    plt.imshow(default_colors,interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    drow_mask_wordColud()
    #single_wordColud()
    #single_wordColud_1()
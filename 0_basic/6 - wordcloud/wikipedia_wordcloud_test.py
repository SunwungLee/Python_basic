# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:04:24 2021

@author: Wyatt
"""

import wikipedia
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off")
    # plt.savefig('wiki_bts_wordcloud_en')


img = Image.open('bts.jpg')
bts_mask = np.array(img)
#print(bts_mask)

# # 위키백과 사전의 컨텐츠 제목을 명시해 준다
# # 이 페이지의 텍스트 컨텐츠를 추출하도록 한다
wikipedia.set_lang("en")
wiki = wikipedia.page("BTSS")

text = wiki.content

# 불용어 활용
#s_word = STOPWORDS.union({'one','using','first','two','make','use'})


# 워드 클라우드를 생성하기 위해 위의 코드를 삽입할 것
wordcloud = WordCloud(width = 2000, height = 1500, 
                      stopwords = STOPWORDS,
                      background_color="white",
                      #font_path = "font/HARLOWSI.TTF"
                      mask = bts_mask
                      ).generate(text)


# wikipedia.set_lang("ko")
# p_wiki = wikipedia.page('방탄소년단')
# text = p_wiki.content
# wordcloud = WordCloud(font_path='C:Windows/Fonts/malgunbd.ttf',
#                       background_color='white',
#                       mask = bts_mask
#                       ).generate(text)

plot_cloud(wordcloud)

# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import jieba


# 得到jieba分词后的文本
def get_text_cut(txt):
    text = open(txt, 'r', encoding='utf8').read()
    return ' '.join(jieba.cut(text))


# 以image为背景模板
def word_cloud_1(text, image, save_image):
    mask = np.array(Image.open(image))
    wc = WordCloud(background_color="white",
                   max_words=1000,
                   mask=mask,
                   max_font_size=100,
                   random_state=1,
                   scale=2,
                   font_path='C:/Windows/Fonts/simkai.ttf',  # 字体
                   ).generate(text)

    print('生成词云成功！')

    img_colors = ImageColorGenerator(mask)  # 将背景图片颜色应用到词语颜色上
    plt.imshow(wc.recolor(color_func=img_colors))
    plt.axis('off')
    plt.show()

    wc.to_file(save_image)


# 生成普通词云
def word_cloud_2(text, save_image):
    wc = WordCloud(background_color='black',
                   max_words=1000,
                   max_font_size=100,
                   random_state=1,
                   scale=2,
                   font_path='C:/Windows/Fonts/simkai.ttf',  # 字体
                   ).generate(text)

    print('生成词云成功！')

    plt.imshow(wc)
    plt.axis('off')
    plt.show()

    wc.to_file(save_image)


def main():
    text = get_text_cut('19th.txt')
    word_cloud_1(text, 'flag.jpg', 'test1.jpg')
    word_cloud_2(text, 'test2.jpg')


if __name__ == '__main__':
    main()

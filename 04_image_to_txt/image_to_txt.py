# -*-coding:utf-8-*-
'''
将图片转为txt文档显示
txt文档需要用记事本之类的打开，并将字体改小
'''

from PIL import Image


serarr=['@', '#', '$', '%', '&', '?', '*', 'o', '/', '{', '[', '(', '|', '!', '^', '~', '-', '_', ':', ';', ',', '.', '`', ' ']
count = len(serarr)


def toTxt(image_file):
    image_file = image_file.convert("L")      # 转灰度
    asd = ''     # 储存字符串
    for h in range(0,  image_file.size[1]):     # h
        for w in range(0, image_file.size[0]):      # w
            gray = image_file.getpixel((w, h))
            asd = asd+serarr[int(gray/(255/(count-1)))]  
        asd = asd+'\r\n'  
    return asd  


def image2txt(image, txt):
    image_file = Image.open(image)      # 打开图片
    image_file = image_file.resize((int(image_file.size[0]*0.9), int(image_file.size[1]*0.9)))      # 调整图片大小
    print('Info:', image_file.size[0], ' ', image_file.size[1], ' ', count)

    tmp = open(txt, 'w')
    tmp.write(toTxt(image_file))  
    tmp.close()  


if __name__ == '__main__':
    image2txt('image.jpg', 'txt.txt')

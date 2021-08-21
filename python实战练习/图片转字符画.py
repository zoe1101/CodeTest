# 为一张图片生成对应的字符集图片
# 字符画是一系列字符的组合，我们可以把字符看作是比较大块的像素，一个字符能表现一种颜色（暂且这么理解吧），字符的种类越多，可以表现的颜色也越多，图片也会更有层次感。
from PIL import Image # PIL 是一个 Python 图像处理库
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# 是我们的字符画所使用的字符集，一共有 70 个字符，字符的种类与数量可以自己根据字符画的效果反复调试的
WIDTH = 60 # 字符画的宽
HEIGHT = 45 # 字符画的高
# 将256灰度映射到70个字符上，也就是RGB值转字符的函数：
def get_char(r,g,b,alpha=256):# alpha透明度
    if alpha==0:
        return ''
    length=len(ascii_char)
    gray=int(0.2126*r+0.7152*g+0.0722*b) ##计算灰度
    unit=(256.0+1)/length
    return ascii_char[int(gray/unit)]  # 不同的灰度对应着不同的字符

if __name__ == '__main__':
    img = r'D:\CODE\CodeTest\data\ascii_dora.png'  # 图片所在位置
    im = Image.open(img)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))  # 获得相应的字符
        txt += '\n'
    print(txt)  # 打印出字符画
    # 将字符画 写入文件中
    # with open("C:/Users/lec/Desktop/output.txt", 'w') as f:
    #     f.write(txt)
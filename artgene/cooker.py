# coding:utf-8
from tkinter import *
import math
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab


def cookerAssemble():
    print("this is haohao")
    s1u = {'S1': -0.133, 'S2': -0.155, 'S3': -0.330, 'S4': 0.160, 'S5': 0.700, 'S6': -0.240, \
           'K1': 0.133, 'K2': -0.064, 'K3': -0.034, 'K4': -0.034, 'B1': 0.046, 'B2': 0.041, 'B3': 0.046, 'B4': -0.132, \
           'D1': 0.051, 'D2': -0.051}
    s1q = {'S': 0.68382, 'K': 0.13112, 'B': 0.11784, 'D': 0.06722}
    s1c = -0.78

    s2u = {'S1': 0.020, 'S2': 0.535, 'S3': -0.265, 'S4': -0.182, 'S5': 0.050, 'S6': -0.160, \
           'K1': 0.128, 'K2': 0.093, 'K3': -0.115, 'K4': -0.107, 'B1': 0.081, 'B2': -0.075, 'B3': 0.071, 'B4': -0.077, \
           'D1': -0.011, 'D2': 0.011}
    s2q = {'S': 0.65406, 'K': 0.19928, 'B': 0.12877, 'D': 0.01788}
    s2c = -0.165

    s3u = {'S1': -0.045, 'S2': 0.405, 'S3': -0.258, 'S4': -0.043, 'S5': 0.063, 'S6': -0.123, \
           'K1': 0.040, 'K2': -0.038, 'K3': 0.048, 'K4': -0.050, 'B1': 0.088, 'B2': 0.038, 'B3': -0.070, 'B4': -0.055, \
           'D1': 0.001, 'D2': -0.001}
    s3q = {'S': 0.72011, 'K': 0.10598, 'B': 0.17120, 'D': 0.00272}
    s3c = -0.503

    s4u = {'S1': 0.021, 'S2': -0.366, 'S3': 0.036, 'S4': 0.071, 'S5': 0.316, 'S6': -0.079, \
           'K1': 0.084, 'K2': -0.063, 'K3': -0.053, 'K4': 0.032, 'B1': -0.056, 'B2': 0.067, 'B3': -0.026, 'B4': 0.014, \
           'D1': -0.056, 'D2': 0.056}
    s4q = {'S': 0.64160, 'K': 0.13866, 'B': 0.11516, 'D': 0.10458}
    s4c = -0.596

    s5u = {'S1': -0.045, 'S2': 0.027, 'S3': -0.353, 'S4': 0.082, 'S5': 0.537, 'S6': -0.248, \
           'K1': 0.177, 'K2': 0.037, 'K3': -0.101, 'K4': -0.113, 'B1': -0.048, 'B2': 0.092, 'B3': -0.011, 'B4': -0.033, \
           'D1': 0.026, 'D2': -0.026}
    s5q = {'S': 0.64904, 'K': 0.21149, 'B': 0.10210, 'D': 0.03737}
    s5c = -0.482

    S = ['S1', 'S2', 'S3', 'S4']
    K = ['K1', 'K2', 'K3', 'K4']
    B = ['B1', 'B2', 'B3', 'B4']
    D = ['D1', 'D2']
    print
    'dsfsdfs'
    content = var.get()
    print
    content
    content = content.split(',')
    print
    content
    minValue = -1
    minitemS = 0
    minitemK = 0
    minitemB = 0
    minitemD = 0
    for itemA in S:
        for itemB in K:
            for itemC in B:
                for itemD in D:
                    s1 = s1u[itemA] * s1q['S'] + s1u[itemB] * s1q['K'] + s1u[itemC] * s1q['B'] + s1u[itemD] * s1q[
                        'D'] + s1c
                    s2 = s2u[itemA] * s2q['S'] + s2u[itemB] * s2q['K'] + s2u[itemC] * s2q['B'] + s2u[itemD] * s2q[
                        'D'] + s2c
                    s3 = s3u[itemA] * s3q['S'] + s3u[itemB] * s3q['K'] + s3u[itemC] * s3q['B'] + s3u[itemD] * s3q[
                        'D'] + s3c
                    s4 = s4u[itemA] * s4q['S'] + s4u[itemB] * s4q['K'] + s4u[itemC] * s4q['B'] + s4u[itemD] * s4q[
                        'D'] + s4c
                    s5 = s5u[itemA] * s5q['S'] + s5u[itemB] * s5q['K'] + s5u[itemC] * s5q['B'] + s5u[itemD] * s5q[
                        'D'] + s5c
                    # s6 = s6u[itemA] * s6q['S'] + s6u[itemB] * s6q['K'] + s6u[itemC] * s6q['B'] + s6u[itemD] * s6q['D'] + s6c
                    value = math.sqrt((s1 - int(content[0])) * (s1 - int(content[0])) + (s2 - int(content[1])) * (
                    s2 - int(content[1])) \
                                      + (s3 - int(content[2])) * (s3 - int(content[2])) + (s4 - int(content[3])) * (
                                      s4 - int(content[3])) + (s5 - int(content[4])) * (s5 - int(content[4])) \
                                      )
                    if minValue == -1 or minValue > value:
                        minValue = value
                        minitemS = itemA
                        minitemK = itemB
                        minitemB = itemC
                        minitemD = itemD
    boat = Image.new('RGBA', (1625, 1000), 'white')
    imageA = Image.open(minitemS + '.png')
    imageB = Image.open(minitemK + '.png')
    imageC = Image.open(minitemB + '.png')

    # imageA = Image.open('S2' + '.png')
    # imageB = Image.open('K3' + '.png')
    # imageC = Image.open('B1' + '.png')

    imageDMask = Image.open('maskboardD1RGB229.229.229' + '.jpg')
    imgaecaizhi = Image.open('M22' + '.jpg')
    imgaecaizhi = imgaecaizhi.resize((1652, 1000))
    imgaelogo = Image.open('LOGO4' + '.png')
    print
    imageDMask.size, imgaecaizhi.size
    print
    minitemS, minitemK, minitemB, minitemD

    imageDMaskArray = np.array(imageDMask)
    # rows,cols,dims = imageDMaskArray.shape
    # for x in range(rows):
    #    for y in range(cols):
    #        if(imageDMaskArray[x,y,0] == 229&imageDMaskArray[x,y,1] == 229&imageDMaskArray[x,y,2] == 229):
    #            imageDMaskArray[x,y,0] = 27
    #            imageDMaskArray[x,y,0] = 224
    #            imageDMaskArray[x,y,0] = 20
    # print imageDMaskArray[x,y:].all()
    # plt.imshow(imageDMaskArray)
    # imageDMask = Image.fromarray(imageDMaskArray)
    # imgBlend = Image.blend(imageDMask, imgaecaizhi, 0.7)
    imgBlend = imageDMask
    r, g, b, a = imageC.split()
    boat.paste(imgBlend, (0, 0))
    boat.paste(imageC, (0, 0), mask=a)
    r, g, b, a = imageA.split()
    boat.paste(imageA, (0, 0), mask=a)
    r, g, b, a = imageB.split()
    boat.paste(imageB, (0, 0), mask=a)
    r, g, b, a = imgaelogo.split()
    # boat.paste(imgaelogo, (0,0), mask = a)
    plt.imshow(boat)
    # imageA.paste(imageC)
    plt.show()


if __name__ == '__main__':
    img = ImageGrab.grab()
    # img.show()
    img.save("3.png")
    root = Tk()
    root.title(u"燃气灶生成")
    root.geometry('300x200')
    Label(root, text=u"请输入5个1-7的用户意向值，以逗号隔开", font=('Arial', 10)).pack()
    var = StringVar()
    e = Entry(root, textvariable=var)
    var.set("")
    e.pack()
    Button(root, text=u"确定", command=cookerAssemble).pack()
    root.mainloop()

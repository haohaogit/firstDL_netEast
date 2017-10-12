# coding:utf-8
from tkinter import *
import math
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def cookerAssemble(content):
    s1u = {'A1': -0.133, 'A2': -0.155, 'A3': -0.330, 'A4': 0.160, 'A5': 0.700, 'A6': -0.240, \
           'B1': 0.133, 'B2': -0.064, 'B3': -0.034, 'B4': -0.034, 'C1': 0.046, 'C2': 0.041, 'C3': 0.046,
           'C4': -0.132, \
           'D1': 0.051, 'D2': -0.051}
    s1q = {'A': 0.68382, 'B': 0.13112, 'C': 0.11784, 'D': 0.06722}
    s1c = -0.78

    s2u = {'A1': 0.020, 'A2': 0.535, 'A3': -0.265, 'A4': -0.182, 'A5': 0.050, 'A6': -0.160, \
           'B1': 0.128, 'B2': 0.093, 'B3': -0.115, 'B4': -0.107, 'C1': 0.081, 'C2': -0.075, 'C3': 0.071,
           'C4': -0.077, \
           'D1': -0.011, 'D2': 0.011}
    s2q = {'A': 0.65406, 'B': 0.19928, 'C': 0.12877, 'D': 0.01788}
    s2c = -0.165

    s3u = {'A1': -0.045, 'A2': 0.405, 'A3': -0.258, 'A4': -0.043, 'A5': 0.063, 'A6': -0.123, \
           'B1': 0.040, 'B2': -0.038, 'B3': 0.048, 'B4': -0.050, 'C1': 0.088, 'C2': 0.038, 'C3': -0.070,
           'C4': -0.055, \
           'D1': 0.001, 'D2': -0.001}
    s3q = {'A': 0.72011, 'B': 0.10598, 'C': 0.17120, 'D': 0.00272}
    s3c = -0.503

    s4u = {'A1': 0.021, 'A2': -0.366, 'A3': 0.036, 'A4': 0.071, 'A5': 0.316, 'A6': -0.079, \
           'B1': 0.084, 'B2': -0.063, 'B3': -0.053, 'B4': 0.032, 'C1': -0.056, 'C2': 0.067, 'C3': -0.026,
           'C4': 0.014, \
           'D1': -0.056, 'D2': 0.056}
    s4q = {'A': 0.64160, 'B': 0.13866, 'C': 0.11516, 'D': 0.10458}
    s4c = -0.596

    s5u = {'A1': -0.045, 'A2': 0.027, 'A3': -0.353, 'A4': 0.082, 'A5': 0.537, 'A6': -0.248, \
           'B1': 0.177, 'B2': 0.037, 'B3': -0.101, 'B4': -0.113, 'C1': -0.048, 'C2': 0.092, 'C3': -0.011,
           'C4': -0.033, \
           'D1': 0.026, 'D2': -0.026}
    s5q = {'A': 0.64904, 'B': 0.21149, 'C': 0.10210, 'D': 0.03737}
    s5c = -0.482

    S = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
    K = ['B1', 'B2', 'B3', 'B4']
    C = ['C1', 'C2', 'C3', 'C4']
    D = ['D1', 'D2']
    print
    'dsfsdfs'
    # content = var.get()
    # print content
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
            for itemC in C:
                for itemD in D:
                    s1 = s1u[itemA] * s1q['A'] + s1u[itemB] * s1q['B'] + s1u[itemC] * s1q['C'] + s1u


    [itemD] * s1q['D'] + s1c
    s2 = s2u[itemA] * s2q['A'] + s2u[itemB] * s2q['B'] + s2u[itemC] * s2q['C'] + s2u
    [itemD] * s2q['D'] + s2c
    s3 = s3u[itemA] * s3q['A'] + s3u[itemB] * s3q['B'] + s3u[itemC] * s3q['C'] + s3u
    [itemD] * s3q['D'] + s3c
    s4 = s4u[itemA] * s4q['A'] + s4u[itemB] * s4q['B'] + s4u[itemC] * s4q['C'] + s4u
    [itemD] * s4q['D'] + s4c
    s5 = s5u[itemA] * s5q['A'] + s5u[itemB] * s5q['B'] + s5u[itemC] * s5q['C'] + s5u
    [itemD] * s5q['D'] + s5c
    # s6 = s6u[itemA] * s6q['A'] + s6u[itemB] * s6q['B'] + s6u[itemC] * s6q['B'] + s6u[itemD] * s6q['D'] + s6c
    value = math.sqrt((s1 - float(content[0])) * (s1 - float(content[0])) + (s2 - float
    (content[1])) * (s2 - float(content[1])) + (s3 - float(content[2])) * (s3 - float(content[2])) + (s4 - float
    (content[3])) * (s4 - float(content[3])) + (s5 - float(content[4])) * (s5 - float(content[4])))
    if minValue == -1 or minValue > value:
        minValue = value
        minitemS = itemA
        minitemK = itemB
        minitemB = itemC
        minitemD = itemD
        print
        minValue

    if minitemD == "D1":
        boat = Image.new('RGBA', (1625, 1000), 'white')
        imageA = Image.open("./D1/" + minitemS + '.png')
        imageB = Image.open("./D1/" + minitemK + '.png')
        imageC = Image.open("./D1/" + minitemB + '.png')
        print
        minitemD
    else:
        boat = Image.new('RGBA', (1800, 1000), 'white')
        imageA = Image.open("./D2/" + minitemS + '.png')
        imageB = Image.open("./D2/" + minitemK + '.png')
        imageC = Image.open("./D2/" + minitemB + '.png')

        # imageA = Image.open('A2' + '.png')
        # imageB = Image.open('K3' + '.png')
        # imageC = Image.open('C1' + '.png')

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
    #        if(imageDMaskArray[x,y,0] == 229&imageDMaskArray[x,y,1] == 229&imageDMaskArray[x,y,2] ==229):
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
    plt.xlabel(minitemS + ' ' + minitemK + ' ' + minitemB + ' ' + minitemD, fontproperties='SimHei')
    plt.imshow(boat)
    plt.savefig('test.jpg', format='jpg')
    return minitemS, minitemK, minitemB, minitemD
    # imageA.paste(imageC)
    # plt.show()
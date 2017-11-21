import math
from PIL import Image
import numpy as np
# import matplotlib.pyplot as plt
import copy
import random
from PIL import ImageDraw
import sys
# print("脚本名：", sys.argv[0])
# print("参数", sys.argv[1])


def HtoRGB(v1, v2, h):
    if h < 0:
        h = h + 1
    if h > 1:
        h = h - 1
    if h < 1.0 / 6.0:
        return (v1 + (v2 - v1) * 6.0 * h)
    if h < 1.0 / 2.0:
        return (v2)
    if h < 2.0 / 3.0:
        return (v1 + (v2 - v1) * ((2.0 / 3.0) - h) * 6.0)
    return v1;


def hsv2rgb(h, s, l):
    r, g, b = 0, 0, 0
    if h >= 360:
        h = h - 360;
    if s == 0:
        r = g = b = l * 255.0
        return r, g, b
    h = h / 360.0
    x1, x2 = 0, 0
    if l < 0.5:
        x1 = l * (1 + s)
    else:
        x1 = l + s - s * l
    x2 = 2 * l - x1

    r = 255.0 * HtoRGB(x2, x1, h + 1.0 / 3.0)
    g = 255.0 * HtoRGB(x2, x1, h)
    b = 255.0 * HtoRGB(x2, x1, h - 1.0 / 3.0)
    return r, g, b


class pk:
    h = 0
    s = 0
    v = 0

    def __init__(self):
        self.h = 0
        self.s = 0
        self.v = 0


class pm:
    sh = 0
    ss = 0
    sl = 0
    h = 0
    ts = 0
    tl = 0

    def __init__(self):
        sh = 0
        ss = 0
        sl = 0
        h = 0
        ts = 0
        tl = 0


def AddAMatchingFromACenter(params, packs, numColorPerPack, h, s, l, span0, span1, span2, flag):
    if (flag == 0):
        theta = span0 / numColorPerPack
        leave = span0 - theta
        avg = leave / (numColorPerPack - 1)

        dis = 0
        low = 0
        if (numColorPerPack % 2 == 0):
            dis = avg / 2 + (numColorPerPack / 2 - 1) * avg
        else:
            dis = (numColorPerPack / 2) * avg
        low = h - dis
        pack = []

        for i in range(numColorPerPack):
            p = pk()
            p.h = low + avg * i
            p.s = s
            p.v = l
            if (p.h < 0):
                p.h += 360
            if (p.h > 360):
                p.h -= 360
            pack.append(p)
        packs.append(pack)

        param = pm()
        param.sh = span0
        param.ss = 0
        param.sl = 0
        param.th = h
        param.ts = s
        param.tl = l
        params.append(param)
    elif (flag == 1):
        avg = span1 / (numColorPerPack - 1)
        dis = 0
        low = 0
        if (numColorPerPack % 2 == 0):
            dis = avg / 2 + (numColorPerPack / 2 - 1) * avg
        else:
            dis = (numColorPerPack / 2) * avg
        low = s - dis
        pack = []

        for i in range(numColorPerPack):
            p = pk()
            p.h = h
            p.s = low + avg * i
            p.v = l

            if (p.s > 1.0):
                p.s = 0.95
            pack.append(p)
        packs.append(pack)

        param = pm()
        param.sh = 0
        param.ss = span1
        param.sl = 0
        param.th = h
        param.ts = s
        param.tl = l
        params.append(param)
    elif (flag == 2):
        avg = span2 / (numColorPerPack - 1)
        dis = 0
        low = 0
        if (numColorPerPack % 2 == 0):
            dis = avg / 2 + (numColorPerPack / 2 - 1) * avg
        else:
            dis = (numColorPerPack / 2) * avg
        low = l - dis

        pack = []

        for i in range(numColorPerPack):
            p = pk()
            p.h = h
            p.s = s
            p.v = low + avg * i

            if (p.v > 1.0):
                p.v = 0.95
            pack.append(p)
        packs.append(pack)

        param = pm()
        param.sh = 0
        param.ss = 0
        param.sl = span2
        param.th = h
        param.ts = s
        param.tl = l
        params.append(param)
    elif (flag == 3):  # 0+1
        theta = span0 / numColorPerPack
        leave = span0 - theta
        avg0 = leave / (numColorPerPack - 1)

        dis0 = 0
        low0 = 0
        if (numColorPerPack % 2 == 0):
            dis0 = avg0 / 2 + (numColorPerPack / 2 - 1) * avg0
        else:
            dis0 = (numColorPerPack / 2) * avg0
        low0 = h - dis0

        avg1 = span1 / (numColorPerPack - 1)
        dis1 = 0
        low1 = 0
        if (numColorPerPack % 2 == 0):
            dis1 = avg1 / 2 + (numColorPerPack / 2 - 1) * avg1
        else:
            dis1 = (numColorPerPack / 2) * avg1
        low1 = s - dis1

        pack = []

        for i in range(numColorPerPack):
            p = pk()
            p.h = low0 + avg0 * i
            p.s = low1 + avg1 * i
            p.v = l
            if (p.h < 0):
                p.h += 360
            if (p.h > 360):
                p.h -= 360
            if (p.s > 1.0):
                p.s = 0.95
            pack.append(p)
        packs.append(pack)

        param = pm()
        param.sh = span0
        param.ss = span1
        param.sl = 0
        param.th = h
        param.ts = s
        param.tl = l
        params.append(param)
    elif (flag == 4):  # 0+2
        theta = span0 / numColorPerPack
        leave = span0 - theta
        avg0 = leave / (numColorPerPack - 1)

        dis0 = 0
        low0 = 0
        if (numColorPerPack % 2 == 0):
            dis0 = avg0 / 2 + (numColorPerPack / 2 - 1) * avg0
        else:
            dis0 = (numColorPerPack / 2) * avg0
        low0 = h - dis0

        avg2 = span2 / (numColorPerPack - 1)
        dis2 = 0
        low2 = 0
        if (numColorPerPack % 2 == 0):
            dis2 = avg2 / 2 + (numColorPerPack / 2 - 1) * avg2
        else:
            dis2 = (numColorPerPack / 2) * avg2
        low2 = l - dis2

        pack = []

        for i in range(numColorPerPack):
            p = pk()
            p.h = low0 + avg0 * i
            p.s = s
            p.v = low2 + avg2 * i
            if (p.h < 0):
                p.h += 360
            if (p.h > 360):
                p.h -= 360
            if (p.v > 1.0):
                p.v = 0.95
            pack.append(p)
        packs.append(pack)

        param = pm()
        param.sh = span0
        param.ss = 0
        param.sl = span2
        param.th = h
        param.ts = s
        param.tl = l
        params.append(param)
    elif (flag == 5):  # 1+2
        avg1 = span1 / (numColorPerPack - 1)
        dis1 = 0
        low1 = 0
        if (numColorPerPack % 2 == 0):
            dis1 = avg1 / 2 + (numColorPerPack / 2 - 1) * avg1
        else:
            dis1 = (numColorPerPack / 2) * avg1
        low1 = s - dis1

        avg2 = span2 / (numColorPerPack - 1)
        dis2 = 0
        low2 = 0
        if (numColorPerPack % 2 == 0):
            dis2 = avg2 / 2 + (numColorPerPack / 2 - 1) * avg2
        else:
            dis2 = (numColorPerPack / 2) * avg2
        low2 = l - dis2

        pack = []

        for i in range(numColorPerPack):
            p = pk()
            p.h = h
            p.s = low1 + avg1 * i
            p.v = low2 + avg2 * i
            if (p.s > 1.0):
                p.s = 0.95
            if (p.v > 1.0):
                p.v = 0.95
            pack.append(p)
        packs.append(pack)

        param = pm()
        param.sh = 0
        param.ss = span1
        param.sl = span2
        param.th = h
        param.ts = s
        param.tl = l
        params.append(param)
    elif (flag == 6):  # 0+1+2
        theta = span0 / numColorPerPack
        leave = span0 - theta
        avg0 = leave / (numColorPerPack - 1)

        dis0 = 0
        low0 = 0
        if (numColorPerPack % 2 == 0):
            dis0 = avg0 / 2 + (numColorPerPack / 2 - 1) * avg0
        else:
            dis0 = (numColorPerPack / 2) * avg0
        low0 = h - dis0

        avg1 = span1 / (numColorPerPack - 1)
        dis1 = 0
        low1 = 0
        if (numColorPerPack % 2 == 0):
            dis1 = avg1 / 2 + (numColorPerPack / 2 - 1) * avg1
        else:
            dis1 = (numColorPerPack / 2) * avg1
        low1 = s - dis1

        avg2 = span2 / (numColorPerPack - 1)
        dis2 = 0
        low2 = 0
        if (numColorPerPack % 2 == 0):
            dis2 = avg2 / 2 + (numColorPerPack / 2 - 1) * avg2
        else:
            dis2 = (numColorPerPack / 2) * avg2
        low2 = l - dis2

        pack = []

        for i in range(numColorPerPack):
            p = pk()
            p.h = low0 + avg0 * i
            p.s = low1 + avg1 * i
            p.v = low2 + avg2 * i
            if (p.h < 0):
                p.h += 360
            if (p.h > 360):
                p.h -= 360
            if (p.s > 1.0):
                p.s = 0.95
            if (p.v > 1.0):
                p.v = 0.95
            pack.append(p)
        packs.append(pack)

        param = pm()
        param.sh = span0
        param.ss = span1
        param.sl = span2
        param.th = h
        param.ts = s
        param.tl = l
        params.append(param)


def generateScarv(rgbs, packNum, imageAName,timeid):
    C2 = [255, 0]
    C3 = [229, 127, 76]
    C4 = [229, 178, 127, 76]
    C5 = [229, 178, 127, 76, 25]
    C6 = [255, 229, 178, 127, 76, 25]
    C7 = [255, 229, 178, 127, 76, 51, 25]
    C8 = [229, 204, 178, 153, 127, 102, 76, 51]
    C9 = [229, 204, 178, 153, 127, 102, 76, 51, 25]
    C10 = [255, 229, 204, 178, 153, 127, 102, 76, 51, 25]
    rgbs = rgbs.split(',')

    # packNum = varPacNum.get()
    packNum = int(packNum)
    if packNum == 0:
        return

    # imageAName = varName.get()

    if imageAName == "":
        return

    imageA = Image.open(imageAName)
    imageAArray = np.array(imageA)
    C = []
    if packNum == 2:
        C = C2
    elif packNum == 3:
        C = C3
    elif packNum == 4:
        C = C4
    elif packNum == 5:
        C = C5
    elif packNum == 6:
        C = C6
    elif packNum == 7:
        C = C7
    elif packNum == 8:
        C = C7
    elif packNum == 9:
        C = C9
    elif packNum == 10:
        C = C10
    # print C
    rows, cols, dims = imageAArray.shape
    print(rows, cols, dims)
    images = []
    imageAArrayTemp = imageA.copy()
    pix = imageAArrayTemp.load()
    print(id(imageAArrayTemp))
    for x in range(rows):
        for y in range(cols):
            # print x,y
            # print imageAArray[x,y,0],imageAArray[x,y,1],imageAArray[x,y,2]
            for i in range(packNum):
                # if((imageAArray[x,y,0] in range(C[i]-5,C[i]+5))&(imageAArray[x,y,1] in range(C[i]-5,C[i]+5))&(imageAArray[x,y,2] in range(C[i]-5,C[i]+5))):
                # if imageAArrayTemp.getpixel[x,y] in range(C[i]-15,C[i]+15):
                r, g, b = pix[y, x]
                if r in range(C[i] - 15, C[i] + 15):
                    pix[y, x] = (int(rgbs[i * 3 + 0]), int(rgbs[i * 3 + 1]), int(rgbs[i * 3 + 2]))
                    break
                    # print int(rss[j][i]),int(gss[j][i]),int(bss[j][i])
                    # imageAArrayTemp.putpixel((x,y), (rss[j][i],gss[j][i],bss[j][i]))
                    # print id(imageAArrayTemp)

    # basename = imageAName.split("/")[-1]
    # print(basename.split(".")[0])
    imageAArrayTemp.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/fabricColorA" + "_" +timeid+ ".jpg")
    imageAArrayTemp.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/fabricTextureA" + "_" + timeid + ".jpg")
    imageAArrayTemp.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/fabricPartA" + "_" + timeid + ".jpg")



if __name__ == '__main__':
    # generateScarv("175,0,0,0,123,0", 2, "D:/20170602/PycharmProjects/firstDL_netEast/artgene/HD1-2G-2.bmp","15236879")
    generateScarv(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
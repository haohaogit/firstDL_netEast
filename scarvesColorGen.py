import math
# from PIL import Image
import numpy as np

import copy
import random
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


def generateScarv(content):
    params = []
    packs = []
    # packNum = 0
    C2 = [255, 0]
    C3 = [229, 127, 76]
    C4 = [229, 178, 127, 76]
    C5 = [229, 178, 127, 76, 25]
    C6 = [255, 229, 178, 127, 76, 25]
    C7 = [255, 229, 178, 127, 76, 51, 25]
    C8 = [229, 204, 178, 153, 127, 102, 76, 51]
    C9 = [229, 204, 178, 153, 127, 102, 76, 51, 25]
    C10 = [255, 229, 204, 178, 153, 127, 102, 76, 51, 25]

    A1 = [119, 0.44, 0.74, 89, 0.41, 0.30]
    A2 = [226, 0.58, 0.49, 194, 0.87, 0.77]
    A12 = [172.5, 0.51, 0.615, 141.5, 0.64, 0.535]
    A3 = [207, 0.49, 0.52, 109, 0.52, 0.49]
    A4 = [40, 0.68, 0.50, 115, 0.57, 0.44]
    A34 = [123.5, 0.585, 0.51, 112, 0.545, 0.465]
    A5 = [238, 0.33, 0.28, 110, 0.43, 0.35]
    A6 = [109, 0.72, 0.51, 181, 0.68, 0.55]
    A56 = [173.5, 0.525, 0.395, 145.5, 0.555, 0.45]
    # A7 = [128,0.49,0.72,31,0.123,0.45]
    # A8 = [226,0.58,0.49,77,0.194,0.87]
    # A78 = [177,0.535,0.605,54,0.1585,0.66]
    # content = var.get()
    # print content
    # print content,packNum,imageAName
    content = content.split(',')

    # packNum = varPacNum.get()
    packNum = int(content[3])
    if packNum == 0:
        return

    # imageAName = varName.get()

    # if imageAName == "":
    #	return
    # input = raw_input('input values:')
    # content = input.split(',')
    V12 = []
    V34 = []
    V56 = []
    V78 = []
    V = []
    Vtemp = 0
    for i in range(6):
        Vtemp = 0
        k = 0
        if int(content[0]) + 4 < 4:
            V12.append((-int(content[0])) / 3.0 * (A1[i] - A12[i]) + A12[i])
            if i == 0:
                Vtemp = Vtemp + (-int(content[0])) / 3.0 * random.randint(0, 360)
            else:
                Vtemp = Vtemp + (-int(content[0])) / 3.0 * (A1[i] - A12[i]) + A12[i]
            if int(content[0]) != 0:
                k = k + 1
        elif int(content[0]) + 4 >= 4:
            V12.append((int(content[0])) / 3.0 * (A2[i] - A12[i]) + A12[i])
            if i == 0:
                Vtemp = Vtemp + (int(content[0])) / 3.0 * random.randint(0, 360)
            # print Vtemp
            else:
                Vtemp = Vtemp + (int(content[0])) / 3.0 * (A2[i] - A12[i]) + A12[i]
            #if int(content[0]) != 0:
            k = k + 1
        if int(content[1]) + 4 < 4:
            V34.append((-int(content[1])) / 3.0 * (A3[i] - A34[i]) + A34[i])
            Vtemp = Vtemp + (-int(content[1])) / 3.0 * (A3[i] - A34[i]) + A34[i]
            if int(content[1]) != 0:
                k = k + 1
        elif int(content[1]) + 4 >= 4:
            V34.append((int(content[1])) / 3.0 * (A4[i] - A34[i]) + A34[i])
            Vtemp = Vtemp + (int(content[1])) / 3.0 * (A4[i] - A34[i]) + A34[i]
            #if int(content[1]) != 0:
            k = k + 1
        if int(content[2]) + 4 < 4:
            V56.append((-int(content[2])) / 3.0 * (A5[i] - A56[i]) + A56[i])
            if i == 0:
                Vtemp = Vtemp + (-int(content[2])) / 3.0 * random.randint(0, 360)
            else:
                Vtemp = Vtemp + (-int(content[2])) / 3.0 * (A5[i] - A56[i]) + A56[i]
            if int(content[2]) != 0:
                k = k + 1
        elif int(content[2]) + 4 >= 4:
            V56.append((int(content[2])) / 3.0 * (A6[i] - A56[i]) + A56[i])
            if i == 0:
                Vtemp = Vtemp + (int(content[2])) / 3.0 * random.randint(0, 360)
            else:
                Vtemp = Vtemp + (int(content[2])) / 3.0 * (A6[i] - A56[i]) + A56[i]
            #if int(content[2]) != 0:
            k = k + 1
        # print k

        V.append(Vtemp / float(k))

    colorNum = 7
    AddAMatchingFromACenter(params, packs, packNum, float(V[0]), float(V[1]), float(V[2]), float(V[3]), float(V[4]),
                            float(V[5]), 0)
    AddAMatchingFromACenter(params, packs, packNum, float(V[0]), float(V[1]), float(V[2]), float(V[3]), float(V[4]),
                            float(V[5]), 1)
    AddAMatchingFromACenter(params, packs, packNum, float(V[0]), float(V[1]), float(V[2]), float(V[3]), float(V[4]),
                            float(V[5]), 2)
    AddAMatchingFromACenter(params, packs, packNum, float(V[0]), float(V[1]), float(V[2]), float(V[3]), float(V[4]),
                            float(V[5]), 3)
    AddAMatchingFromACenter(params, packs, packNum, float(V[0]), float(V[1]), float(V[2]), float(V[3]), float(V[4]),
                            float(V[5]), 4)
    AddAMatchingFromACenter(params, packs, packNum, float(V[0]), float(V[1]), float(V[2]), float(V[3]), float(V[4]),
                            float(V[5]), 5)
    AddAMatchingFromACenter(params, packs, packNum, float(V[0]), float(V[1]), float(V[2]), float(V[3]), float(V[4]),
                            float(V[5]), 6)

    # centers = [];
    # center.h = 0;
    # center.s = 0;
    # center.l = 0.25;
    # AddAMatchingFromACenter(params,packs,5,0,0,0.25,0.3,2);
    # for pack in packs:
    #	for index in range(packNum):
    #		r,g,b = hsv2rgb(0, 0, 0.9)
    #		print pack[index].h, pack[index].s, pack[index].v
    #		print r,g,b
    # centers.append(center)

    pack = packs[0]
    pki = pack[0]
    # plt.imshow(imageA)
    # imageA.paste(imageC)
    # plt.show()
    rss = []
    gss = []
    bss = []
    for pack in packs:
        rs = []
        gs = []
        bs = []
        for index in range(packNum):
            r, g, b = hsv2rgb(pack[index].h, pack[index].s, pack[index].v)
            rs.append(r)
            gs.append(g)
            bs.append(b)
        # print pack[index].h, pack[index].s, pack[index].v
        # print r,g,b
        rss.append(rs)
        gss.append(gs)
        bss.append(bs)
    for j in range(colorNum):
        for i in range(packNum):
            print(str(int(rss[j][i])) + "," + str(int(gss[j][i])) + "," + str(int(bss[j][i])))
            # print(int(rss[j][i]),int(gss[j][i]),int(bss[j][i]))

if __name__ == '__main__':
	#generateScarv('0,1,0,4')
    generateScarv(sys.argv[1])
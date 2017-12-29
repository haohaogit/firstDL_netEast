# coding:utf-8
# from Tkinter import *
import copy
import random
# import matplotlib.pyplot as plt
import numpy as np
# from scipy import interpolate
from PIL import Image
import sys


def scan_line_seed(i, j, frame, r, g, b):
    stack = []
    return_value = 0
    if (frame[i, j, 0] <= 255 and frame[i, j, 0] >= 120) and (frame[i, j, 1] <= 255 and frame[i, j, 1] >= 120) and (
            frame[i, j, 2] <= 255 and frame[i, j, 2] >= 120):
        stack.append((i, j));
        while len(stack) != 0:
            seed = stack.pop()
            x, y = seed
            while (frame[x, y, 0] <= 255 and frame[x, y, 0] >= 120) and (
                    frame[x, y, 1] <= 255 and frame[x, y, 1] >= 120) and (
                    frame[x, y, 2] <= 255 and frame[x, y, 2] >= 120):
                frame[x, y, 0] = r
                frame[x, y, 1] = g
                frame[x, y, 2] = b
                # print x, y
                x += 1
            x_right = x - 1
            x, y = seed
            x -= 1
            while (frame[x, y, 0] <= 255 and frame[x, y, 0] >= 120) and (
                    frame[x, y, 1] <= 255 and frame[x, y, 1] >= 120) and (
                    frame[x, y, 2] <= 255 and frame[x, y, 2] >= 120):
                frame[x, y, 0] = r
                frame[x, y, 1] = g
                frame[x, y, 2] = b
                # print x, y
                x -= 1
            x_left = x + 1
            # 如果左右端点为空则加入种子点
            if (frame[x_left, y - 1, 0] <= 255 and frame[x_left, y - 1, 0] >= 120) and (
                    frame[x_left, y - 1, 1] <= 255 and frame[x_left, y - 1, 1] >= 120) and (
                    frame[x_left, y - 1, 2] <= 255 and frame[x_left, y - 1, 2] >= 120):
                stack.append((x_left, y - 1))
            if (frame[x_left, y + 1, 0] <= 255 and frame[x_left, y + 1, 0] >= 120) and (
                    frame[x_left, y + 1, 1] <= 255 and frame[x_left, y + 1, 1] >= 120) and (
                    frame[x_left, y + 1, 2] <= 255 and frame[x_left, y + 1, 2] >= 120):
                stack.append((x_left, y + 1))
            if (frame[x_right, y - 1, 0] <= 255 and frame[x_right, y - 1, 0] >= 120) and (
                    frame[x_right, y - 1, 1] <= 255 and frame[x_right, y - 1, 1] >= 120) and (
                    frame[x_right, y - 1, 2] <= 255 and frame[x_right, y - 1, 2] >= 120):
                stack.append((x_right, y - 1))
            if (frame[x_right, y + 1, 0] <= 255 and frame[x_right, y + 1, 0] >= 120) and (
                    frame[x_right, y + 1, 1] <= 255 and frame[x_right, y + 1, 1] >= 120) and (
                    frame[x_right, y + 1, 2] <= 255 and frame[x_right, y + 1, 2] >= 120):
                stack.append((x_right, y + 1))
            for x in range(x_left, x_right + 1):
                # 上左
                if ((frame[x, y - 1, 0] <= 255 and frame[x, y - 1, 0] >= 120) and (
                        frame[x, y - 1, 1] <= 255 and frame[x, y - 1, 1] >= 120) and (
                        frame[x, y - 1, 2] <= 255 and frame[x, y - 1, 2] >= 120)) and (
                            frame[x - 1, y - 1, 0] <= 230 | frame[x - 1, y - 1, 1] <= 230 | frame[
                            x - 1, y - 1, 2] <= 230):
                    stack.append((x, y - 1))
                # 下左
                if ((frame[x, y + 1, 0] <= 255 and frame[x, y + 1, 0] >= 120) and (
                        frame[x, y + 1, 1] <= 255 and frame[x, y + 1, 1] >= 120) and (
                        frame[x, y + 1, 2] <= 255 and frame[x, y + 1, 2] >= 120)) and (
                            frame[x - 1, y + 1, 0] <= 230 | frame[x - 1, y + 1, 1] <= 230 | frame[
                            x - 1, y + 1, 2] <= 230):
                    stack.append((x, y + 1))
                # 上右
                if ((frame[x - 1, y - 1, 0] <= 255 and frame[x - 1, y - 1, 0] >= 120) and (
                        frame[x - 1, y - 1, 1] <= 255 and frame[x - 1, y - 1, 1] >= 120) and (
                        frame[x - 1, y - 1, 2] <= 255 and frame[x - 1, y - 1, 2] >= 120)) and (
                            frame[x, y - 1, 0] <= 120 or frame[x, y - 1, 1] <= 120 or frame[x, y - 1, 2] <= 120):
                    stack.append((x - 1, y - 1))
                # 下右
                if ((frame[x - 1, y + 1, 0] <= 255 and frame[x - 1, y + 1, 0] >= 120) and (
                        frame[x - 1, y + 1, 1] <= 255 and frame[x - 1, y + 1, 1] >= 120) and (
                        frame[x - 1, y + 1, 2] <= 255 and frame[x - 1, y + 1, 2] >= 120)) and (
                            frame[x, y + 1, 0] <= 120 or frame[x, y + 1, 1] <= 120 or frame[x, y + 1, 2] <= 120):
                    stack.append((x - 1, y + 1))

        return_value = 1
    return frame


def goblet(filename, rgb, saveTime):
    rgb = rgb.split(',')
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])
    imagegaojiaobei = Image.open(filename)
    imagegaojiaobeiArray = np.array(imagegaojiaobei)
    rows, cols, dims = imagegaojiaobeiArray.shape
    first = 0
    print(rows, cols)
    # imagegaojiaobeiArray = scan_line_seed(rows/2, cols/2, imagegaojiaobeiArray,100,100,110)
    rangev = 40
    rcolor = 240
    gcolor = 0
    bcolor = 255
    for x in range(rows):
        num = 0
        for y in range(cols):
            # print first,imagegaojiaobeiArray[x, y, 0],imagegaojiaobeiArray[x, y, 1],imagegaojiaobeiArray[x, y, 2]
            if first == 0:
                value = (imagegaojiaobeiArray[x, y, 0] <= rcolor + rangev and imagegaojiaobeiArray[
                    x, y, 0] >= rcolor - rangev) and (
                        imagegaojiaobeiArray[x, y, 1] <= gcolor + rangev and imagegaojiaobeiArray[
                            x, y, 1] >= gcolor) and (
                        imagegaojiaobeiArray[x, y, 2] <= bcolor and imagegaojiaobeiArray[x, y, 2] >= bcolor - rangev)
                if value == True:
                    first = 1
                    # print first
            elif first == 1:
                value = (imagegaojiaobeiArray[x, y, 0] <= rcolor + rangev and imagegaojiaobeiArray[
                    x, y, 0] >= rcolor - rangev) and (
                        imagegaojiaobeiArray[x, y, 1] <= gcolor + rangev and imagegaojiaobeiArray[
                            x, y, 1] >= gcolor) and (
                        imagegaojiaobeiArray[x, y, 2] <= bcolor and imagegaojiaobeiArray[x, y, 2] >= bcolor - rangev)
                if value == False:
                    first = 2
                    imagegaojiaobeiArray[x, y, 0] = r
                    imagegaojiaobeiArray[x, y, 1] = g
                    imagegaojiaobeiArray[x, y, 2] = b
                    # print 33
                else:
                    num = num + 1
                    if num >= 10:
                        first = 0
                        break
            elif first == 2:
                value = (imagegaojiaobeiArray[x, y, 0] <= rcolor + rangev and imagegaojiaobeiArray[
                    x, y, 0] >= rcolor - rangev) and (
                        imagegaojiaobeiArray[x, y, 1] <= gcolor + rangev and imagegaojiaobeiArray[
                            x, y, 1] >= gcolor) and (
                        imagegaojiaobeiArray[x, y, 2] <= bcolor and imagegaojiaobeiArray[x, y, 2] >= bcolor - rangev)
                if value == False:
                    imagegaojiaobeiArray[x, y, 0] = r
                    imagegaojiaobeiArray[x, y, 1] = g
                    imagegaojiaobeiArray[x, y, 2] = b
                # print imagegaojiaobeiArray[x, y, 0]
                # print 38
                # value = (imagegaojiaobeiArray[x, y, 0] <= rcolor+rangev and imagegaojiaobeiArray[x, y, 0] >= rcolor-rangev) and (imagegaojiaobeiArray[x, y, 1] <= gcolor+rangev and imagegaojiaobeiArray[x, y, 1] >= gcolor) and (imagegaojiaobeiArray[x, y, 2] <= bcolor and imagegaojiaobeiArray[x, y, 2] >= bcolor-rangev)
                elif value == True:
                    first = 0
                    break
    images = Image.fromarray(imagegaojiaobeiArray)

    images.save("C:\\apache-tomcat-7.0.53\\wtpwebapps\\art0804\\image\\gaojiaobeiColorA_"+saveTime+".jpg")
    images.save("C:\\apache-tomcat-7.0.53\\wtpwebapps\\art0804\\image\\gaojiaobeiTextureA_" + saveTime + ".jpg")
    images.save("C:\\apache-tomcat-7.0.53\\wtpwebapps\\art0804\\image\\gaojiaobeiPartA_" + saveTime + ".jpg")

if __name__ == '__main__':
    # goblet("gaojiaobei_45411.jpg","33,55,112","64384")
    goblet(sys.argv[1],sys.argv[2],sys.argv[3])

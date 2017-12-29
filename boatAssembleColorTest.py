#coding:utf-8
# from Tkinter import *
import math
from PIL import Image
# import matplotlib.pyplot as plt
import numpy as np
import sys

def boatAssemble(content,rgb,timeid):
    print(content)
    print(rgb)
    print(timeid)
    content = content.split(",")
    minitemA = content[0]
    minitemB = content[1]
    minitemC = content[2]
    minitemD = content[3]

    rgb = rgb.split(',')
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])

    A = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
    B = ['B1', 'B2', 'B3']
    C = ['C1', 'C2', 'C3']
    D = ['D1', 'D2']

    print(minitemD)
    if minitemD == "D1":
        boat = Image.new('RGBA', (1173,1024),'white')					
        imageA = Image.open("C:/firstDL_netEast/D1/" + minitemA + '.png')
        imageB = Image.open("C:/firstDL_netEast/D1/" + minitemB + '.png')
        imageC = Image.open("C:/firstDL_netEast/D1/" + minitemC + '.png')
        print(minitemD)
    else:
        boat = Image.new('RGBA', (1173,1024),'white')					
        imageA = Image.open("C:/firstDL_netEast/D2/" + minitemA + '.png')
        imageB = Image.open("C:/firstDL_netEast/D2/" + minitemB + '.png')
        imageC = Image.open("C:/firstDL_netEast/D2/" + minitemC + '.png')

    #boat = Image.new('RGBA', (1000,1000),'white')
    #imageA = Image.open(minitemA + '.png')
    #imageB = Image.open(minitemB + '.png')
    #imageC = Image.open(minitemC + '.png')
	
    #imageA = Image.open('D3' + '.png')
    #imageB = Image.open('B2' + '.png')
    #imageC = Image.open('C2' + '.png')
	
	#imageDMask = Image.open('maskboardD1RGB229.229.229' + '.jpg')
    #imgaecaizhi = Image.open('M22' + '.jpg')
    if minitemD == "D1":
        imageDMask = Image.open("C:/firstDL_netEast/D1/" + minitemA + "_mask.png")
    else:
        #imgaecaizhi = imgaecaizhi.resize((1800, 1000))
        imageDMask = imageDMask = Image.open("C:/firstDL_netEast/D2/" + minitemA + "_mask.png")
    #imgaelogo = Image.open('LOGO4' + '.png')
    print("C:/firstDL_netEast/D2/"+minitemA+"_mask.png")
    imageDMaskArray = np.array(imageDMask)
    rows,cols,dims = imageDMaskArray.shape
    print(rows,cols,dims)
    pix = imageDMask.load()
    for x in range(cols):
        for y in range(rows):
            rs,gs,bs,a = pix[x,y]
            if rs == 229 and gs == 229 and bs == 229:
                pix[x,y] = (r,g,b,a)
                #print pix[x,y]
                #print imageDMaskArray[x,y:].all()
    # plt.imshow(imageDMaskArray)
    #imgBlend = Image.blend(imageDMask, imgaecaizhi, 0.7)
    imgBlend = imageDMask
	
	
    print (minitemA, minitemB,minitemC,minitemD)
    r,g,b,a = imageB.split()
    boat.paste(imageB, (0,0), mask = a)
    if minitemC != 'C3':
        r,g,b,a = imageC.split()
        boat.paste(imageC, (0,0), mask = a)
    r,g,b,a = imgBlend.split()
    boat.paste(imgBlend, (0,0), mask = a)

    box = (0, 200, 1173, 852)
    boat=boat.crop(box)
    boat.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/boatColorA_" + timeid + ".jpg")
    boat.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/boatTextureA_" + timeid + ".jpg")
    boat.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/boatPartA_" + timeid + ".jpg")

    # plt.xlabel(minitemA+' '+minitemB+' '+minitemC+' '+minitemD, fontproperties='SimHei')
    # plt.imshow(boat)
    # #imageA.paste(imageC)
    # plt.show()

if __name__ == '__main__':
    # boatAssemble("A4,B3,C2,D1","255,255,255","1111111")
    boatAssemble(sys.argv[1],sys.argv[2],sys.argv[3])
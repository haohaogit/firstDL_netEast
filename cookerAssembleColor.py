import sys
import math
from PIL import Image
import numpy as np


def cookerAssembleColor(content,rgb,timeid):
    # minitemS = sys.argv[1]
    # minitemK = sys.argv[2]
    # minitemB = sys.argv[3]
    # minitemD = sys.argv[4]
    content = content.split(",")
    minitemS = content[0]
    minitemK = content[1]
    minitemB = content[2]
    minitemD = content[3]
    print("crgb222 "+rgb)
    rgb = rgb.split(',')
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])

    print(minitemS)
    print(minitemK)
    print(minitemB)
    print(minitemD)
    print(rgb[0])
    print(rgb[1])
    print(rgb[2])

    if minitemD == "D1":
        boat = Image.new('RGBA', (1625,1000),'white')					
        imageA = Image.open("C:/firstDL_netEast/artgene/D1/" + minitemS + '.png')
        imageB = Image.open("C:/firstDL_netEast/artgene/D1/" + minitemK + '.png')
        imageC = Image.open("C:/firstDL_netEast/artgene/D1/" + minitemB + '.png')
        #print minitemD
    else:
        boat = Image.new('RGBA', (1800,1000),'white')					
        imageA = Image.open("C:/firstDL_netEast/artgene/D2/" + minitemS + '.png')
        imageB = Image.open("C:/firstDL_netEast/artgene/D2/" + minitemK + '.png')
        imageC = Image.open("C:/firstDL_netEast/artgene/D2/" + minitemB + '.png')
	
    #imageA = Image.open('A2' + '.png')
    #imageB = Image.open('K3' + '.png')
    #imageC = Image.open('C1' + '.png')
    imgaecaizhi = Image.open('C:/firstDL_netEast/artgene/M22' + '.jpg')
    imageDMask = Image.open('C:/firstDL_netEast/artgene/maskboardD1RGB229.229.229' + '.png')
    if minitemD == "D1":
        imgaecaizhi = imgaecaizhi.resize((1652, 1000))
        imageDMask = imageDMask.resize((1652, 1000))
    else:
        imgaecaizhi = imgaecaizhi.resize((1800, 1000))
        imageDMask = imageDMask.resize((1800, 1000))

    imgaelogo = Image.open('C:/firstDL_netEast/artgene/LOGO4' + '.png')

    # print imageDMask.size, imgaecaizhi.size
    # print minitemS, minitemK,minitemB,minitemD

    imageDMaskArray = np.array(imageDMask)
    rows, cols, dims = imageDMaskArray.shape
    print(rows, cols, dims)
    pix = imageDMask.load()
    for x in range(cols):
        for y in range(rows):
            rs, gs, bs, ass = pix[x, y]
            if rs in range(229 - 5, 229 + 5):
                pix[x, y] = (r, g, b, ass)
                #print pix[x,y]
                #print imageDMaskArray[x,y:].all()
    #plt.imshow(imageDMaskArray)
    #imgBlend = Image.blend(imageDMask, imgaecaizhi, 0.7)
    imgBlend = imageDMask
    r,g,b,a = imageC.split()
    #boat.paste(imgBlend, (0,0))
    #boat.paste(imageC, (0,0), mask = a)
    r,g,b,a = imageA.split()
    imgBlend.paste(imageA, (0,0), mask = a)
    r,g,b,a = imageB.split()
    imgBlend.paste(imageB, (0,0), mask = a)
    r,g,b,a = imgaelogo.split()
    imgBlend.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/cookerColorA_"+timeid+".jpg")
    imgBlend.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/cookerTextureA_"+timeid+".jpg")
    imgBlend.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/cookerPartA_"+timeid+".jpg")
	#boat.paste(imgaelogo, (0,0), mask = a)
    #return minitemS,minitemK,minitemB,minitemD
    #imageA.paste(imageC)
    #plt.show()	
if __name__ == '__main__':
    # print("aaaaaaaaaa")
    # print(sys.argv[0])
    cookerAssembleColor(sys.argv[1],sys.argv[2],sys.argv[3])
    # cookerAssembleColor("A5,B1,C2,D2","110,110,110","1111")

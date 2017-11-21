#coding:utf-8
# from Tkinter import *
import math
from PIL import Image
# import matplotlib.pyplot as plt
import sys
# print(sys.argv[1])
# print(sys.argv[2])


def boatAssemble(content,timeid):
    print(content)
    print(timeid)
    s1u = {'A1':-0.221, 'A2':-0.121, 'A3':0.266, 'A4':0.116, 'A5':-0.181, 'A6':0.142, \
	      'B1':0.110, 'B2':-0.209, 'B3':0.1, 'C1':-0.716, 'C2':0.056, 'C3':0.66, 'D1':0.074, 'D2':-0.074}
    s1q = {'A':0.20901, 'B':0.13696, 'C':0.59078, 'D':0.06323}
    s1c = -0.4
	
    s2u = {'A1':-0.083, 'A2':0.064, 'A3':0.010, 'A4':0.049, 'A5':-0.071, 'A6':0.032, \
	      'B1':-0.019, 'B2':-0.083, 'B3':0.102, 'C1':-0.983, 'C2':0.062, 'C3':0.921, 'D1':0.127, 'D2':-0.127}
    s2q = {'A':0.05894, 'B':0.07412, 'C':0.7649, 'D':0.10203}
    s2c = -0.218
	
    s3u = {'A1':-0.011, 'A2':-0.092, 'A3':0.113, 'A4':-0.049, 'A5':0.161, 'A6':-0.122, \
	      'B1':0.088, 'B2':0.029, 'B3':-0.117, 'C1':0.766, 'C2':-0.003, 'C3':-0.762, 'D1':0.073, 'D2':-0.073}
    s3q = {'A':0.13104, 'B':0.09455, 'C':0.70658, 'D':0.06783}
    s3c = -0.402
	
    s4u = {'A1':0.101, 'A2':0.308, 'A3':-0.248, 'A4':-0.513, 'A5':0.418, 'A6':-0.066, \
	      'B1':-0.065, 'B2':0.15, 'B3':-0.085, 'C1':0.249, 'C2':-0.009, 'C3':-0.239, 'D1':-0.121, 'D2':0.121}
    s4q = {'A':0.4912, 'B':0.12383, 'C':0.25763, 'D':0.12735}
    s4c = 0.223
	
    s5u = {'A1':-0.054, 'A2':0.099, 'A3':0.014, 'A4':-0.219, 'A5':0.154, 'A6':0.004, \
	      'B1':0.046, 'B2':-0.1, 'B3':0.054, 'C1':-0.182, 'C2':-0.007, 'C3':0.189, 'D1':0.128, 'D2':-0.128}
    s5q = {'A':0.32354, 'B':0.13385, 'C':0.32162, 'D':0.22099}
    s5c = -0.76
	
    s6u = {'A1':-0.073, 'A2':-0.049, 'A3':0.103, 'A4':-0.113, 'A5':0.238, 'A6':-0.106, \
	      'B1':0.025, 'B2':0.064, 'B3':-0.089, 'C1':0.726, 'C2':-0.03, 'C3':-0.696, 'D1':-0.158, 'D2':0.158}
    s6q = {'A':0.15613, 'B':0.0684, 'C':0.63445, 'D':0.14102}
    s6c = 0.012
    A = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
    B = ['B1', 'B2', 'B3']
    C = ['C1', 'C2', 'C3']
    D = ['D1', 'D2']
    #print 'dsfsdfs'
    #input = raw_input('input values:')
    #print content
    content = content.split(',')
    #print content
    minValue = -1
    minitemA = 0
    minitemB = 0
    minitemC = 0
    minitemD = 0
    for itemA in A:
        for itemB in B:
            for itemC in C:
                for itemD in D:
                    s1 = s1u[itemA] * s1q['A'] + s1u[itemB] * s1q['B'] + s1u[itemC] * s1q['C'] + s1u[itemD] * s1q['D'] + s1c
                    s2 = s2u[itemA] * s2q['A'] + s2u[itemB] * s2q['B'] + s2u[itemC] * s2q['C'] + s2u[itemD] * s2q['D'] + s2c
                    s3 = s3u[itemA] * s3q['A'] + s3u[itemB] * s3q['B'] + s3u[itemC] * s3q['C'] + s3u[itemD] * s3q['D'] + s3c
                    s4 = s4u[itemA] * s4q['A'] + s4u[itemB] * s4q['B'] + s4u[itemC] * s4q['C'] + s4u[itemD] * s4q['D'] + s4c
                    s5 = s5u[itemA] * s5q['A'] + s5u[itemB] * s5q['B'] + s5u[itemC] * s5q['C'] + s5u[itemD] * s5q['D'] + s5c
                    s6 = s6u[itemA] * s6q['A'] + s6u[itemB] * s6q['B'] + s6u[itemC] * s6q['C'] + s6u[itemD] * s6q['D'] + s6c
                    value = math.sqrt((s1-float(content[0]))*(s1-float(content[0])) + (s2-float(content[1]))*(s2-float(content[1])) \
					+ (s3-float(content[2]))*(s3-float(content[2])) + (s4-float(content[3]))*(s4-float(content[3])) + (s5-float(content[4]))*(s5-float(content[4])) \
					+ (s6-float(content[5]))*(s6-float(content[5])))
                    if minValue == -1 or minValue > value:
                        minValue = value
                        minitemA = itemA
                        minitemB = itemB
                        minitemC = itemC
                        minitemD = itemD
    #print minitemD

    if minitemD == "D1":
        boat = Image.new('RGBA', (1173,1024),'white')					
        imageA = Image.open("C:/firstDL_netEast/D1/" + minitemA + '.png')
        imageB = Image.open("C:/firstDL_netEast/D1/" + minitemB + '.png')
        imageC = Image.open("C:/firstDL_netEast/D1/" + minitemC + '.png')
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
	
    print(minitemA+","+minitemB+","+minitemC+","+minitemD)

    r,g,b,a = imageB.split()
    boat.paste(imageB, (0,0), mask = a)
    if minitemC != 'C3':
        r,g,b,a = imageC.split()
        boat.paste(imageC, (0,0), mask = a)
    r,g,b,a = imageA.split()
    boat.paste(imageA, (0,0), mask = a)
    boat.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/boat_" + timeid + ".jpg")
    boat.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/boatColor_" + timeid + ".jpg")
    boat.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/boatTexture_" + timeid + ".jpg")
    boat.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/boatPart_" + timeid + ".jpg")

    boat.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/boatColorA_" + timeid + ".jpg")
    boat.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/boatTextureA_" + timeid + ".jpg")
    boat.save("C:/apache-tomcat-7.0.53/wtpwebapps/art0804/image/boatPartA_" + timeid + ".jpg")

    '''
    plt.xlabel(minitemA+' '+minitemB+' '+minitemC+' '+minitemD, fontproperties='SimHei')
    plt.imshow(boat)
    #imageA.paste(imageC)
    plt.show()
    '''

if __name__ == '__main__':
    # boatAssemble("-1,-1,-1,-1,-1,1","111111111111111")
    boatAssemble(sys.argv[1],sys.argv[2])


from PIL import ImageGrab
import sys
print("脚本名：", sys.argv[0])
img = ImageGrab.grab()
# img.show()
img.save("4.png")
print("this is ahaha")
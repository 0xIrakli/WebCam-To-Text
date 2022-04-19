from PIL import Image
import time
import cv2
import os

string = ''
char = "._-~+=?08$%&#"
CAMERA_NUMBER = int(open('config.txt', 'r').read())
cap = cv2.VideoCapture(CAMERA_NUMBER)
char_len = len(char)
threshhold = 255/char_len
while True:
    rval, frame = cap.read()
    i = Image.fromarray(frame)#cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    i = i.resize((190, 59))
    for y in range(i.height):
        for x in range(i.width):
            #pixel = i.getpixel((x, y))
            p = sum(i.getpixel((x, y))) / 3
            for j in range(char_len):
                if p <= (j+1)*threshhold and p > j*threshhold:
                    string += char[j]
        string += '\n'
    print(string)
    string = ''
    #os.system('cls')

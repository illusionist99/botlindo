import cv2
import pyautogui
import time 
import keyboard


seed = cv2.imread('seed.png', 0)
bird = cv2.imread('bird_00.png', 0)


test = cv2.imread('rename.png', 0)
inv = cv2.imread('inventory.png', 0)
test0 = cv2.imread('action.png', 0)

fofo = cv2.imread('feed.png', 0)

findfofo = cv2.imread('findfofo.png', 0)

act = cv2.imread('action_.png', 0)

bigone = cv2.imread('bigone.png', 0)

confirm = cv2.imread('confirm.png', 0)

def getScreenState(filename):
    
    time.sleep(2)
    image = pyautogui.screenshot(filename)

    return image

def detect_object(needle , haystack, color):
    imageGray = needle
    templateGray = haystack

    result = cv2.matchTemplate(imageGray, templateGray,
        cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

    (startX, startY) = maxLoc
    print(startX ,startY)
    endX = startX  + imageGray.shape[1]
    endY = startY  + imageGray.shape[0]

    #cv2.rectangle(haystack, (startX , startY ), (endX, endY), color, 3)


#def feed():


#def connectPlayer():


color = (255, 255, 255)
color1 = (100, 100, 100)


#detect_object(bird, test, color1)
#detect_object(seed, test, color)
#detect_object(confirm, bigone, color)
#getScreenState('form.png')
#keyboard.send("echap")

#image = cv2.imread('action.png')
# show the output image
#cv2.imshow("Output", bigone)
#cv2.waitKey(0)

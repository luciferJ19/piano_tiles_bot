import mss
import numpy
import cv2
import pyautogui
import keyboard

def grabFrame(region):
    with mss.mss() as sct:
        screen = numpy.array(sct.grab(region))
        screenGrayscale = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        #cv2.imwrite("ags.png", screen)
    return screenGrayscale

def detectTile(frame):
    #print(frame.shape)
    for y in range(frame.shape[0]):
        for x in range(frame.shape[1]):
            if (frame[y,x] == 0):
                bool = True
                #print(x)
                #print(y)
                return x,y

region = {"top":99, "height":2, "left":int(0.4*pyautogui.size()[0]),
              "width":int(0.25*pyautogui.size()[0])}
coords = []
#run the game in fullscreen mode
if __name__ == "__main__":
    pyautogui.PAUSE = 0.005
    pyautogui.sleep(2)

    while True:
        if keyboard.is_pressed("q"):
            break
        f = grabFrame(region)
        coords = detectTile(f)

        if coords:
            target_x = coords[0] + region["left"] + 1
            target_y = coords[1] + region["top"] + 1
            #print(pyautogui.position())
            pyautogui.moveTo(x=target_x, y=target_y)
            pyautogui.mouseDown()

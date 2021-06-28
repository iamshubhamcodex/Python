from openEverything import openEv
import time
import pyautogui
import datetime

def ScreenShot():
    file_path  = "E:\\Coding\\Python\\Programmes\\Jarvis\\Screenshot\\" + str(datetime.now()).split(".")[0] + ".png"
    time.sleep(5)
    _ = pyautogui.screenshot(file_path).show()
    b = input("Wanna Open Folder [Y & N]\t").lower()
    if b == "y":
        openEv(file_path.replace(str(datetime.now()).split(".")[0] + ".png",""), 2, "Opening Screen Shot....")

if __name__ == "__main__":
    ScreenShot()
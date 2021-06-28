from pyttsx3 import speak
import webbrowser
import os

def openEv(addr, id, toSpeak):
    speak(toSpeak)
    if id == 1:
        get_url = input("Want to Get URL [Y]\t").lower()
        if get_url == "y":
            print(addr)
        else:
            webbrowser.open(addr)
    elif id == 2:
        os.startfile(addr)
    elif id == 3:
        if toSpeak == "":
            addr()
        else:
            speak(toSpeak)
            addr()
        while True:
            if input("Want to Continue[Y]\t").lower() == "y":
                addr()
            else:
                break


if __name__ == "__main__":
    # openEv()
    pass
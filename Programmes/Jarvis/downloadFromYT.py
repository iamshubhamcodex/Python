from openEverything import openEv
from pytube import YouTube  as YT
from pyttsx3 import speak


def downloadYT():
    print(YT (input("Enter Link to be downloaded....\t")).title)
    ys = YT (input("Enter Link to be downloaded....\t")).streams.get_by_resolution("360p")
    speak("downloading...")
    ys.download("E:\\Coding\\Python\\Programmes\\Jarvis\\YT Downloads\\")
    speak("downloaded")
    if input("Wanna Open Folder [Y & N]").lower() == "y":
        openEv("E:\\Coding\\Python\\Programmes\\Jarvis\\YT Downloads\\", 2, "Opening YT Downloads....")

if __name__ =="__main__":
    downloadYT()
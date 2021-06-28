import os
import wishMe
import random
import playGame
import requests
import noToWord
import playGame
import wikipedia
import webbrowser
# import time
# import pyautogui as pg
# import speech_recognition as sr

from pyttsx3 import speak
from openEverything import openEv
from sendWhatMsg import sendWhatsapp
from takeScreenShot import ScreenShot
from downloadFromYT import downloadYT
from monthlyMoneyCalc import totalMoney
# from datetime import datetime
# from plyer import notification
# from pytube import YouTube


def ask():
    try:
        while True:
            query = input("\nEnter your Search\t").lower()

            if 'screenshot' in query:
                openEv(ScreenShot, 3, "Just about to take SCREENSHOT in 5 seconds")
            elif 'pokemon' in query:
                import pokemonDex 
                openEv(pokemonDex.call, 3, "Opening Pokedex....")
            elif 'o images' in query:
                openEv("C:\\Users\\dell laptop\\Pictures", 2, "Opening Images....")
            elif 'o videos' in query:
                openEv("C:\\Users\\dell laptop\\Videos", 2, "Opening Music....")
            elif 'o downloads' in query:
                openEv("C:\\Users\\dell laptop\\Downloads", 2, "Opening Download....")
            elif 'o ld c' in query:
                openEv("C:\\", 2, "Opening Local Disk(C)....")
            elif 'o ld e' in query:
                speak()
                openEv("E:\\", 2, "Opening Study(E)....")
            elif 'o ld d' in query:
                speak()
                openEv("D:\\", 2, "Opening Local Disk(C)....")
            elif 'o documents' in query:
                speak()
                openEv("C:\\Users\\dell laptop\\Documents", 2, "Opening Documents....")
            elif 'o music' in query:
                speak()
                openEv("C:\\Users\\dell laptop\\Music", 2, "Opening Music....")
            elif 'qqq' in query:
                break
            elif 'play game' in query:
                openEv(playGame.playG, 3, "Opening Game....")
            elif 'calc total m' in query:
                openEv(totalMoney, 3, "Opening....")
            elif 'to word' in query:
                openEv(noToWord.UserInp, 3, "Opeing Number to Word Converter...")
            elif 'play music' in query:
                songs = os.listdir("C:\\Users\\dell laptop\\Music")
                randomNo = random.randint(4, len(songs)-1)
                openEv(os.path.join("C:\\Users\\dell laptop\\Music", songs[randomNo]), 2, "Playing Music....")
            else:
                try:
                    request = requests.get("https://www.google.com", timeout=1)
                    if 'send whatsapp' in query:
                        openEv(sendWhatsapp, 3, "")
                        while True:
                            inp = input("Want to Continue[Y]\t").lower()
                            if inp == "y":
                                sendWhatsapp()
                            else:
                                break
                    elif 'download yt' in query:
                        openEv(downloadYT, 3, "")
                    elif 'swikipedia' in query:
                        speak("According to Wikipedia:\n" + wikipedia.summary(query.replace("swikipedia ", ""), sentences=3))
                    elif 'o youtube' in query:
                        openEv("youtube.com", 1, "Opening Youtube")
                    elif 'o gmail' in query:
                        openEv("gmail.com", 1, "Opening Gmail")
                    elif 'syoutube' in query:
                        openEv("https://www.youtube.com/results?search_query=" + query.replace("syoutube ", ""), 1, "Searching Youtube.....")
                    elif 'direction' in query:
                        openEv("https://www.google.com/maps/dir/" + input("From:\t") + "/" + input("To:\t"), 1,"Getting Direction......")
                    elif 'o google account' in query:
                        openEv("https://myaccount.google.com/", 1,"Opeing Your Google Account")
                    elif 'o yt liked videos' in query:
                        openEv("youtube.com/playlist?list=LL", 1,"Opeing Your YT Liked Videos")
                    elif 'o yt history' in query:
                        openEv("youtube.com/feed/history", 1,"Opening Your YT History")
                    elif 'o yt library' in query:
                        openEv("youtube.com/feed/library", 1,"Opening Your YT Library")
                    elif 'o yt watch later' in query:
                        openEv("youtube.com/playlist?lis=WL", 1,"Opening Your YT Watch Later")
                    elif 'o yt subscription' in query:
                        openEv("youtube.com/feed/subscription", 1,"Opening Your YT Subscirption")
                    elif 'sw3 school' in query:
                        openEv("https://www.w3schools.com/" + query.replace("sw3 school ", ""), 1,"Searching W3 School.....")
                    elif 'apni kaksha' in query:
                        openEv("https://www.youtube.com/channel/UCF7BExjT2zH_mmyqOB139Dg", 1,"Opening Apni Kaksha")
                    elif 'aman dhattarwal' in query:
                        openEv("https://www.youtube.com/channel/UCmXZxX_qexEZxhb5_vQKPCw", 1,"Opening Aman Dhattarwal")
                    elif 'sgoogle' in query:
                        openEv("https://www.google.com/search?q=" + query.replace("sgoogle ", ""), 1,"Searching Google.....")
                    elif 'smap' in query:
                        openEv("https://www.google.com/maps/search/" + query.replace("smap ", ""), 1, "Searching on Maps.....")
                    elif 'simages' in query:
                        openEv("https://www.google.com/search?q=" + query.replace("simages ","") + "&tbm=isch", 1, "Searching Images on Google.....")
                    elif 'svideos' in query:
                        openEv("https://www.google.com/search?=" + query.replace("svideos ","") + "&tbm=vid", 1, "Searching Videos on Google.....")
                    else:
                        user_input = input(
                            f"Wannna Search on Google ['{query}'] ")
                        if user_input == "y":
                            speak("Searching Google")
                            openEv("https://www.google.com/search?q=" % query)
                except Exception as e:
                    print(f"You are having some error LIKE\n {e}")
    except Exception as e:
        speak(f"You are having error LIKE\n {e}")
        ask()

if __name__ == "__main__":
    wishMe.wishMe()
    ask()

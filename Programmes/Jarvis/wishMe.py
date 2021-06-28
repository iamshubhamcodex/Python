from datetime import datetime
from pyttsx3 import speak

def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak(f"Good Morning")
    elif hour >= 12 and hour < 16:
        speak(f"Good Afternoon")
    elif hour >= 16 and hour < 20:
        speak(f"Good Evening")
    else:
        speak(f"Good Night")

if __name__ == "__main__":
    wishMe()
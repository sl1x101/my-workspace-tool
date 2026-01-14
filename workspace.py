import webbrowser
import os
import time

urls =[
        "https://www.google.com/",
        "https://pomofocus.io/",
        "https://open.spotify.com/"
    ]

#openweb 
def openWeb():
    for url in urls :
        print("Open Web....")
        webbrowser.open(url)
        time.sleep(1)
        
#open app
def openApp():
    print("open app...")
    try:
        os.startfile("notepad.exe")
        time.sleep(1)
    except Exception as e:
        print(f"Error:{e}")
        
if __name__ == "__main__":
    print("Starting your Workspace...")
    openWeb()
    openApp()
    print("Redy!..")
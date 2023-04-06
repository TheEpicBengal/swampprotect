import time
import pyautogui

  
while True:
        print("Auto Protecting soon....")
        time.sleep(20)
        pyautogui.press('-') # You can choose your own key or type bind - "say /protect" in gmod console
        print("Protection Activated, Time until next protection sequence countdown:")
        for i in range(4):
                t = (1150)
        while t: 
                mins = t // 60 
                secs = t % 60
                timer = '{:02d}:{:02d}'.format(mins, secs) 
                print(timer, end="\r")-
                time.sleep(1)
                t -= 1  

from pyautogui import hotkey
from subprocess import call
from time import sleep
call(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
sleep(0.500) #You need to increase it if your hardware is slower
hotkey("ctrl", "shift", "n")
# Method One - PyAutoGui

A alternative (but slower and less efficient of subprocess) is **pyautogui**

You just need to import it (only the **.hotkey** if needed) and insert the .exe of your browser, examples:
> obs: you need to download it before import (pip install pyautogui)

#####Better PyAutoGui run:

The PyAutoGui is very good for the most cases, but there is a necessity of use time.sleep to fix problems of delay (hardware or software limitation) to everything works (example, the browser is slow to open or the python is glitching the code)

##### Importing:
- import pyautogui	 (entire module)
- from pyautogui import hotkey	 (.call function)

##### Browser Path (example):
- "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

To finish the code, we need to start the browser and use the hotkey (ctrl+shift+n) to start the incognito mode.

##### Opening The Browser:

The problem of usig the PyAutoGui is the difficulty of opening manually the browser (ex: search the browser in OS Search or clicking on it at the taskbar). So, we should use the subprocess to get a faster and more efficient program, example:
```python
from subprocess import call
call(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
```

##### Incognito Mode:

To open in Incogito Mode, we just need to run the hotkey (ctrl+shift+n)
> obs: I think every browser use the ctrl+shift+n to open it, but if your browser has different hotkey, just change the keys name in .hotkey

#### The Entire Code Result:
```python
from pyautogui import hotkey
from subprocess import call
from time import sleep
call(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
sleep(0.500) #You need to increase it if your hardware is slower
hotkey("ctrl", "shift", "n")
```

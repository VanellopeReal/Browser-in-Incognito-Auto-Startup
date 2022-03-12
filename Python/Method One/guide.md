# Method One - 	Subprocess

The most efficient and fast is the **subprocess**

You just need to import it (only the **.call** if needed) and insert the .exe of your browser, examples:

##### Importing:
- import subprocess (entire module)
- from subprocess import call (.call function)

##### Browser Path (example):
- "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

To finish the code, you just need to combine the .call (our subprocess.call) with the path, example:
```python
call(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
```
> obs: "r" is used to ignore Python "\" indexing

##### Incognito Mode:

To open in Incogito Mode, we just need to add a parameter on it, example:
-“C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe -incognito"
> obs: every browser can have different parameters names (example: in Edge, it uses -inprivate, and in Chrome -incognito)

#### The Entire Code Result:
```python
import subprocess
subprocess.call(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe -inprivate")
#Edge uses -inprivate, Chrome -incognito.
#You should be searching or testing which (or what) your browser is using
#In Parameter names
```

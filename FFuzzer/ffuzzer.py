#!/usr/bin/python
from sys import argv
import requests, getopt, os

"""
	Coded by Pyp3R4ng3r 
	Python Versions Tested: 2.7 , 3.x 
	Require requests module 
	How2Install: pip install requests

"""



def file_check(word):
	if os.path.exists(word) == False:
		print ("\n[-]Arquivo nao existe ou esta em diretorio diferente\n")
		exit(1)
	wordlist = []
	wordlist_f = open(word,"r")
	wordlist = wordlist_f.read().split()
	wordlist_f.close()
	return(wordlist)

def b4nner():
	print ("""Web Fuzzer Simple # C0d3d by Pyp3R4ng3r  
options:
	-h 	HOST/IP  target
	-d 	File with directory 
	-p 	Port target  (80 Default)

Usage:
	%s -h h4ckit.n3t -d jboss-dir.txt -p 8081  
	""" % argv[0])
	exit(1)

if len(argv) == 1:
	b4nner()


# Get Options from Arguments inputs
try:
	opts, args = getopt.getopt(argv[1:],"h:d:p",["host=","dir=","port="])
except getopt.GetoptError as err:
	b4nner()

port = 0
for o, a in opts:
	if o in ("-h","--host"):
		host = a
	elif o in ("-p","--port"):
		port =  a
	elif o in ("-d","--dir"):
		word =  a
		print (word)
		# Launch to _file_check function
		wordlist = file_check(word)
	else:
		b4nner()

if not word:
	b4nner


if not port:
	port = 80
port = ":"+str(port)

if "http" not in host:
	host = "http://"+host




print ("""
[*] Target - %s
[*] Port - %s
[*] Directory - %s 
[+] %d / Directories Load

[*] Starting Attack 
""" % (host,port[1:],word,len(wordlist)))


for i in range(len(wordlist)):
	try:
		req = requests.get(host+port+"/"+wordlist[i])
	except requests.exceptions.RequestException:
		print ("[-] Connection Lost")
		exit(1)

	code = req.status_code
	if code == 200:
		print ("[+] OK - "+req.url)
	elif code == 403:
		print ("[x] Forbiden - "+req.url)
	elif code == 500:
		print ("[-] Internal Error - "+req.url)
	elif code == 301:
		print ("[?] Redirect - "+req.url)
	elif code == 400:
		print ("[x] Bad Request - "+req.url)
	elif code == 401:
		print ("[x] Unauthorized - "+req.url)
	else:
		pass

print ("\n[+] Scan Finish ")
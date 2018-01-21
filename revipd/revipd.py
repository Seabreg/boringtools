# -*- coding: utf-8 -*-
from sys import argv
import requests
import re
import urllib

def reverse_host(host):
	print "\n[+] Search for websites in the server host [ Reverse IP]\n"
	payload = {"remoteAddress":host,"key":""}
	r = requests.post("https://domains.yougetsignal.com/domains.php",params=payload)

	if "Daily reverse" in r.content:
		print "[-] YouGetSignal blocked your IP:change your proxy or wait"
		exit()

	broken_1 = re.compile('"(.*?)"')
	a = re.findall(broken_1,r.content)
	out = []
	f = open("revipd_outreverse.txt","a+")
	del a[0:13]
	for i in range(len(a)):
		a[i] = a[i].translate(None,'1')
		if a[i] != "":
			print "[*] "+a[i]
			out.append(a[i])
			f.write(a[i]+"\n")
	f.close
	print "\n[+] Your search was saved in revipd_outreverse.txt\n"


if len(argv) == 1:
	print """
	 _____                                _____ _____
	|  __ \                              |_   _|  __ \
	| |__) |_____   _____ _ __ ___  ___    | | | |__) |
	|  _  // _ \ \ / / _ \ '__/ __|/ _ \   | | |  ___/
	| | \ \  __/\ V / _+_/ |  \__ \  __/  _| |_| |
	|_|  \_\___| \_/ \___|_|  |___/\___| |_____|_|

	       Version:1.1    @pyperanger                                          
	 _____                        _
	|  __ \                      (_)
	| |  | | ___  _ __ ___   __ _ _ _ __
	| |  | |/ _ \| '_ ` _ \ / _` | | '_ \
	| |__| | (_) | | | | | | (_| | | | | |
	|_____/ \___/|_| |_| |_|\__,_|_|_| |_|


	Usage python %s IP/HOST

	""" % (argv[0])
else:
	reverse_host(argv[1])

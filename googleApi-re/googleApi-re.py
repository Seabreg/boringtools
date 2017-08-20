# -*- coding: utf-8 -*- 
import requests
import re
import itertools
import urllib
from random import uniform
from time import sleep

print """ 
+--------------------------------------------+
+----| Google Search com Python - Version 1.1	 
+----| Desenvolvido por PyPe Ranger
|\/\/|
+----| Enjoy to share this c0de ;)				 
+--------------------------------------------+

"""
search = raw_input("Procurar : ")
page = int ( raw_input("Quantidade de paginas a procurar: ") ) * 10
arquivo = raw_input("Arquivo para salvar a busca: ")

print "\n\n[+] Procurando\n"

p = 0
while p < 500:
	
	r = requests.get("https://www.google.com/search?q="+search+"&start="+str(p)) 
	if r.status_code != 200:
		print "\n[-] Google bloqueou seu IP  -  :( "
		exit()

	sites = []
	a = r.content.split()
	for i in range(len(a)):
		
		if "http://webcache" in a[i]:
			i += 1
		elif "http://" in a[i]:
			sites.append(a[i])
		elif "https://" in a[i]:
			sites.append(a[i])

	broken = re.compile("q=(.*?)&amp")
	lista = ""
	for cont in range(len(sites)):
		sites[cont] = re.findall(broken,sites[cont])
	
	lista = "\n".join(list(itertools.chain(*sites)))
	lista = urllib.unquote(lista).decode('utf8') 
	byp_list = str(lista).split()

	save = open(arquivo,"a+")
	for i in range(len(byp_list)):
		if "http://"  in byp_list[i] or "http://"  in byp_list[i]:
			print byp_list[i]
			byp_list[i] = byp_list[i] 
			save.write(byp_list[i]+"\n")

	save.close
	sleep(uniform(3.7,7.0))
	p+= 10

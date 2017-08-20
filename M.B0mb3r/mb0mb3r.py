import smtplib
import os.path

import sys
myinput = None

if sys.version_info >= (3, 0):
    myinput = input
else:
    myinput = raw_input

def banner():
	
	print ("""
		
	 __  __   ____   ___            _    ____       
	|  \/  | |  _ \ / _ \          | |  |___ \      
	| \  / | | |_) | | | |_ __ ___ | |__  __) |_ __ 
	| |\/| | |  _ <| | | | '_ ` _ \| '_ \|__ <| '__|
	| |  | |_| |_) | |_| | | | | | | |_) |__) | |   
	|_|  |_(_)____/ \___/|_| |_| |_|_.__/____/|_|   
				By: Pype Ranger

	[HELP] - Alguns SMTP Servers
			smtp.gmail.com [port:587;465]
			smtp.live.com  [port:587,465,25] 
			smtp.mail.yahoo.com [port:465]

	""")
banner()
server = myinput("SMTP Server:")
port = myinput("Port Server:")
user_mail = myinput("Email:")
password = myinput("Senha:")
lis = myinput("Arquivo com Lista de emails:")

if os.path.exists(lis) == False:
	print ("Arquivo nao existe")
	exit()

assunto = myinput("Assunto:")
TEXT = myinput("Mensagem contida no email:")
x = myinput("Quantidade de Vezes a ser enviado:")
FROM = user_mail
message = 'Subject: %s\n\n%s' % (assunto, TEXT)
print ("\n\n")
l = open(lis,"r")
for TO in l: 
	for y in range(int(x)):

	 gm = smtplib.SMTP(server,port)
	 gm.ehlo()
	 gm.starttls()
	 gm.ehlo()
	 gm.login(user_mail,password) 
	 gm.sendmail(FROM,TO, message)
	 gm.close() 

	 print (("Email Enviados[%d] para => %s" % (y+1,TO)))
	 

l.close()

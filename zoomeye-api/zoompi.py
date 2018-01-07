import requests, json

'''
    zoomeye API v0.1
    C0d3d by pype
    thx j0n3sb0y
'''


MAIL = ""
PASSWORD = ""
QUERY = ""
PRV_TOKEN = ""

def search(token):
    headers = {
        "Authorization" : "JWT "+token
    }
    page = 1
    count_erros = 0
    for i in range(300):
        s = requests.get("https://api.zoomeye.org/host/search?query="+QUERY+str(page), headers=headers)
        if s.status_code == 200:
            for lip in range(len(json.loads(s.text)["matches"])):
                compl_ip = str(json.loads(s.text)["matches"][lip]["ip"])+":"+str(json.loads(s.text)["matches"][lip]['portinfo']['port'])
                print (compl_ip)
                save = open("IPs.txt", "a")
                save.write(compl_ip+"\n")
                save.close()
        elif count_erros > 3:
            print ("Acabou as pages ou deu merda viadin")
            exit()
        else:
            count_erros+=1

        page+=1

def get_token(email, passw):
    try:
        th = {
                "username": email,
                "password": passw
                }

        t = requests.post("https://api.zoomeye.org/user/login", data=json.dumps(th))
        if t.status_code == 200:
            acctoken = str(t.json()["access_token"])
            print ("[+] Login com sucesso: "+acctoken)
            return acctoken
        else:
            print ("[-] sifodeu")
            exit()


    except:
        print ("[-] sifodeu")
        exit()


def main():
    if PRV_TOKEN and QUERY:
        search(PRV_TOKEN)

    elif MAIL and PASSWORD and QUERY:
        token = get_token(MAIL,PASSWORD)
        search(token)

    else:
        print ("[-] sifodeu")


if __name__ == '__main__':
	main()

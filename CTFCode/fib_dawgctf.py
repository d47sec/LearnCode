import socket
import re

dayso=[]
c=0
a=1
b=1

while c<999999999999999999999999999:
	c=a+b
	b=a
	a=c
	dayso.append(str(c))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("umbccd.io", 6000))

while 1:
    data = s.recv(1024)
    if data == "":
        break

    x=(re.search('\[.*\]',data.decode('utf-8'))) # lấy mảng ở trong data 
    if x:
        x=x.group()[1:-1] # vì x nhận trả về là một chuỗi [1,2,3] lấy [1:-1] để bỏ đi 2 kí tự []
        ls=x.split(',')
        x=''
        for i in ls:
            i=i.replace(' ','')
            if i in dayso:
                x=i
        if x=='':
        	x=ls[2]
        x=x+'\n'
        s.send(bytes(x.encode()))
    print(data)

s.close()

# Congrats! Here's your flag: DawgCTF{jU$T_l1k3_w3lc0me_w33k}





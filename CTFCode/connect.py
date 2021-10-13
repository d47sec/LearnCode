from pwn import remote
host = '103.229.41.18' 
port = 8084
r = remote(host, port)
r.recvuntil("Now, let find S with n:\n")
data = r.recv()
print(data)
while data:
    try:
        print(data)
        data = data.decode().strip()
        res = int(data) * (2 * int(data) - 1)
        print("Sending {}".format(res))
        r.send(str(res)+"\n")
        data = r.recv()
    except:
        print(r.recvuntil("}"))
        break

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # có chức năng khởi tạo một socket 
# AF_INET ==> CHỈ ĐỊNH IP ĐƯỢC SỬ DỤNG==> Ở ĐÂY LÀ IPv4
# SOCK_STREAM ===> CHỈ ĐỊNH GIAO THỨC ĐƯỢC SỬ DỤNG , Ở ĐÂY LÀ TCP 

s.connect(("172.104.49.143",9234)) # kết nối đến server có host và port đã được chỉ định cụ thể 
data = s.recv(10240).decode(); # nhận dữ liệu từ server
print(data)
data = s.recv(10240).decode();
print(data)

# bài này sử dụng thuật toán binary search  ===> log2(r) < 70
l = 0
r = 18446744073709551616
while True:
    m = ( l + r ) // 2; # // chia lấy phần nguyên 
    s.send((str(m)+'\n').encode())
    print(m)
    data = s.recv(10240).decode(); 
    print(data)
    data = data.split()[4].replace(';',''); # [low/high] # ở chỗ này sài regex cũng được 

    if (data == "high"): 
        r = m-1; # too high -> the answer is strictly less than m
    else:
        l = m + 1; # too low -> the answer is strictly larger than m

# Flag{meow_meow_meow}
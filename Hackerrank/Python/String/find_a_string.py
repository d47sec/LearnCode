import re

def count_substring(string, sub_string):
    #  Đề: tính tổng số lần xuất hiện của chuỗi sub_string trong string 
    len_sub_string = len(sub_string)
    len_string = len(string)
    k = 0
    for i in range(len_string - len_sub_string + 1):
        if string[i:i+len_sub_string] == sub_string:
            k += 1
    return k

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
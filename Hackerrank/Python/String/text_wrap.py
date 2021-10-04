
def wrap(string, max_width):
    len_string = len(string)
    result = ''
    for i in range(0,len_string,max_width):
        result += string[i:i+max_width] + "\n"
    
    return result 

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
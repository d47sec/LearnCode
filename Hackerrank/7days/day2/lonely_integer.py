def lonelyinteger(a):
    # Write your code here
    dict = {}
    for i in a:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
            
    for i in dict:
        if dict[i] == 1:
            return i 
        

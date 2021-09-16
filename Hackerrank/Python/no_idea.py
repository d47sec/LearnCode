if __name__ == "__main__":

    n, m = list(input().split())
    arr_choice = list(input().split())
    A = list(input().split()) #
    B = list(input().split()) #

    print(arr_choice) #
    print(A)
    print(B)
    result = 0 
    for i in arr_choice: 
        if i in A: result += 1 
        elif i in B: result -= 1 
        else: pass 
    print(result)
    
# TIME EXCEEDED
# link: https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

# cách lấy bao nhiêu số thập phân đằng sau dấu chấp trong python 

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    result =  "{:.2f}".format(sum(marks)/3)
    print(result)

# link: https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
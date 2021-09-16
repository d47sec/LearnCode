if __name__ == '__main__':
    # print("Nhap vao N: ")
    d = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name] = score

    second = sorted(list(set(d.values())))[1]
    second_lowest = []
    for key, value in d.items():
        if value == second:
            second_lowest.append(key)
    second_lowest.sort()
    for val in second_lowest:
        print(val)

# link: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
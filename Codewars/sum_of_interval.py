
def sum_of_intervals(intervals):
    l = []
    for i, j in intervals:
       l += range(i, j)

    return len(set(l))
        
print(sum_of_intervals([(1, 5), (6, 10), (1,4)]))

# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python
# Day 2
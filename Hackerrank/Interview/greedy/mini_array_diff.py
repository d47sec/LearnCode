def minimumAbsoluteDifference(arr):
    # Write your code here
    min_value = 99999999999
    arr.sort()
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i+1]) < min_value:
            min_value = abs(arr[i] - arr[i+1])
    return min_value



# link: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
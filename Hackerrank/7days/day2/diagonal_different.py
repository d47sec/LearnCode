def diagonalDifference(arr):
    # Write your code here
    left, right = 0, len(arr)-1
    result = 0 
    while left < len(arr) and right >= 0:
        result += (arr[left][left] - arr[left][right])
        left += 1
        right -= 1
    return abs(result)

# https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two&h_r=next-challenge&h_v=zen
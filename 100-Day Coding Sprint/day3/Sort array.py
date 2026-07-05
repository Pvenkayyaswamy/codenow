# complete program that reads stdin and writes stdout
import sys
data = list(map(int , sys.stdin.read().split()))
n , arr = data[0] , data[1:]
arr = sorted(arr)
mid = (n+1)//2
print(*(arr[:mid])+arr[mid:][::-1])     # '*' unpacks the list and send to print as individual numbers

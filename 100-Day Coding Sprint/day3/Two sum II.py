# complete program that reads stdin and writes stdout
import sys
data = sys.stdin.read().split()
le,num = int(data[0]),int(data[1])
arr = [int(x) for x in data[2:2+le]]
left , right = 0, le - 1
while left<right:
    temp = arr[left]+arr[right]
    if temp == num :
        print(f"{left+1} {right+1}")
        break
    elif temp < num:
        left+=1
    else :
        right -= 1

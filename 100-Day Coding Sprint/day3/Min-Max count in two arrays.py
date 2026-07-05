# complete program that reads stdin and writes stdout
import sys
data = sys.stdin.read().split()
len1,len2=int(data[0]),int(data[1])      # input data is string type so convert into int its mandatory
arr1 = [int(x) for x in data[2:2+len1]]
arr2 = [int(x) for x in data[2+len1:2+len2+len1]]
k = int(data[2+len1+len2])
left=sum(1 for i in arr1 if i>k)
right = sum(1 for i in arr2 if i<k)
print(max(left,right))

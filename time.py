import time
import math
import matplotlib
import matplotlib.pyplot as plt

def b_s(a,low,high,key):
    if(low<=high):
        mid=(low+high)//2
        if(key==a [mid]):
            return mid
        if (key<a[mid]):
            return b_s(a,low,mid-1,key)
        else:
            return b_s(a,mid+1,high,key)
        return-1
a=[]
n=int(input("enter no of elements"))
for i in range(0,n):
    e=int(input("enter element"))
    a.insert(i,e)
key=int(input("enter  key value"))
start=time.time()
print("the array is:",a,"the element to search is:",key)
r=b_s(a,0,n-1,key)
end=time.time()
if(r ==-1):
    print("key element not found")
else:
    print("key element found at position",r)
    print("time taken to search an element",end-start)

x=list(range(1,100))
plt.plot(x,[y*math.log(y) for y in x])
plt.title("time complexity of binary search log(n)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()

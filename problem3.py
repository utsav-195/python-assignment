import math


class ElementNotFoundError(Exception):
    def __int__(self):
       return

def binarySearch(num,list):
    start = 0
    end = len(list)-1
    while start <= end:
        mid = int(math.ceil((start + end) / 2))
        #print("mid",mid)
        if list[mid] == num:
            return mid
        elif key>list[mid]:
            start=mid+1
            #print("start",start)
        else:
            end=mid-1
    return 9999999


n=int(raw_input("enter length of list "))
l=[]
for i in range(0,n):
    l.append(int(raw_input("enter element in sorted manner: ")))
key=int(raw_input("enter key to be searched: "))
index=9999999
try:
    index=binarySearch(key,l)
    if index==9999999:
        raise ElementNotFoundError
except ElementNotFoundError:
    print("Element Not Found")


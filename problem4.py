n=int(raw_input("enter number of lists: "))
l=[]
for i in range(0,n):
    l.append(tuple(map(int,raw_input().split())))

for i in range(0,len(l)-1):
    for j in range(0,len(l)-i-1):
        if l[j][len(l[j])-1]>l[j+1][len(l[j+1])-1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)
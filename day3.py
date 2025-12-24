# 1 find the min and max
a=[6,3,9,6,5]
n=len(a)
min=a[0]
max=a[0]
for i in a:
    if(i>max):
        max=i
    if(i<min):
        min=i
print(min)
print(max)

#2 find the prime number
a = 7
flag = True

if a <= 1:
    flag = False
else:
    for i in range(2, a):
        if a % i == 0:
            flag = False
            break

if flag:
    print("prime number")
else:
    print("not prime")

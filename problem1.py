'''in this we will print a pattern with stars '''

for i in range(0 ,5):
    for j in range(0 ,i+1):
        print("*" , end= " ")
    print("\r")
#problem 2    
a =1 
for i in range(0 ,5):
    for j in range(0 ,i+1):
        print(a , end = " ")
        a = a+1
    print("\r")
#problem 3
b = 1
for i in range(0 , 5):
    for j in range(0 ,i+1):
        print(b , end = " ")
        b = b+2
    print("\r")
a = 100
n = 1
while(n<=5):
    if(n<4):
        print(a-n)
    else:
        print(a+n)
    n = n+1
#problem 4 
x = 100
y = 200
n =1
while(n<=5):
    if(n<3):
        x = x+10
        print(x)
    else:
        y=y+10
        print(y)
    n=n+1 
#problem 5
a =1
b =2
c =2
d =1
i = 1
while (i<=5):
    if(i==3):
        print(a+b+c+d)
    else:
        print(a+b)
    i = i+1
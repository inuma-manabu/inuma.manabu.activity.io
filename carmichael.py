import math
n = int(input('Input n: '))
m = 0
for a in range(1,n):
    x=a**(n-1)%n
    if a%1000==0:
           print(a) 
    if x!=1 and math.gcd(n,a)==1:
       print(n, "is not prime")
       print(a, x)
       break
    elif x!=1 and math.gcd(n,a)!=1:
       m=m+1        
if a==n-1 and m==0:
    print("prime")
elif a==n-1 and m!=0:
    print("carmichael")
        

import math
print('Miller test from 2s+1 to 2t-1')
s= int(input('Input number s: '))
t = int(input('Input number t: '))
b= int(input('Input base b: '))
SP=[]
P=[]
for k in range(s,t):
 n=2*k+1
 q=n-1
 L=[]
 while   q%2==0:
  q=int(q/2)
  L=[b**q%n]+L
 if L[0] == 1 or  L.count(n-1) != 0:
  c=0
  for i in range(1,n):
        if i**(n-1)%n==1:
         c=c+1
         #print(i,n,c)
  if c!=n-1:
      SP=SP+[n]
      print("Miller's seudo numbers are",SP)
  else:
      P=P+[n]
      print("Prime numbers are",P)





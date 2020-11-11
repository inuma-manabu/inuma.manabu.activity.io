import math
s= int(input('Input odd s: '))
t = int(input('Input odd t: '))
b= int(input('Input b: '))
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
      print("Miller seudoprimes are",SP)
  else:
      P=P+[n]
      print("Prime numbers are",P)





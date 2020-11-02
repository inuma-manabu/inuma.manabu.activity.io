import math
import numpy as np
import sympy as sym
p= int(input('Input prime p: '))
n= int(input('Input n (length of x): '))
k= int(input('Input k (dimension k): '))
t=int((n-k)/2)
l0=n-1-t
l1=t
print('t=',t,'l0=',l0,'l1=',l1)
x=[]
r=[]
A=np.ones((n,l0+l1+2),dtype=int)
for  i in range(n):
  print(f'Input x{i}')
  a=int(input())%p
  x=np.array(np.append(x,int(a)),dtype=int)
print('x=',x)
for  i in range(n):
  print(f'Input r{i}')
  a=int(input())%p
  r=np.array(np.append(r,int(a)),dtype=int)
print('r=',r)
for i in range(n):
  for j in range(l0+1):
    A[i][j]=int(x[i]**j)%p
  for j in range(l1+1):
    A[i][l0+j+1]=int(r[i]*(x[i]**j))%p
print('A=',A)
Q=eliminate1(A,p)
print('Q=',Q)
polyQ0=np.poly1d([Q[l0-u] for u in range(l0+1)])
polyQ1=np.poly1d([Q[l0+l1+1-u] for u in range(l1+1)])
print('polyQ0=',polyQ0)
print('polyQ1=',polyQ1)
f=(-polyQ0/polyQ1)[0]
print('f=',f)
c=np.array([f(x[v])%p for v in range(n)])
print('c=',c)


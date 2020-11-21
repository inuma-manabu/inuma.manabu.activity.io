import math
import numpy as np
import sympy as sym
p= int(input('Input prime p: '))
n= int(input('Input n (length of x): '))
k= int(input('Input k (dimension k): '))
t=int((n-k)/2)
l0=n-1-t
l1=t
print('t=',t,', l0=',l0,', l1=',l1)
#x=[]
#r=[]
A=np.ones((t,t+1),dtype=int)
x = list(map(int, input(f'Input x of length {n} : ').split()))
x = np.array(x)%p
H=np.array([[x[j]**(i+1)%p for j in range(len(x))] for i in range(n-k)])
print(
  #'x=',x,
'H=',H)
r = list(map(int, input(f'Input r of length {n} : ').split()))
r = np.array(r)%p
#for  i in range(n):
  #print(f'Input r{i}')
  #a=int(input())%p
  #r=np.array(np.append(r,int(a)),dtype=int)
S=H@r%p
print(
  #'r=', r,
'S=',S)
for i in range(t):
  for j in range(t+1):
    A[i][j]=int(S[i+j])%p
#print('A=', A)
Q=eliminate1(A,p)
Q1_array=np.array([Q[l1-u] for u in range(l1+1)])%p
polyQ1=np.poly1d(Q1_array)
print('polyQ1='\
      \
      , polyQ1)
P=np.zeros((n,n),dtype=int)
errorfree=[]
for i in range(n):
  if polyQ1(x[i])%p==0:
    P[i][i]=1
  else:
    errorfree=errorfree+[i]
B=np.dot(H,P)%p
print('B=',B)
BB=np.transpose(np.vstack((np.transpose(B),[(-S[i])%p for i in range(n-k)])))
#print('BB=',BB)
e=eliminate1(BB,p)
for i in range(len(errorfree)):
  e[errorfree[i]]=0
e=[e[i]%p for i in range(n)]
print('e=',e)
c=(r-e)%p
print('c='\
      ,  c)
#else:
  #print('復号語を出力できません')


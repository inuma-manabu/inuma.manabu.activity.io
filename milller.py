import math
n= int(input('Input odd n: '))
b= int(input('Input b: '))
SP=[]
q=n-1
L=[]
while   q%2==0:
  q=int(q/2)
  L=[b**q%n]+L
if L[0] == 1 or  L.count(n-1) != 0:
  print(L, n, "is prime or strong pseudoprime")
else:
   print(L, n, "is composite")
   

        
    
  

    
        

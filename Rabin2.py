def rabin2(n):
  #n= int(input('Input odd n: '))
  #b= int(input('Input b: '))
  c=0
  a=-1
  if n==2:
    a=1
  elif n%2==0:
    a=-1
  else:
    for b in range(1,n):
      q=n-1
      L=[]
      if a==0:
        #print(n, "is composite")
        break
      elif a==-1 and c>n/4:
        a=1
        #print(n, "is prime")
        break
      else:
        while   q%2==0:
          q=int(q/2)
          L=[b**q%n]+L
          #print("q=",q,"L=",L)
        if L[0] == 1 or  L.count(n-1) != 0:
          c=c+1
          #print(L, n, "is prime or strong pseudoprime","b=",b,"c=",c)
        else:
          #print("b=,",b,"L=",L)
          a=0
  return a

        
    
  

    
        

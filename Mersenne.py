def mersenne(p):
  #p= int(input('Input prime p: '))
  #b= int(input('Input b: '))
  n=2**p-1
  t=int((n**0.5-1)/(2*p))+1
  d=1
  for r in range(1,t):
    q=1+2*p*r
    #if rabin2(q)==1:
    #print("r/t=",round((q-1)/(2*p*t),2))
    if n%q==0:
      d=0
      #print("n=",n,"is composite,q=",q)
      break      
  if d==1:
     q=n
     #print("n=",n,"is prime")
  return d,p,q
    
  

    
        

def mersenne2():
  s= int(input('Input number s>=2: '))
  #b= int(input('Input b: '))
  L=[]
  for p in range(2,s+1):
    l=[]
    if rabin2(p)==1:
      #print(p)
      if mersenne(p)[0]==1:
          l=l+[mersenne(p)[j] for j in range(1,3)]
          L=L+[l]
          #print(L)
  return L      
    
  

    
        

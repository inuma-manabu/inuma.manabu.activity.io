def eliminate(i,j,A,p):
    n=A.shape[0]
    m=A.shape[1]
    c=invp(int(A[i][j]),p)
    if c!=1:
        print(i+1,'行目を',c,'倍する')
        for l in range(j,m):
         A[i][l]=A[i][l]*c%p
    print(A)     
    for k in range(i):
         d=(-A[k][j])%p
         if d!=0:
             print(i+1,'行目を',d,'倍して',k+1,'行目に加える')
             for l in range(j,m):
                A[k][l]=(A[k][l]+A[i][l]*d)%p
             print(A)
    for k in range(i+1,n):
         d=(-A[k][j])%p
         if d!=0:
             print(i+1,'行目を',d,'倍して',k+1,'行目に加える')
             for l in range(j,m):
                A[k][l]=(A[k][l]+A[i][l]*d)%p
             print(A)
    return(A)

    
        

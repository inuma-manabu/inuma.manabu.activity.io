def eliminate1(A,p):
  n=A.shape[0]
  m=A.shape[1]
  print('n,m=',n,m)
  Q=np.zeros(m,dtype=int)
  pivot=[]
  for j in range(m):
        s=len(pivot)
        #print('j,s=',j,s)
        count=0 #ピボットを見つけるまでの0の個数
        for i in range(s,n):
                 #print('i,s=',i,s)
                 if i==s and A[i][j]!=0:
                     print(s+1,'行',j+1,'列をピボットとして掃き出しを行う')
                     eliminate(i,j,A,p)
                     break
                 elif i>s and A[i][j]!=0:
                     print(s+1,'行目と',i+1,'行目を入れ替えて',s+1,'行',j+1,'列をピボットとして掃き出しを行う')
                     B=np.array(A[s])
                     A[s]=np.array(A[i])
                     A[i]=np.array(B)
                     print(A)
                     eliminate(i,j,A,p)
                     break
                 elif A[i][j]==0:
                     count=int(count+1)
        if count==n-s:
            for t in range(s):
                Q[pivot[t]]=(Q[pivot[t]]-A[t][j])%p
            Q[j]=1
            #print('Q=',Q)
        else:
            pivot=pivot+[j]            
  print('AQ=0の解はQ=',Q)
  return Q
            
        

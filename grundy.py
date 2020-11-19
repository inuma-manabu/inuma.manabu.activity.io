import math
T= list(map(int, input(f'Input T : ').split()))
n= int(input('Input n : '))
L=[]
for k in range(n+1):
    g=0
    #print('k=',k)
    for j in range(k):
        for i in range(1,k+1):
            if i not in T and g==L[k-i]:
                g=g+1
    L=L+[g]
print(L)

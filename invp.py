def invp(a,p):
    for b in range(p):
        if a*b%p==1:
          break
    return b

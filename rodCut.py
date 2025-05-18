
"""
"""

import Math

def  CutRod(p, n):
    if n==0:
      return 0
    q = -Math.inf
    for i in range(n):
      q = max(q, p[i]+CutRod(p, n-i-1))
    return q

def memoizedCutRod(p, n):
  r = [-Math.inf] * (n+1)
  return memoizedCutRodAux(p, n, r)

def memoizedCutRodAux(p, n, r):
  if r[n] >= 0:
    return r[n]
  if n == 0:
    q = 0
  else:
    q = -Math.inf
    for i in range(1, n+1):
      q = max(q, p[i]+memoizedCutRodAux(p, n-i, r)
  r[n] = q
  return q
  
  


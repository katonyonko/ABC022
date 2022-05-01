import io
import sys

_INPUT = """\
6
5 60 70
50
10
10
10
10
5 50 100
120
-10
-20
-30
70
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,S,T=map(int,input().split())
  W=int(input())
  ans=0
  if S<=W<=T: ans+=1
  for i in range(N-1):
    A=int(input())
    W+=A
    if S<=W<=T: ans+=1
  print(ans)
import io
import sys

_INPUT = """\
6
5
1
2
3
2
1
11
3
1
4
1
5
9
2
6
5
3
5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=[int(input()) for _ in range(N)]
  visited=set()
  ans=0
  for i in range(N):
    if A[i] in visited: ans+=1
    visited.add(A[i])
  print(ans)
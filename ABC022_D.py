import io
import sys

_INPUT = """\
6
4
0 0
0 1
1 0
1 1
0 2
2 0
-2 0
0 -2
6
3 4
1 3
4 3
2 2
0 1
2 0
5 5
-1 2
-1 -3
2 1
2 6
4 -3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=[list(map(int,input().split())) for _ in range(N)]
  B=[list(map(int,input().split())) for _ in range(N)]
  ax,ay=sum([A[i][0] for i in range(N)])/N,sum([A[i][1] for i in range(N)])/N
  bx,by=sum([B[i][0] for i in range(N)])/N,sum([B[i][1] for i in range(N)])/N
  a=sum([((A[i][0]-ax)**2+(A[i][1]-ay)**2)**.5 for i in range(N)])
  b=sum([((B[i][0]-bx)**2+(B[i][1]-by)**2)**.5 for i in range(N)])
  print(b/a)
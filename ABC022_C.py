import io
import sys

_INPUT = """\
6
5 7
1 2 2
1 4 1
2 3 7
1 5 12
3 5 2
2 5 3
3 4 5
5 4
1 2 1
1 3 1
1 4 1
1 5 1
10 12
1 4 3
1 9 1
2 5 4
2 6 1
3 7 5
3 10 9
4 7 2
5 6 6
5 8 5
6 8 3
7 9 5
8 10 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop,heappush
  def Dijkstra(G,s):
    done=[False]*len(G)
    inf=10**20
    C=[inf]*len(G)
    C[s]=0
    h=[]
    heappush(h,(0,s))
    while h:
      x,y=heappop(h)
      if done[y]:
        continue
      done[y]=True
      for v in G[y]:
        if C[v[1]]>C[y]+v[0]:
          C[v[1]]=C[y]+v[0]
          heappush(h,(C[v[1]],v[1]))
    return C
  N,M=map(int,input().split())
  G=[[] for _ in range(N)]
  next=[]
  for i in range(M):
    u,v,l=map(int,input().split())
    u-=1; v-=1
    if u==0: next.append((l,v))
    if v==0: next.append((l,u))
    if u!=0 and v!=0:
      G[u].append((l,v))
      G[v].append((l,u))
  ans=10**10
  for i in range(len(next)):
    d=Dijkstra(G,next[i][1])
    for j in range(i+1, len(next)):
      ans=min(ans,d[next[j][1]]+next[i][0]+next[j][0])
  if ans==10**10: print(-1)
  else: print(ans)
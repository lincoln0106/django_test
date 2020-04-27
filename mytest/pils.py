#encoding=UTF-8
MAX=9
'''
Created on 2016年9月28日
@author: sx
'''
b=999
G=[[0,1,5,b,b,b,b,b,b],
 [1,0,3,7,5,b,b,b,b],
 [5,3,0,b,1,7,b,b,b],
 [b,7,b,0,2,b,3,b,b],
 [b,5,1,2,0,3,6,9,b],
 [b,b,7,b,3,0,b,5,b],
 [b,b,b,3,6,b,0,2,7],
 [b,b,b,b,9,5,2,0,4],
 [b,b,b,b,b,b,7,4,0]]
P=[]
D=[]
def Djstela(G,P,D):
 final=[]
 for i in range(0,len(G)):
  final.append(0)
  D.append(G[0][i])
  P.append(0)
 D[0]=0
 final[0]=1
 k=03
 for v in range(1,len(G)):
  min=999
  for w in range(0,len(G)):
   if final[w]==0 and D[w]<min:
    k=w
    min=D[w]
  final[k]=1
  for t in range(0,len(G)):
   if min+G[k][t]<D[t]:
    D[t]=min+G[k][t]
    P[t]=k
 print("\n最短路径\n",D,"\n","\n前一个选择\n",P)
def search(x):
 print("选择的终点",x,"最短路径",D[x])
print("邻接矩阵\n")
for i in range(0,9):
 print(G[i])
Djstela(G, P, D)
q=input("\n请输入终点")
search(int(q))
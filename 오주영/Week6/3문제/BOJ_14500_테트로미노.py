import sys, heapq
input=sys.stdin.readline

x,y=tuple(map(int,input().split()))
field_0=[list(map(int,sys.stdin.readline().split())) for _ in range(x)]   #원본 공간 x,y
field_1=list(map(list,zip(*field_0)))  # 행 열 반전 y,x
field_2=[field_1[i][-1::-1] for i in range(y)]  # 좌 우 반전 y,x
field_3=list(map(list,zip(*field_2)))  # 행 열 반전 x,y
field_4=[field_3[i][-1::-1] for i in range(x)]  # 좌 우 반전 x,y
field_5=list(map(list,zip(*field_4)))  # 행 열 반전 y,x
field_6=[field_5[i][-1::-1] for i in range(y)]  # 좌 우 반전 y,x
field_7=list(map(list,zip(*field_6)))  # 행 열 반전 x,y
# fieldset=(field_0,field_1,field_2,field_3,field_4,field_5,field_6,field_7)

heap=[]
# def blo(i,j):
#     return ((i,j),(i+1,j),(i,j+1),(i+1,j+1))
# def bli(i,j):
    

# def peak(bl_type,field):
    

for i in range(x-1):    #O블럭
    for j in range(y-1):
        blo=field_0[i][j]+field_0[i+1][j]+field_0[i][j+1]+field_0[i+1][j+1]
        heapq.heappush(heap,-blo)

for i in range(x):      #I블럭
    for j in range(y-3):
        bli=field_0[i][j]+field_0[i][j+1]+field_0[i][j+2]+field_0[i][j+3]
        heapq.heappush(heap,-bli)       
for i in range(y):      #I블럭
    for j in range(x-3):        
        bli=field_1[i][j]+field_1[i][j+1]+field_1[i][j+2]+field_1[i][j+3]
        heapq.heappush(heap,-bli)
        
for i in range(x-1):    #S,T,7블럭
    for j in range(y-2):
        for fi in (field_0,field_3):
            bls=fi[i][j]+fi[i][j+1]+fi[i+1][j+1]+fi[i+1][j+2]
            heapq.heappush(heap,-bls)
        for fi in (field_0,field_3,field_4,field_7):
            blt=fi[i][j]+fi[i][j+1]+fi[i][j+2]+fi[i+1][j+1]
            bl7=fi[i][j]+fi[i][j+1]+fi[i][j+2]+fi[i+1][j]
            heapq.heappush(heap,-blt)
            heapq.heappush(heap,-bl7)    
            
for i in range(y-1):    #S,T,7블럭
    for j in range(x-2):
        for fi in (field_1,field_2):
            bls=fi[i][j]+fi[i][j+1]+fi[i+1][j+1]+fi[i+1][j+2]
            heapq.heappush(heap,-bls)
        for fi in (field_1,field_2,field_5,field_6):
            blt=fi[i][j]+fi[i][j+1]+fi[i][j+2]+fi[i+1][j+1]
            bl7=fi[i][j]+fi[i][j+1]+fi[i][j+2]+fi[i+1][j]
            heapq.heappush(heap,-blt)
            heapq.heappush(heap,-bl7)
         
print(-heapq.heappop(heap))



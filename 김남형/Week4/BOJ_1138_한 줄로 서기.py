n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n

for i in range(n): # 
    cnt = 0 # 빈 자리 카운트
    for j in range(n):
        if cnt == arr[i] and ans[j] == 0: # 본인 인덱스에 주어진 수와 앞에 빈 자리 수가 같고, 현재 자리가 비었으면
            ans[j] = i+1
            break
        elif ans[j] == 0: # 자리가 비어있으면 cnt 증가
            cnt += 1
        
print(*ans)

# 본인 인덱스에 주어진 수만큼 앞에 자리를 비워두고 빈 자리에 찾아가면 된다.

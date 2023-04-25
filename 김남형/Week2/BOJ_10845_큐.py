import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
  com = sys.stdin.readline().split()
  
  if com[0] == 'push':
    arr.append(com[1])
  elif com[0] == 'size':
    print(len(arr))
  elif com[0] == 'pop':
    if len(arr) > 0:
      print(arr.pop(0))
    else:
      print(-1)
  elif com[0] == 'empty':
    if len(arr) > 0:
      print(0)
    else:
      print(1)
  elif com[0] == 'front':
    if len(arr) > 0:
      print(arr[0])
    else:
      print(-1)
  elif com[0] == 'back':
    if len(arr) > 0:
      print(arr[-1])
    else:
      print(-1)

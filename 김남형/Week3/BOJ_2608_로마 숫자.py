# num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

# 로마 숫자를 숫자로 바꾸는 함수
def num(x):
  # 3번 조건
  for i in range(len(x)):
    try : # 알파벳이 남아 있을 때(두 개가 바뀌면 리스트 범위를 벗어남)
      if x[i] == 'I':
        try: # 마지막 인덱스에 걸리면 x[i+1]이 없어서 오류남
          if x[i+1] == 'V':
            x[i] = 4
            del x[i+1]
          elif x[i+1] == 'X':
            x[i] = 9
            del x[i+1]
          else:
            x[i] = 1
        except: # 마지막 인덱스일 경우
          x[i] = 1

      elif x[i] == 'V':
        x[i] = 5

      elif x[i] == 'X':
        try:
          if x[i+1] == 'L':
            x[i] = 40
            del x[i+1]
          elif x[i+1] == 'C':
            x[i] = 90
            del x[i+1]
          else:
            x[i] = 10
        except:
          x[i] = 10

      elif x[i] == 'L':
        x[i] = 50

      elif x[i] == 'C':
        try:
          if x[i+1] == 'D':
            x[i] = 400
            del x[i+1]
          elif x[i+1] == 'M':
            x[i] = 900
            del x[i+1]
          else:
            x[i] = 100
        except:
          x[i] = 100

      elif x[i] == 'D':
        x[i] = 500

      elif x[i] == 'M':
        x[i] = 1000

    except: # 알파벳이 없을 때
      break
  return sum(x)

def roma(x):
  IV_cnt = IX_cnt = XL_cnt = XC_cnt = CD_cnt = CM_cnt = I_cnt = V_cnt = X_cnt = L_cnt = C_cnt = D_cnt = M_cnt = 0

  while x != 0:
    if x // 1000 >= 1: # 1000
      if M_cnt <= 3:
        x -= 1000
        M_cnt += 1
        ans.append('M')
        I_cnt = X_cnt = C_cnt = 0
        continue

    elif x // 900 >= 1: # 900
      if CM_cnt == 0:
        x -= 900
        CM_cnt += 1
        ans.append('CM')
        I_cnt = X_cnt = C_cnt = M_cnt = 0
        continue

    elif x // 500 >= 1: # 500
      if D_cnt == 0:
        x -= 500
        D_cnt += 1
        ans.append('D')
        I_cnt = X_cnt = C_cnt = M_cnt = 0
        continue

    elif x // 400 >= 1: # 400
      if CD_cnt == 0:
        if CM_cnt == 0:
          x -= 400
          CD_cnt += 1
          ans.append('CD')
          I_cnt = X_cnt = C_cnt = M_cnt = 0
          continue

    elif x // 100 >= 1: # 100
      if C_cnt <= 3:
        x -= 100
        C_cnt += 1
        ans.append('C')
        I_cnt = X_cnt = M_cnt = 0
        continue

    elif x // 90 >= 1: # 90
      if XC_cnt == 0:
        x -= 90
        XC_cnt += 1
        ans.append('XC')
        I_cnt = X_cnt = C_cnt = M_cnt = 0
        continue

    elif x // 50 >= 1: # 50
      if L_cnt == 0:
        x -= 50
        L_cnt += 1
        ans.append('L')
        I_cnt = X_cnt = C_cnt = M_cnt = 0
        continue

    elif x // 40 >= 1: # 40
      if XL_cnt == 0:
        if XC_cnt == 0:
          x -= 40
          XL_cnt += 1
          ans.append('XL')
          I_cnt = X_cnt = C_cnt = M_cnt = 0
          continue

    elif x // 10 >= 1: # 10
      if X_cnt <= 3:
        x -= 10
        X_cnt += 1
        ans.append('X')
        I_cnt = C_cnt = M_cnt = 0
        continue

    elif x // 9 >= 1: # 9
      if IX_cnt == 0:
        x -= 9
        IX_cnt += 1
        ans.append('IX')
        I_cnt = X_cnt = C_cnt = M_cnt = 0
        continue

    elif x // 5 >= 1: # 5
      if V_cnt == 0:
        x -= 5
        V_cnt += 1
        ans.append('V')
        I_cnt = X_cnt = C_cnt = M_cnt = 0
        continue

    elif x // 4 >= 1: # 4
      if IV_cnt == 0:
        if IX_cnt == 0:
          x -= 4
          IV_cnt += 1
          ans.append('IV')
          I_cnt = X_cnt = C_cnt = M_cnt = 0
          continue

    elif x // 1 >= 1: # 1
      if I_cnt <= 3:
        x -= 1
        I_cnt += 1
        ans.append('I')
        X_cnt = C_cnt = M_cnt = 0
        continue

  return ''.join(ans)

x, y = list(input()), list(input())
ans = []

sum = num(x) + num(y)
print(sum)
print(roma(sum))

# 1번 조건은 3번 조건 충족 시 해결
# 2번, 4번 조건은 출력 시 사용
# 4번 조건 = 그리디
# 2번 + 3번 :
# 가. 4, 9, 40, 90, 400, 900은 한 번씩만 사용 가능
# 나. (4, 9), (40, 90), (400, 900)은 둘 중 하나만 사용 가능
# 다. 5, 50, 500은 한 번만 사용 가능
# 라. 1, 10, 100, 1000은 연속해서 세 번까지만 사용 가능

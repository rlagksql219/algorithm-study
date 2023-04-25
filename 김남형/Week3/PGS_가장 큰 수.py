def solution(numbers):
    s = list(map(str,numbers))
    a = sorted(s,key=lambda x: x*3,reverse=True)
    return str(int("".join(a)))
  
# 입력 받는 수가 1000 미만이므로 앞에 세 자릿수만 비교하면 됨
# 문자열을 3번 반복해서 비교하면 해결

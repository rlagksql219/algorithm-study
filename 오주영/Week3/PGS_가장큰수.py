def solution(numbers):
    answer = ''
    numbers=list(map(str,numbers)) #각 원소를 문자열로
    # ml=max(len(numbers))    #가장 큰 자리수 확인하려고 넣었는데 오류나서 보류
    # a=[]
    # dic={}
    a=[i*3 for i in numbers] #리스트 내포방식
    # for i in numbers:   
    #     a.append(i*3) #1000 이하이므로 앞 3자리를 비교하기 위해
    # print(a,len(a))
    # for i,v in enumerate(a):
    #     dic[v] = numbers[i] # a를 정렬한 후 호출할 수 있게
    dic={v : numbers[i] for i,v in enumerate(a)}    #리스트 내포방식
    a.sort(key=lambda x:x[0:2],reverse=True)    #맨앞3자리로 정렬
    # print(dic)
    
    # print(a)
    for i in a:
        answer+=dic[i]
        # print(answer)
    
    
    return answer

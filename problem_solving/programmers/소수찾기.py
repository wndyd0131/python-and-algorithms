# retry
def solution(numbers):
    '''
    한자리수 종이조각
    "1"
    "1111"
    "1234567"
    "0000"
    "0"
    조합을 만들어서, 2~그 수까지 나눠서 나눠떨어지면 소수가 아님
    "1", "2"는 원래 나눠 떨어지니까 제외
    3,4,5,6,7,8,9
    2,
    2,3,5,7
    
    재귀 함수
    1234567
    7
    1234567 -> 소수?
    123456 -> 소수?
    6
    1234567 -> 소수?
    123457 -> 소수?
    12345 -> 소수?
    5
    1234567 -> 소수?
    12345
    123457 -> 소수?
    12345 -> 소수?
    
    "1234"

123
"1"
"12"
"123"
"13"
"2"
"23"

Base case
    numbers 길이만큼 반복
Recursion
    숫자 append
    방문하지 않았으면
        방문 표시
        Recurse
        방문 해제
Recursive Tree
    '''
    hashset = set()
    visited = [False] * len(numbers)
    answer = 0
    
    def dfs(cur_str):
        if cur_str != "":
            hashset.add(int(cur_str))
            
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                dfs(cur_str + numbers[i])
                visited[i] = False
    dfs("")
    
    for number in hashset:
        is_prime = True
        if number < 2:
            continue
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1
    return answer


def solution(numbers):
    '''
    개선점: 숫자의 제곱근까지만 나눠서 소수를 구함
    '''
    hashset = set()
    visited = [False] * len(numbers)
    answer = 0
    
    def dfs(cur_str):
        if cur_str != "":
            hashset.add(int(cur_str))
            
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                dfs(cur_str + numbers[i])
                visited[i] = False
    dfs("")
    
    for number in hashset:
        is_prime = True
        if number < 2:
            continue
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1
    return answer

'''
key takeaways:
1. 모든 조합을 찾는 경우 재귀함수를 통해 쉽게 해결할 수 있다
2. Recursive Tree를 그리는 것이 도움이 될 수 있다
3. 소수를 구할 때, 모든 수를 나눌 필요 없이 제곱근까지만 나눠봐도 소수인지 확인할 수 있기 때문에, 이로써 성능을 향상시킬 수 있다.
  - 제곱근까지만 나눠봐도, 이후에 나눠 떨어질 가능성이 있는 숫자들은 이미 이전에 계산했던 숫자의 짝꿍밖에 안 남게 되기 때문
'''
# 주피터 노트북
- Anaconda prompt -> jupyter-notebooke 입력

# TYPE
- '가나다': String 문자열
- 123: int 숫자
- True, False: bool 불린
- (): tuple 투플
- {}: dict 딕셔너리
- []: list 리스트

# 연산자
- +: 더하기
- -: 빼기
- *: 곱하기
- /: 나누기
- %: 나머지
- //: 정수만 나오도록 나누기
- ** : 제곱
- A += B: A에 B를 더해서 나온 값
- A -= B: A에 B를 빼고 나온 값
- A *= B: A에 B를 곱해서 나온 값
- A /= B: A에 B를 나누고 나온 값
- A //= B: A에 B를 나누고 나온 값
- A %= B: A에 B를 나누고 나온 나머지 값

# .format()
"내 이름 {}, 주소{}, 나이{}" .format(AAA, BBB, CCC)
-> 내이름 AAA, 주소 BBB, 나이CCC 출력
"내 이름 {0}, 주소{2}, 나이{1}" .format(AAA, CCC, BBB)
-> 내이름 AAA, 주소 BBB, 나이CCC 출력

fruit = 'apple'
cost = '$3'
f'{fruit} cost {cost}'
-> 'apple cost $3' 출력

# 문자열 객체
- 'AAA' .upper(): AAA의 모든 문자를 대문자로 변환
- 'AAA'.swapcase(): AAA의 대문자 소문자를 반대로 전환
- "AAA".capitalize(): 첫문자를 대문자로 변환하고 이후 문자를 소문자로 변환
- " AAA ".strip(): 양쪽 빈공간을 삭제
    - \n\r 또한 삭제
    - " AAA\n\r".lstrip(): 왼쪽 공간만 삭제
    - " AAA\n\r".rstrip(): 오른쪽 공간만 삭제
- len(" AAA "): 문자 수를 출력
- " AAA\n\r".replace('BB','CC'): 문자열 AAA 안에 있는 BB를 CC로 전환
- " AAA\n\r".find('BB'): 문자열 AAA 안에 BB가 몇번째 순서에 있는지 출력
- AAA = ['a','b','c']  #리스트
    - "#".join(AAA) -> 'a#b#c' 출력
- 'AAA-BBB'.split('-') -> ['AAA','BBB'] 출력
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

# 입출력
AAA = input(BBB):

# .format()
"내 이름 {}, 주소{}, 나이{}" .format(AAA, BBB, CCC)
-> 내이름 AAA, 주소 BBB, 나이CCC 출력
"내 이름 {0}, 주소{2}, 나이{1}" .format(AAA, CCC, BBB)
-> 내이름 AAA, 주소 BBB, 나이CCC 출력

fruit = 'apple'
cost = '$3'
f'{fruit} cost {cost}'
-> 'apple cost $3' 출력

문자열: %s
숫자: %d
소수: %.Af(A: 소수점 아래 몇번째까지 나타내는지에 대한 값)

# if 제어문
if AAA:
    BBB
elif CCC:
    DDD
else: EEE
- AAA가 True라면 BBB를 실행
- AAA가 False고 CCC가 True라면 DDD 실행
- AAA와 CCC 둘 다 False라면 EEE 실행

# for 제어문
for i in range(AAA):
    BBB
- range를 통해 범위를 설정하여 그만큼 i를 반복해서 BBB에 넣고 실행
for i in range(CCC, DDD):
    BBB
- AAA부터 DDD의 앞까지 i를 반복해서 BBB에 넣고 실행
# 문자열 매소드
- 'AAA' .upper(): AAA의 모든 문자를 대문자로 변환
- 'AAA' .lower(): AAA의 모든 문자를 소문자로 변환
- 'AAA'.swapcase(): AAA의 대문자 소문자를 반대로 전환
- "AAA".capitalize(): 첫문자를 대문자로 변환하고 이후 문자를 소문자로 변환
= 'AAA' .title(): 각 단어의 첫 글자를 대문자로 변환
- " AAA ".strip(): 양쪽 빈공간을 삭제
    - \n\r 또한 삭제
    - " AAA\n\r".lstrip(): 왼쪽 공간만 삭제
    - " AAA\n\r".rstrip(): 오른쪽 공간만 삭제
- 'AAA' .replace(a, b): 문자열 AAA의 문자a를 문자b로 변환
- '{}AA'.format(a): {}부분에 a를 대입
- len(" AAA "): 문자 수를 출력
- " AAA\n\r".find('BB'): 문자열 AAA 안에 BB가 몇번째 순서에 있는지 출력
- 'AAA' .join(BBB): 리스트 BBB의 각 인자 사이에 AAA를 대입
- 'ABC' .split(B): 문자열 ABC를 문자 B로 나누어 [A, c]를 출력
    - 'AAA-BBB'.split('-') -> ['AAA','BBB'] 출력
- 'AAA' .count(BBB): 문자열 AAA 안에 있는 문자 BBB의 갯수
- 'AAA' .find(BBB): 문자열 AAA 안에서 문자 BBB의 인덱스 값을 출력
- 'AAA' .rfind(BBB): 문자열 AAA 안에서 문자 BBB의 인덱스 값을 뒤에서부터 찾아서 출력
- 'AAA' .index(BBB): 문자열 AAA 안에서 문자 BBB의 인덱스 값을 출력(없으면 예외를 발생)
# True와 False 값을 리턴하는 매소드
- 'AAA' .isalnum(): AAA가 알파벳 또는 숫자인가?
- 'AAA' .isalpha(): AAA가 알파벳인가?
- 'AAA' .isdecimal(): AAA가 숫자(decimal)인가?
- 'AAA' .isdigit(): AAA가 숫자(digit)인가?
- 'AAA' .isidentifier(): AAA가 식별자로 사용 가능한가?
- 'AAA' .islower(): AAA가 소문자인가?
- 'AAA' .isupper(): AAA가 대문자인가?
- 'AAA' .isnumeric(): AAA가 숫자인가?
- 'AAA' .isspace(): AAA가 공백인가?
- 'AAA' .istitle(): AAA가 title형식(단어마다 첫 글자가 대문자)인가? 
- 'AAA' .startwith(BBB): 문자열 AAA가 BBB로 시작하는가?
- 'AAA' .endwith(BBB): 문자열 AAA가 BBB로 끝나는가?

# 모듈 라이브러리
importA: A를 가져오기
from A import B

# 튜플과 리스트의 차이
리스트와 달리 튜플은 추가 및 변경 불가

# 딕셔너리
키(key)와 값(value)으로 구성
A = {AAA: BBB, CCC: DDD}

# 지역변수와 전역변수
지역변수: 함수 안에서 선언된 변수
전역변수: 메인 루틴에서 사용되는 변수

함수를 사용할 때 함수 안에 지역변수가 없고 local 값을 함수에 주지 않으면 변수에 맞는 전역변수를 사용하여 함수 작동
# 자료 총 정리 중

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
```py
"내 이름 {}, 주소{}, 나이{}" .format(AAA, BBB, CCC)
```
-> 내이름 AAA, 주소 BBB, 나이CCC 출력
```py
"내 이름 {0}, 주소{2}, 나이{1}" .format(AAA, CCC, BBB)
```
-> 내이름 AAA, 주소 BBB, 나이CCC 출력

```Python
fruit = 'apple'
cost = '$3'
f'{fruit} cost {cost}'
```
-> 'apple cost $3' 출력

문자열: %s
숫자: %d
소수: %.Af(A: 소수점 아래 몇번째까지 나타내는지에 대한 값)

# if 제어문
```Python
if AAA:
    BBB
elif CCC:
    DDD
else: EEE
```
- AAA가 True라면 BBB를 실행
- AAA가 False고 CCC가 True라면 DDD 실행
- AAA와 CCC 둘 다 False라면 EEE 실행

# for 제어문
```Python
for i in range(AAA):
    BBB
```
- range를 통해 범위를 설정하여 그만큼 i를 반복해서 BBB에 넣고 실행
```Python
for i in range(CCC, DDD):
    BBB
```
- AAA부터 DDD의 앞까지 i를 반복해서 BBB에 넣고 실행
# 문자열 매소드
- `'AAA' .upper()`: AAA의 모든 문자를 대문자로 변환
- `'AAA' .lower()`: AAA의 모든 문자를 소문자로 변환
- `'AAA'.swapcase()`: AAA의 대문자 소문자를 반대로 전환
- `"AAA".capitalize()`: 첫문자를 대문자로 변환하고 이후 문자를 소문자로 변환
= `'AAA' .title()`: 각 단어의 첫 글자를 대문자로 변환
- `" AAA ".strip()`: 양쪽 빈공간을 삭제
    - \n\r 또한 삭제
    - `" AAA\n\r".lstrip()`: 왼쪽 공간만 삭제
    - `" AAA\n\r".rstrip()`: 오른쪽 공간만 삭제
- `'AAA' .replace(a, b)`: 문자열 AAA의 문자a를 문자b로 변환
- `'{}AA'.format(a)`: {}부분에 a를 대입
- `len(" AAA ")`: 문자 수를 출력
- `" AAA\n\r".find('BB')`: 문자열 AAA 안에 BB가 몇번째 순서에 있는지 출력
- `'AAA' .join(BBB)`: 리스트 BBB의 각 인자 사이에 AAA를 대입
- `'ABC' .split(B)`: 문자열 ABC를 문자 B로 나누어 [A, c]를 출력
    - `'AAA-BBB'.split('-')` -> ['AAA','BBB'] 출력
- `'AAA' .count(BBB)`: 문자열 AAA 안에 있는 문자 BBB의 갯수
- `'AAA' .find(BBB)`: 문자열 AAA 안에서 문자 BBB의 인덱스 값을 출력
- `'AAA' .rfind(BBB)`: 문자열 AAA 안에서 문자 BBB의 인덱스 값을 뒤에서부터 찾아서 출력
- `'AAA' .index(BBB)`: 문자열 AAA 안에서 문자 BBB의 인덱스 값을 출력(없으면 예외를 발생)
# True와 False 값을 리턴하는 매소드
- `'AAA' .isalnum()`: AAA가 알파벳 또는 숫자인가?
- `'AAA' .isalpha()`: AAA가 알파벳인가?
- `'AAA' .isdecimal()`: AAA가 숫자(decimal)인가?
- `'AAA' .isdigit()`: AAA가 숫자(digit)인가?
- `'AAA' .isidentifier()`: AAA가 식별자로 사용 가능한가?
- `'AAA' .islower()`: AAA가 소문자인가?
- `'AAA' .isupper()`: AAA가 대문자인가?
- `'AAA' .isnumeric()`: AAA가 숫자인가?
- `'AAA' .isspace()`: AAA가 공백인가?
- `'AAA' .istitle()`: AAA가 title형식(단어마다 첫 글자가 대문자)인가? 
- `'AAA' .startwith(BBB)`: 문자열 AAA가 BBB로 시작하는가?
- `'AAA' .endwith(BBB)`: 문자열 AAA가 BBB로 끝나는가?

# 모듈 라이브러리
importA: A를 가져오기
`from A import B`

# 리스트

### 요소 추가
- `list.append(A)`: 리스트 안에 A를 추가(하나의 요소(index)만 추가 가능)
- `list.extend(A)`: 리스트 안에 A를 넣어 확장
- `list.insert(A,B)`: 특정 인덱스(A)에 요소(B)를 추가

### 요소 삭제
- `list.pop(A)`: 리스트의 마지막 요소 혹은 해당 index(A) 값을 삭제
- `list.remove(A)`: 리스트에서 리스트값 A를 삭제 
- `list.clear()`: 리스트의 모든 요소 삭제

### 특정 값의 인덱스 구하기
- `list.index(A)`: 리스트에서 리스트값 A의 index값 출력

### 특정 값의 갯수 구하기
- `list.count(A)`: 리스트에서 리스트값 A의 갯수 구하기

### 리스트의 순서 뒤집기
- `list.reverse()`: 리스트값의 순서를 뒤집어서 뒤에서부터 출력

### 리스트의 요소 정리
- `list.sort()`: 리스트값을 작은 수부터 차례대로 변경하여 정렬
- `list.sort(reverse=True)`: 리스트값을 큰 수부터 차례대로 변경하여 정렬
- `list.sorted()`: 리스트값을 작은 수부터 차레대로 생성하여 정렬

# 튜플과 리스트의 차이
리스트와 달리 튜플은 추가 및 변경 불가

# 딕셔너리
키(key)와 값(value)으로 구성
`A = {AAA: BBB, CCC: DDD}`

# 지역변수와 전역변수
지역변수: 함수 안에서 선언된 변수
전역변수: 메인 루틴에서 사용되는 변수

함수를 사용할 때 함수 안에 지역변수가 없고 local 값을 함수에 주지 않으면 변수에 맞는 전역변수를 사용하여 함수 작동

# 파일쓰기
C라이브러리에서 OS를 통해 하드웨어의 파일을 열었을 때 쓰고 난 뒤에 종료하는 거 중요! 
- r: 읽기 모드
- w: 쓰기 모드
- a: 추가 모드
- x: 파일 생성 후 쓰기 모드
- b: 바이너리 모드(순수 비트 파일)
- t: 텍스트 모드(유니코드)

`file = open('파일이름','r/w/a','b/t')`
`file.write('AAA')`
`file.readline()`: 파일을 한줄씩 읽기
`file.readlines()`: 모든 파일을 읽기
- `file.seek`,`file.tell`을 통해 파일 위치를 탐색/이동 가능
- `with open('AAA','B',C) as file:`을 통해 close()할 필요 없이 사용 가능

# 내장함수

### math 모듈
- `math.floor()`: 소수점 이하를 절삭
- `math.ceil()`: 무조건 올림
- `math.factorial()`: 팩토리알 값을 구함
- `math.sin()`: 사인 값을 구함(Radian)
- `math.cos()`: 코사인 값을 구함(Radian)
- `math.tan()`: 탄젠트 값을 구함(Radian)
- `math.pow()`: 거듭제곱 값을 구함
- `math.log10()`: 밑이 10인 로그 값을 구함
- `math.pi`: 파이값(3.141592...)

### datetime 모듈
```python
datetime.strftime()
```
- `%Y`: 네 자리 연도
- `%y`: 두 자리 연도
- `%m`: 월
- `%d`: 일
- `%A`: 요일(Monday, Tuesday...)
- `%a`: 생략 요일(Mon, Tues...)
- `%H`: 시(24기준)
- `%I`: 시(12기준)
- `%p`: AM 또는 PM
- `%M`: 분
- `%S`: 초
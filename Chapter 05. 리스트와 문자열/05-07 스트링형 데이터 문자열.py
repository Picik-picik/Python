Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 05-7 스트링형 데이터 : 문자열
>>> 
>>> # 파이썬에서 문자열을 표현하는 방법은 다음과 같이 큰따옴표로 묶는 것이다.
>>> 
>>> "Happy birthday to you"
'Happy birthday to you'
>>> 
>>> # 그런데 다음과 같이 작은 따옴표로 묶어서 문자열을 표현할 수도 있다. 그래서 위의 경우 문자열을 큰따옴표로 묶었지만
>>> # 출력 결과에서는 작은따옴표로 묶여서 출력되었다. (무엇으로 문자열을 묶던 차이는 없다.)
>>> 
>>> 'Happy birthday to you'
'Happy birthday to you'
>>> 
>>> # 그리고 문자열은 그 자체로 문자들을 묶어 놓은 데이터이다. 그래서 다음과 같이 숫자를 묶어서 문자열을 표현하면,
>>> # 이는 정수가 아닌 문자들의 모임 즉 문자열로 인식이 된다.
>>> 
>>> "235"
'235'
>>> 
>>> # 그럼 문자열도 파이썬이 인식하는 데이터의 한 종류임을 확인하기 위해서, 더불어 문자열의 데이터형을 확인하기 위해서
>>> # 문자열을 전달하면서 type 함수를 호출해보자.
>>> 
>>> type('what1')	# 작은따옴표로 묶은 문자열
<class 'str'>
>>> type("what2")	# 큰따옴표로 묶은 문자열
<class 'str'>
>>> 
>>> # 위의 type 함수 호출 결과로 출력된 <class 'str'>은 전달된 값이 '스트링형 데이터'임을 의미한다.
>>> # ('스트링형 데이터'라는 표현보다 '문자열'이라는 표현을 많이 쓴다.) 이로써 지금까지 파이썬을 통해 접한 데이터의 종류는 다음과 같이 네 가지가 되었다.
>>> 
>>> #	* int형 데이터		ex) 3, 5, 7, 9
>>> #	* float형 데이터		ex) 2.2, 4.4, 6.6, 8.8
>>> #	* 리스트형 데이터	ex) [3, 5, 7, 9], [2.2, 4.4, 6.6, 8.8]
SyntaxError: invalid syntax
>>> #	* 스트링형 데이터	ex) "I am a boy", 'You are a girl'
>>> 
>>> # 그리고 느꼈는지 모르겠지만, 문자열은 리스트와 다음 측면에서 상당히 유사하다.
>>> 
>>> #	"하나 이상의 값을 묶어서(모아서) 만들어지는 데이터"
>>> 
>>> # 예를 들어서 3과 5라는 값을 묶어서 리스트를 만들 수 있는 것처럼,
>>> 
>>> [3, 5]
[3, 5]
>>> 
>>> # 문자 A와 Z를 묶어서 다음과 같은 문자열을 만들 수 있다.
>>> "AZ"
'AZ'
>>> 
>>> # 이렇듯 리스트와 문자열은 상당 부분 유사하기 때문에 리스트를 대상으로 했던 연산 대부분을 문자열을 대상으로도 할 수 있다.
>>> # 그럼 먼저 덧셈 연산의 예와 그 결과를 보이겠다.
>>> 
>>> [1, 2] + [3, 4]	# 두 리스트를 합한(연결한) 결과가 만들어진다.
[1, 2, 3, 4]
>>> "Hello" + "Everybody"	# 두 문자열을 합한(연결한) 결과가 만들어진다.
'HelloEverybody'
>>> [1, 2] * 3 	# 리스트를 세 배 늘린 결과가 만들어진다.
[1, 2, 1, 2, 1, 2]
>>> "AZ" * 3 	# 문자열을 세 배 늘린 결과가 만들어진다.
'AZAZAZ'
>>> 
>>> # 그리고 리스트와 마찬가지로 문자열을 가지고도 '인덱싱 연산'과 '슬라이싱 연산'을 할 수 있다. 물론 연산의 방식과 결과도 완전히 동일하다.
>>> 
>>> st = [1, 2, 3, 4, 5]
>>> st[2]	# 세 번째 위치의 값만 뽑아 냄
3
>>> str = "SIMPLE"
>>> str[2]	# 세 번째 위치의 값만(문자만) 뽑아 냄
'M'
>>> 
>>> st = [1, 2, 3, 4, 5, 6, 7]
>>> st[2 : 5]	# 인덱스 값이 2 ~ 4인 위치의 값들 뽑아 냄
[3, 4, 5]
>>> str = "SIMPLEST"
>>> st[2 : 5]	# 인덱스 값이 2 ~ 4인 위치의 값을 뽑아 냄
[3, 4, 5]
>>> str[2 : 5]	# 인덱스 값이 2 ~ 4인 위치의 값을 뽑아 냄
'MPL'
>>> 
>>> # 단, 리스트와 달리 문자열은 그 내용을 바꾸지 못한다. (이거 매우 중요한 사실이다.) 따라서 다음과 같이 문자열의 일부를 바꾸는 연산을 하면 오류가 발생한다.
>>> 
>>> str = "Happy"
>>> str[0] = "D"	# 이렇게 문자열의 일부를 바꿀 수 없다니까!
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    str[0] = "D"	# 이렇게 문자열의 일부를 바꿀 수 없다니까!
TypeError: 'str' object does not support item assignment
>>> 
>>> # 이 사실에 주의하자. 문자열을 리스트와 달리 그 내용을 바꾸지 못한다는 사실 말이다.
>>> 
>>> 
#
>>> # [연습문제 05-3]
>>> str = "Hello"
>>> str += " Python"
>>> str
'Hello Python'
>>> 
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 04-4 복합 대입 연산자
>>> 
>>> # 설명하는 김에 두 가지 연산자를 더 소개하겠다. 먼저 다음 예를 보자.
>>> 
>>> num = 10
>>> num = num + 1 	# num의 값을 1 증가
>>> print(num)
11
>>> 
>>> #	num = num + 1
>>> 
>>> # 위의 경우 + 연산이 먼저 진행된다. 따라서 덧셈 결과가 num에 저장되어 결국 num에 저장된 값이
>>> # 1 증가하는 결과로 이어진다. 그런데 위의 문장은 다음과 같이 줄여서 쓸 수도 있다.
>>> 
>>> num = 10
>>> num += 1 		# num = num + 1을 줄인 표현
>>> print(num)
11
>>> 
>>> # 정리하면, 다음 두 문장은 완전히 동일하다.
>>> 
>>> #	num = num + 1   vs.   num += 1
>>> 
>>> # 마찬가지로 다음 두 문장도 완전히 동일하다.
>>> 
>>> #	num = num - 1   vs.   num -= 1
>>> 
>>> # 이쯤 되면 규칙이 눈에 보이지 않는가? 다음 두 문장도 마찬가지로 동일하다.
>>> 
>>> #	num = num * 3   vs.   num *= 3
>>> 
>>> 
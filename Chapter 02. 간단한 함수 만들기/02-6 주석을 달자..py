Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 02-6 주석을 달자.
>>> # 소스코드에는 '주석(comment)'이라는 것을 달아서 코드가 의미하는 바를 남겨둘 수 있다.
>>> # 주석이 달린 예는 다음과 같다.
>>> # adder1.py
>>> def adder(num1, num2):	# 함수 adder의 정의
	return num1 + num2 	# num1과 num2의 덧셈 결과를 넘김

>>> print(adder(5, 3))		# adder 함수 호출, 그리고 그 결과 출력
8
>>> 
>>> # 이렇듯 #이 달리면 그 뒤에(그 오른쪽에) 등장하는 내용은 프로그램의 일부로 인식되지 않고 무시된다.
>>> # 즉 위에 등장하는 다음 내용들은,
>>> 
>>> # adder1.py
>>> # 함수 adder의 정의
>>> # num1과 num2의 덧셈 결과를 넘김
>>> # adder 함수 호출, 그리고 그 결과 출력
>>> 
>>> #우리들 눈에는 보이지만 파이썬은 이를 무시한다. 그래서 실행될 내용에서 제외된다.
>>> # 따라서 적절히 주석을 달아 놓아서 코드를 이해하는데 도움을 줄 수 있다.
>>> 
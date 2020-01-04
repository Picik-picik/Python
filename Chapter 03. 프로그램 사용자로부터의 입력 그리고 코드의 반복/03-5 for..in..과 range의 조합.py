Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 03-5 for..in..과 range의 조합
>>> 
>>> # 앞서 1부터 10까지의 합을 구하는 for 루프를 만들어봤다.
>>> # 그때 다음의 내용을 입력하면서 힘들지 않았는가?
>>> 
>>> # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> # 힘들지 않았다면 1부터 100까지의 합을 구하는 for 루프를 만들어보자.
>>> # 그러면 이런 식의 코드 입력에 한계가 있음을 느낄 것이다. 그렇다면 대안이 있을까?
>>> # 물론이다. 다음과 같이 for와 range의 조합을 만들면 된다.
>>> 
>>> sum = 0
>>> for i in range(1, 11):	# for 루프와 range의 조합
	sum = sum * i

	
>>> print(sum)
0
>>> for i in range(1, 11):	# for 루프와 range의 조합
	sum = sum + i

	
>>> print(sum)
55
>>> 
>>> # 위의 예에서 보이듯이 for 루프에서 다음 둘이 의미하는 바는 같다.
>>> 
>>> # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] vs. range(1, 11)
>>> 
>>> # 그러니까 위 예의 range(1, 11)를 다음과 같이 이해하자.
>>> 
>>> # range(1, 11)
>>> #	→ for의 변수 i에 1부터 11 이전의 값까지 넣어서 반복을 진행하라는 의미
>>> 
>>> #따라서 1부터 100까지의 합을 구하는 for 루프는 다음과 같이 작성하면 된다.
>>> 
>>> sum = 0
>>> for i in range(1, 101):	# 변수에 1부터 (101-1)까지 넣어서 반복
	sum = sum + i

	
>>> print(sum)
5050
>>> 
>>> 
>>> # 그리고 for 루푸의 변수 i가 다음 예에서 보이듯이 그저 반복의 횟수를 세는 목적으로만 사용된다면,
>>> # 이 변수의 값은 1이 아닌 0에서부터 시작하도록 코드를 작성하는 것이 좋다.
>>> 
>>> for i in range(0, 3):	# 3회 반복이 목적입니다. i에는 0, 1, 2가 들어갑니다.
	print("Happy")

	
Happy
Happy
Happy
>>> 
>>> # 물론 위의 경우 range(0, 3)을 대신해서 range(1, 4) 또는 range(2, 5)를 넣어도 결과는 같지만,
>>> # 이렇듯 단순히 반복 횟수를 명시하는 것이 목적인 경우에는 range() 안의 첫 번째 숫자를 0으로
>>> # 두는 것이 관례이다. 그래야 두 번째 숫자만 보고도 몇 번 반복하는지 알 수 있기 때문이다.
>>> # 그리고 다음에서 보이듯이 range(0, 3)은 range(3)으로 줄여서 쓸 수 있다.
>>> 
>>> for i in range(3):	# range(3)은 range(0, 3)과 같다. 즉 '3회 반복'의 의미 가짐
	print("Happy")

	
Happy
Happy
Happy
>>> 
>>> # 물론 range에 변수도 넣을 수 있다. 필요한 경우에는 다음과 같이 변수를 기반으로 반복 횟수를 결정할 수도 있다.
>>> 
>>> cnt = 2
>>> for i in range(cnt):	# cnt만큼 반복
	print("I love coffee")

	
I love coffee
I love coffee
>>> 
>>> # 이 정도 했으면 그래도 파이썬의 맛은 봤다고 할 수 있다. 그리고 여기까지 잘 왔다면 이 책을 마지막까지 공부하는데
>>> # 큰 무리가 없을 것이다.
>>> 
>>> # [연습문제 03-4]
>>> 
>>> # 문제 1
>>> for i in range(5):
	print("안녕하세요.")

	
안녕하세요.
안녕하세요.
안녕하세요.
안녕하세요.
안녕하세요.
>>> 
>>> for i int range(1, 10):
	
SyntaxError: invalid syntax
>>> 
>>> # 문제 2
>>> for i in range(1, 10):
	print("7 X", i, "=", 7 * i)

	
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
>>> 
>>> # 문제 3
>>> def exp(x, y):
	rit = 1
	for i in range(y)
	
SyntaxError: invalid syntax
>>> def exp(x, y):
	rit = 1
	for i in range(y):
		rit = rit * x
	return rit

>>> exp(2, 3)
8
>>> exp(3, 4)
81
>>> exp(4, 4)
256
>>> 
>>> # 문제 4
>>> def greet()
SyntaxError: invalid syntax
>>> def greet():
	num = eval(input("인사를 몇 번 할까요? "))
	for i in range(num)
	
SyntaxError: invalid syntax
>>> def greet():
	num = eval(input("인사를 몇 번 할까요? "))
	for i in range(num):
		print("반갑습니다.")

		
>>> greet(3)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    greet(3)
TypeError: greet() takes 0 positional arguments but 1 was given
>>> greet()
인사를 몇 번 할까요? 2
반갑습니다.
반갑습니다.
>>> greet()
인사를 몇 번 할까요? 5
반갑습니다.
반갑습니다.
반갑습니다.
반갑습니다.
반갑습니다.
>>> 
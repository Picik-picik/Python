Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 04-5 소괄호
>>> 
>>> # 수학에서 소괄호는 연산의 순서를 결정하는 중요한 역할을 한다. 예를 들어서 다음 수식의 계산 결과는
>>> # 나눗셈을 먼저 진행하기 때문에 5이다.
>>> 
>>> #	3 + 4 ÷ 2 = 5
>>> 
>>> # 하지만 다음과 같이 소괄호를 해주면 덧셈을 먼저 하기 때문에 결과는 달라진다.
>>> 
>>> #	(3 + 4) ÷ 2 = 3.5
>>> 
>>> # 파이썬에서도 이러한 의미로 소괄호가 존재한다. (사실 1장에서 이미 한 번 써봤다.)
>>> # 즉 파이썬의 소괄호는 수학에서 사용하는 소괄호와 그 의미가 같다.
>>> 
>>> 3 + 4 /2
5.0
>>> (3 + 4) / 2
3.5
>>> 
>>> # [연습문제 04-1]
>>> 
>>> # 문제 1
>>> def int_div(num1, num2):
	print(num1 // num2)
	print(num1 % num2)

	
>>> int_div(5, 2)	# 5 나누기 2의 몫과 나머지는?
2
1
>>> def int_div(num1, num2):
	print("몫 :", num1 // num2)
	print("나머지 :", num1 % num2)

	
>>> int_div(5, 2)	# 5 나누기 2의 몫과 나머지는?
몫 : 2
나머지 : 1
>>> 
>>> # 문제 2
>>> def bet_sum(num1, num2):
	for i in range(num1, num2 + 1)
	
SyntaxError: invalid syntax
>>> def bet_sum(num1, num2):
	for i in range(num1, num2 + 1):
		sum += i

		
>>> print(sum)
<built-in function sum>
>>> def bet_sum(num1, num2):
	for i in range(num1, num2 + 1):
		sum += i
	print(sum)

	
>>> bet_sum(2, 5)	# 2와 5 사이의 수 3과 4의 합은?
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    bet_sum(2, 5)	# 2와 5 사이의 수 3과 4의 합은?
  File "<pyshell#41>", line 3, in bet_sum
    sum += i
UnboundLocalError: local variable 'sum' referenced before assignment
>>> def bet_sum(num1, num2):
	sum = 0
	for i in range(num1, num2 + 1):
		sum += i
	print(sum)

	
>>> bet_sum(2, 5)	# 2와 5 사이의 수 3과 4의 합은?
14
>>> def bet_sum(num1, num2):
	for i in range(num1 + 1, num2):
		sum += i
	print(sum)

	
>>> bet_sum(2, 5)	2와 5 사이의 수 3과 4의 합은?
SyntaxError: invalid syntax
>>> bet_sum(2, 5)	2와 5 사이의 수 3과 4의 합은?
SyntaxError: invalid syntax
>>> bet_sum(2, 5)	# 2와 5 사이의 수 3과 4의 합은?
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    bet_sum(2, 5)	# 2와 5 사이의 수 3과 4의 합은?
  File "<pyshell#52>", line 3, in bet_sum
    sum += i
UnboundLocalError: local variable 'sum' referenced before assignment
>>> # 문제 2
>>> def bet_sum(num1, num2):
	sum = 0
	for i in range(num1 + 1, num2):
		sum += i
	print(sum)

	
>>> bet_sum(2.5)		# 2와 5 사이의 수 3과 4의 합은?
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    bet_sum(2.5)		# 2와 5 사이의 수 3과 4의 합은?
TypeError: bet_sum() missing 1 required positional argument: 'num2'
>>> bet_sum(2, 5)		# 2와 5 사이의 수 3과 4의 합은?
7
>>> bet_sum(2, 5)	# 2와 5 사이의 수 3과 4의 합은?
7
>>> bet_sum(1, 5)	# 1과 5 사이의 수 2, 3, 4의 합은?
9
>>> 
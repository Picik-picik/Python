Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 05-10 리스트와 문자열을 인자로 전달하고 반환하기
>>> 
>>> # 앞서 우리는 다음과 같이 int형 값을 전달받거나 반환하는 함수를 만든 바 있다.
>>> 
>>> def so_simple1(num):		# 매개변수 num을 통해 값을 받음
	return num + 1 		# num + 1의 결과 반환

>>> n = so_simple1(7)		# 함수 호출하면서 7 전달, 그리고 반환되는 값 n에 저장
>>> n
8
>>> 
>>> # 이와 마찬가지로 다음과 같이 함수의 매개변수에 리스트도 인자로 전달할 수 있다.
>>> 
>>> def so_simple2(st):
	print(st)	# 매개변수 st로 전달된 대상을 출력함

	
>>> so_simple2([1, 3, 5])	# 리스트를 전달하면서 함수 호출
[1, 3, 5]
>>> 
>>> # 뿐만 아니라 다음과 같이 함수 내에서 리스트를 반환할 수도 있다.
>>> 
>>> def so_simple3():
	st = [1, 2, 3, 4, 5]
	return st 	# 리스트를 반환한다.

>>>  r = so_simple3()	# 반환되는 리스트를 변수 r에 저장
 
SyntaxError: unexpected indent
>>> r = so_simple3()	# 반환되는 리스트를 변수 r에 저장
>>> r
[1, 2, 3, 4, 5]
>>> 
>>> # 이는 문자열도 마찬가지다. 다음 예에서 보이듯이 문자열도 함수에 전달이 가능하고 또 반환도 가능하다.
>>> # (사실 우리는 이미 문자열을 함수의 인자로 전달해 본 경험이 있다.)
>>> 
>>> def so_simple4(s):
	print(s)
	return "Bye~"	# 문자열 "Bye~"를 반환

>>> r = so_simple4("Hello")	# 문자열 "Hello"를 전달, 그리고 반환되는 값 r에 저장
Hello
>>> r 	# 반환된 결과물 출력함
'Bye~'
>>> 
>>> # [연습문제 05-4]
>>> 
>>> # 문제 1
>>> def sum_all(st):
	for i in range(len(st))
	
SyntaxError: invalid syntax
>>> def sum_all(st):
	sum = 0
	for i in range(len(st)):
		sum += st[i]
		return sum

	
>>> sum_all([1, 2, 3, 4, 5])
1
>>> def sum_all(st):
	sum = 0
	for i in range(len(st)):
		sum += st[i]
	return sum

>>> sum_all([1, 2, 3, 4, 5])
15
>>> 
>>> # 문제 2
>>> def show_reverse(st):
	for i in range(len(st)):
		print(st[(i + 1) * -1], end = ' ')

		
>>> show_reverse([1, 2, 3, 4, 5])
5 4 3 2 1 
>>> show_reverse("ABCDEFG")
G F E D C B A 
>>> 
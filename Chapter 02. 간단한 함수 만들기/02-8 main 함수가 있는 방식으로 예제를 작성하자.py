Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 02-8 main 함수가 있는 방식으로 예제를 작성하자
>>> 
>>> # 앞서 소스파일에 담았던 다음 예를 다시 보자.
>>> # adder1.py
>>> def adder(num1, num2):	# 함수 adder의 정의
	return num1 + num2

>>> print(adder(5, 3))		# 위에 정의된 adder 함수의 호출과 print 함수의 호출
8
>>> 
>>> # 위의 내용을 실행시키면 먼저 adder 함수가 정의되고, 이어서 다음 문장에 의해서 adder 함수가 호출이 된다.
>>> 
>>> # print(adder(5, 3))
>>> 
>>> # 그런데 위의 예를 다음과 같은 방식으로도 작성할 수 있고 이것이 더 권장되는 방식이기도 한다.
>>> # adder2.py
>>> def adder(num1, num2):	# 함수 adder의 정의
	return num1 + num2

>>> def main():			# 프로그램의 실행 흐름을 담은 main 함수의 정의
	print(adder(5, 3))

	
>>> main()			# 위에 정의된 함수 main의 호출
8
>>> 
>>> # 위의 예에는 다음과 같은 특징이 있다.
>>> 
>>> # "프로그램의 실행 흐름을 담은 main이라는 이름의 함수를 별도로 정의하고 있다."
>>> 
>>> # 물론 소스파일에 담긴 내용은 위에서부터 아래로 실행되기 때문에, adder1.py와 같이 필요한 함수들
>>> # 을 먼저 정의하고 이어서 실행 흐름에 해당하는 문장들을 그냥 나열해도 된다.
>>> # 그러나 위와 같이 main함수에 실행 흐름에 해당하는 문장들을 담아 놓으면, 훨씬 정된된 느낌을 받을 수 있고
>>> # 또 관리하기도 좋아진다.
>>> # 자! 그럼 예제를 하나 더 소개하겠다. 이 예제의 경우 함수의 정의가 넷, 실행의 흐름을 이루는 문장도 넷인데
>>> # 이 네 개의 문장을 main 함수에 담았다.
>>> 
>>> # op4.py
>>> def add(num1, num2):	# add 함수의 정의
	return num1 + num2

>>> def min(num1, num2):		# min 함수의 정의
	return num1 - num2

>>> def mul(num1, num2):		# mul 함수의 정의
	return num1 * num2

>>> def div(num1, num2):		# div 함수의 정의
	return num1 / num2

>>> def main():			# 프로그램의 실행 흐름을 담고 있는 main  함수의 정의
	print(add(5, 3))
	print(min(5, 3))
	print(mul(5, 3))
	print(div(5, 3))

	
>>> main()			# main 함수의 호출
8
2
15
1.6666666666666667
>>> 
>>> # 그리고 위와 같이 main 함수를 정의하고 호출하는 방식으로 예제를 실행하면 main 함수의
>>> # 정의가 남아 있는 상태이기 때문에, 다음과 같이 main 함수의 호출을 다시 명령할 수 있다.
>>> 
>>> main()
8
2
15
1.6666666666666667
>>> 
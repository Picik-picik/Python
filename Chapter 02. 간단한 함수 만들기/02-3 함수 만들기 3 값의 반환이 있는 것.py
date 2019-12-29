Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 02-3 함수 만들기 3: 값의 반환이 있는 것
>>> 
>>> # 앞서 매개변수를 통해 함수로 값을 전달할 수 있음에 대해 살펴보았다.
>>> # 그런데 반대로 함수가 값을 되돌려 줄 수도 있다.
>>> def adder2(num1, num2):
	ar = num1 + num2
	return ar

>>> result = adder2(5, 3)
>>> print(result)
8
>>> 
>>> # 위 함수 내에서는 다음과 같이 변수 ar을 선언하고 num1과 num2의 합을 이 변수에 저장하였다.
>>> 
>>> # ar = num1 + num2
>>> 
>>> # 그리고 이어서 return으로 시작하는 다음 문장을 실행했는데,
>>> 
>>> # return ar
>>> 
>>> # 이는 변수 ar에 저장된 값을, 함수를 호출한 영역으로 되돌려주라는 뜻이다.
>>> # 따라서 다음과 같이 함수를 호출하면,
>>> # result = adder2(5, 3)
>>> 
>>> # 먼저 adder2 함수가 호출되고, 그 함수 안에서 되돌려 주는 값 8이 adder2(5, 3)을 대신하여 다음의 상태가 된다.
>>> # result = 8
>>> 
>>> # 그리고 이것이 바로 '함수를 호출한 영역으로 값을 되돌려 준 결과'이다.
>>> 
>>> # 이렇듯 함수가 되돌려 주는 값을 가리켜 '반환 값'이라 한다. 즉 return은 함수를 호출한 영역으로 값을 반환할 때
>>> # (되돌려 줄 때) 사용하는 명령어이다.
>>> # 그럼 이어서 다음 예를 보자. 이 예에서 정의한 함수 adder3은 앞서 정의한 함수 adder2와 완전히 동일하다.
>>> # 다만 문장의수를 줄여서 정의했을 뿐이다.
>>> 
>>> 
>>> def adder3(num1, num2):
	return num1 + num2

>>> print(adder3(5, 3))
8
>>> 
>>> # 위의 함수에서 보이듯이 return으로 시작하는 문장을 만들 수도 있다.
>>> # 그러면 덧셈이 먼저 진행되어 return num1 + num2 문장이 return 8로 된다.
>>> # 따라서 덧셈의 결과로 얻어진 값 8이 반환된다. 그리고 위 예에서는 다음과 같이 adder3 함수를 호출 했는데,
>>> 
>>> # print(adder3(5, 3))
>>> 
>>> # 모양새가 print 함수에 adder3(5, 3)을 전달하는 것처럼 보인다. 그러나 print 함수에 실제 전달되는 값은
>>> # adder3(5, 3)이 반환하는 값이다. 즉 위의 문장을 실행하면, 먼저 adder3이 호출되고
>>> # 그 결과로 8이 반환되어 다음과 같이 print 함수를 호출하게 된다.
>>> # print(adder3(5, 3)) → print(8)
>>> 
>>> #[연습문제 02-3]
>>> # 문제 1
>>> def reverse(num):
	return num
	return -num

>>> reverse(5)
5
>>> def reverse(num):
	return -num

>>> reverse(5)
-5
>>> reverse(-5)
5
>>> 
>>> # 문제 2
>>> def avg(num1, num2):
	return (num1 + num2) / 2

>>> print(avg(3, 4))
3.5
>>> 
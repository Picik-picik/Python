Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 03-2 입력받은 내용을 숫자로 바꾸려면
>>> 
>>> # 프로그램 사용자로부터 '문자열'이 아닌 '수'를 입력받으려면 어떻게 해야 할까?
>>> # 파이썬은 수를 입력받는 함수를 제공하지 않는다. 대신에 문자열의 내용을 수로 바꿀 때
>>> # 사용할 수 있는 함수를 제공하고 있다.
>>> 
>>> year = input("This year : ")
This year : 2020
>>> year = eval(year)	# year에 저장된 내용을 산술 연산이 가능한 '수'로 바꾼다.
>>> year = year + 1
>>> print("Next year :", year)
Next year : 2021
>>> 
>>> # 위 예에서는 다음과 같이 eval 함수를 호출하였다.
>>> 
>>> # year = eval(year)
>>> 
>>> # 이 문장이 실행되기 전 year에 저장된 내용은 문자열 "2020"이었다. 그런데 이를 eval 함수에
>>> # 전달하였고, 그 결과 eval 함수는 2020이라는 수를 반환하였다.
>>> # 즉 위 문장에서 eval 함수가 호출된 이후의 상태는 다음과 같다.
>>> 
>>> # year = 2020
>>> 
>>> # 그래서 다음과 같이 덧셈을 통해서 year에 저장된 값을 1 증가시킬 수 있었다.
>>> # 왜? year에 저장된 것은 '수(number)'이니까.
>>> 
>>> # year = year + 1
>>> 
>>> # 그런데 처음부터 수를 입력받는 것이 목적이었다면 다음의 두 문장을,
>>> 
>>> #   year = input("This year : ")
>>> #   year = eval(year)
>>> 
>>> # 다음과 같이 한 문장으로 구성할 수도 있다.
>>> 
>>> #   year = eval(input("This year : "))
>>> 
>>> # 위의 경우 input 함수가 먼저 호출되고, 그 결과로 반환되는 값이 eval 함수에 전달된다.
>>> # 따라서 이렇게 줄여서 표현할 수 있다. 그리고 당연한 얘기로 들리겠지만
>>> # eval 함수는 소수점 이하의 값을 갖는 실수를 대상으로도 잘 동작한다.
>>> 
>>> rad = eval(input("radius : "))
radius : 2.5
>>> area = rad * rad * 3.14		# 이는 원의 넓이 계산 공식을 적용한 문장입니다.
>>> print(area)
19.625
>>> 
>>> # 위의 예에서는 원의 넓이를 구하고 있는데, 그보다는 '입력받은 값으로 곱셈을 했다.'
>>> # 는 사실에 주목해야 한다. 곱셈을 했다는 것은 eval 함수가 2.5라는 수를 반환했다는 뜻이니까 말이다.
>>> 
>>> # [연습문제 03-2]
>>> str1 = eval(input("첫 번째 입력 : "))
첫 번째 입력 : 1.24
>>> str2 = eval(input("두 번째 입력 : "))
두 번째 입력 : 3.12
>>> print("두 입력의 합 :" + str1 + str2)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print("두 입력의 합 :" + str1 + str2)
TypeError: can only concatenate str (not "float") to str
>>> print("두 입력의 합 :" + (str1 + str2))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print("두 입력의 합 :" + (str1 + str2))
TypeError: can only concatenate str (not "float") to str
>>> str3 = str1 + str2
>>> print("두 입력의 합 :" + str3)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print("두 입력의 합 :" + str3)
TypeError: can only concatenate str (not "float") to str
>>> print("두 입력의 합 :", str3)
두 입력의 합 : 4.36
>>> str1 = eval(input("첫 번째 입력 : "))
첫 번째 입력 : 1.24
>>> str2 = eval(input("두 번째 입력 : "))
두 번째 입력 : 3.12
>>> print("두 입력의 합 :", str1 + str2)
두 입력의 합 : 4.36
>>> 
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Chapter 03. 프로그램 사용자로부터의 입력 그리고 코드의 반복
>>> # 03-1 프로그램 사용자로부터 입력받기
>>> 
>>> # 컴퓨터 프로그램의 중요한 기능 중 하나는 프로그램 사용자로부터 무언가를 입력받는 기능이다.
>>> 
>>> # 앞서 만든 adder2.py 덧셈 프로그램은 5와 3의 덧셈 결과만 출력한다. 그러니까 프로그램 사용자가 궁금해하는 내용에는 관심이 없다.
>>> # 물론 코드를 수정하면(adder에 전달하는 값을 수정하면) 원하는 덧셈 결과를 얻을 수 있다.
>>> # 그런데 그런 형태로 프로그램을 사용하라고는 할 수 없지 않은가? 다음과 같이 대화하듯 동작하도록 만들어야 하지 않겠는가?
>>> 
>>> #   컴퓨터 : 숫자 하나를 입력하세요.
>>> #   사용자 : 25
>>> #   컴퓨터 : 하나 더 입력해주세요.
>>> #   사용자 : 33
>>> #   컴퓨터 : 입력하신 두 수의 합은 58입니다. ^^
>>> 
>>> # 그렇다면 어떻게 해야 프로그램 사용자로부터 정보를 입력받을 수 있을까? 답은 함수에 있다.
>>> # 그런 기능을 제공하는 함수를 사용하면 된다. 그리고 다음 예에서 보이듯이 그 함수의 이름은 input이다.
>>> # 물론 이 함수는 파이썬이 미리 만들어서 제공하는 함수이다.
>>> 
>>> str = input("How old are you : ")	# 함수의 호출
How old are you : 12 years old
>>> print(str)
12 years old
>>> 
>>> # 우선 위 예의 첫 번째 문장이 실행되면 다음 상태가 된다.
>>> str = input("How old are you : ")	# input 호출하면서 "How old are you : " 전달
How old are you : 12
>>> # input 함수가 호출되면, 호출 할 때 인자로 전달된 문자열이 출력되면서 프로그램 사용자가 무엇인가를
>>> # 입력할 때까지 기다리게 된다. 따라서 이 상태에서는 무엇이든 키보드로 입력하고 입력의 끝을 의미하는
>>> # 엔터키를 눌러야 한다. 그러면 키보드로 입력된 내용을 input 함수가 반환한다.
>>> 
>>> # 입력된 내용을 input 함수가 '문자열의 형태
>>> # 입력된 내용을 input 함수가 '문자열의 형태'로 반환해서 다음의 상태가 된다.
>>> # (비록 숫자 12를 입력했지만 문자열 "12"가 반환되었음에 주목한다.)
>>> 
>>> # str = input("How old are you : ")
>>> #         ↓
>>> # str = "12"
>>> 
>>> # 이러한 input 함수는 누구나 쉽게 사용할 수 있다. 그러나 입력된 내용이 하나의 문자열로 묶여서 반환된다는 사실에 주의해야 한다.
>>> 
>>> # "input 함수는 입력된 내용을 하나의 문자열로 묶어서 반환한다."
>>> 
>>> # 그러니까 input 함수의 호출 결과는 다음과 같지 않고,
>>> 
>>> # str = 12
>>> 
>>> # 다음과 같다.
>>> 
>>> # str = "12"
>>> 
>>> # 그런데 파이썬은 '수'와
>>> 
>>> 3
>>> # 그런데 파이썬은 '수'와 '문자열'을 구분하기 때문에, 이렇듯 문자열의 상태로 반환된 결과를 가지고는 '산술 덧셈'을 할 수 없다.
>>> # 문자열을 가지고 덧셈을 할 경우 다음과 같이 문자열을 이어 붙이는 결과로 이어지기 때문이다.
>>> 
>>> num = "31" + "24"	# 이 덧셈은 두 문자열을 이어 붙이는 결과로 이어진다.
>>> print(num)
3124
>>> 
>>> # 즉, 다음 문장에서의 덧셈 결과는,
>>> 
>>> # num = "31" + "24"
>>> 
>>> # 다음과 같다.
>>> 
>>> # num = "3124"
>>> 
>>> # 그렇다면 이 문제는 어떻게 해결해야 할까? 어떻게 해야 input 함수가 읽어 들인 결과를 가지고 산술 덧셈을 할 수 있을까?
>>> # 그 방법에 대해서는 연습문제를 먼저 제공하고 이어서 소개하겠다.
>>> 
>>> # [연습문제 03-1]
>>> str1 = input("첫 번째 입력 : ")
첫 번째 입력 : 12
>>> str2 = input("두 번째 입력 : ")
두 번째 입력 : 34
>>> print("두 입력의 합 : " + str1 + str2)
두 입력의 합 : 1234
>>> 
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 05-2 리스트형 데이터
>>> 
>>> # 다음과 같이 프롬포트상에서 숫자를 입력하고 엔터키를 눌러보자.
>>> 
>>> 35
35
>>> 
>>> # 이렇듯 정수는 print 함수를 호출하지 않고 그냥 입력만 해도 출력이 된다.
>>> # 그리고 이는 35라는 값의 존재를 '파이썬이 데이터로 인식한다는 의미'이기도 하다.
>>> # 물론 'int형 값'으로 인식한다. 반면 다음과 같이 입력하면 오류가 발생한다.
>>> 
>>> Happy
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    Happy
NameError: name 'Happy' is not defined
>>> 
>>> # 이는 '당신이 입력한 Happy가 무엇인지 판단이 안됩니다.'라고 답하는 상황이다. 그럼 이번에는 실수를 입력해보자.
>>> 
>>> 3.14
3.14
>>> 
>>> # 역시 3.14는 'float형 값'으로 인식되기 때문에 입력한 값이 그대로 출력되었다.
>>> # 그렇다면 다음과 같이 for 루프를 작성할 때 사용하는 [1, 2, 3]을,
>>> 
>>> #	for i in [1, 2, 3]:
>>> #	   pass	# pass라고 입력하면 아무 일도 하지 않는 for 루프가 만들어집니다.
>>> 
>>> # 다음과 같이 입력하고 엔터키를 눌러보자. 그러면 출력 결과를 통해서 [1, 2, 3]도 데이터로 인식됨을 알 수 있다.
>>> # (데이터로 인식이 되니까 입력 내용 그대로 출력이 된 것이다.)
>>> 
>>> for i in [1, 2, 3]:
	pass 	# pass라고 입력하면 아무 일도 하지 않는 for 루프가 만들어집니다.

>>> 
>>> for i in [1, 2, 3]:
	pass

>>> [1, 2, 3]
[1, 2, 3]
>>> 
>>> # 사실 [1, 2, 3]과 같은 표현은 for 루프의 일부로만 사용하는 표현이 아니라, 그 자체로 파이썬이 인식하는 데이터의 한 종류이다.
>>> # 그리고 이러한 유형의 데이터를 가리켜 '리스트형 데이터' 또는 간단히 '리스트'라 한다.
>>> 
>>> #	"[1, 2, 3]은 파이썬이 인식하는 데이터의 한 종류이다."
>>> #	"[1, 2, 3]은 정수 1, 2, 3을 묶어 놓은 '리스트형(list type) 데이터'이다."
>>> 
>>> # 이러한 사실은 다음과 같이 type 함수 호출을 통해서도 확인할 수 있다. type 함수는 전달된 값의 데이터형을 알려주는 함수이니 말이다.
>>> 
>>> type([1, 2, 3])	# [1, 2, 3]의 데이터 종류는?
<class 'list'>
>>> 
>>> # 이러한 리스트는 여러 개의 값을 묶는데 사용된다. 그리고 다음에서 보이듯이 묶을 수 있는 값의 종류에 제한이 없다.
>>> # 서로 다른 종류의 값도 얼마든지 묶을 수 있다.
>>> 
>>> [1, "hello", 3.3]
[1, 'hello', 3.3]
>>> 
>>> # 물론 다음과 같이 리스트 안에 리스트를 넣을 수도 있다.
>>> [1, 2, [3, 4], ["AAA", "ZZZ"]]
[1, 2, [3, 4], ['AAA', 'ZZZ']]
>>> 
>>> # 그리고 또 중요한 사실 하나는 다음과 같이 리스트를 변수에 담는 것도 가능하다는 것이다.
>>> 
>>> st = [1, "hello", 3.3]	# 리스트를 변수 st에 담았음
>>> print(st)
[1, 'hello', 3.3]
>>> 
>>> # 잠시 정리를 하면, 리스트를 포함하여 우리가 지금까지 접한 데이터의 종류는 다음과 같이 세 가지이다.
>>> # (문자열도 데이터의 한 종류인데 이는 잠시 후에 포함시키겠다.)
>>> 
>>> #	* int형 데이터	ex)3, 5, 7, 9
>>> #	* float형 데이터	ex)2.2, 4.4, 6.6, 8.8
>>> #	* 리스트형 데이터 ex)[3, 5, 7, 9], ][
>>> 
>>> #	* int형 데이터		ex) 3, 5, 7, 9
>>> #	* float형 데이터		ex) 2.2, 4.4, 6.6, 8.8
>>> #	* 리스트형 데이터	ex) [3, 5, 7, 9], [2.2, 4.4, 6.6, 8.8]
>>> 
>>> # 이렇듯 데이터의 종류를 정리한 이유는, 파이썬이 데이터로 인식하는 것들의 종류를 아는 것이 중요하기 때문이다.
>>> # 따라서 앞으로도 새로운 유형의 데이터가 등장할 때마다 위와 같이 정리해 나가겠다.
>>> 
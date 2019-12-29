Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Chapter 02 간단한 함수 만들기
>>> # 02-1 함수 만들기 1: 인자 없는 것
>>> 
>>> print("반갑습니다.")
반갑습니다.
>>> print("파이썬의 세계로 오신 것을 환영합니다.")
파이썬의 세계로 오신 것을 환영합니다.
>>> # 위의 두 문장을 한 번 더 실행하고 싶다면? 두 문장을 다시 입력해야 한다.
>>> # 그러나 위의 두 문장을 '함수(function)'라는 것으로 묶으면, 한 번의 명령으로 위의 두 문장을 실행시킬 수 있다.
>>> # 횟수에 상관 없이 원하면 언제든 말이다. 그럼 위의 두 문장을 함수로 묶어 보겠다.
>>> 
>>> def greet();
SyntaxError: invalid syntax
>>> def greet():
	print("반갑습니다.")
	print("파이썬의 세계로 오신 것을 환영합니다.")

	
>>> # 위에서는 greet이라는 이름의 함수를 만들었다. 그리고 이 앟ㅁ수에는 두 개의 문장이 속해 있다.
>>> # 즉 위 함수의 내용을 정리하자면 다음과 같다.
>>> # def => 함수 만든다는 선언 greet => 함수의 이름 print() 2문장 => 함수에 속하는 문장들
>>> # 함수 만들기 끝낼 때 엔터키 한번 더 입력!!
>>> 
>>> # 이렇듯 함수를 만들어 놓으면, 다음과 같이 함수 이름의 입력을 통해
>>> # 그 안에 속한 문장들을 순서대로 실행시킬 수 있다. 몇 번이든 말이다.
>>> greet()
반갑습니다.
파이썬의 세계로 오신 것을 환영합니다.
>>> greet()
반갑습니다.
파이썬의 세계로 오신 것을 환영합니다.
>>> 
>>> # def greet(): 이는 파이썬 프롬포트에게 다음과 같이 말하는 것과 같다.
>>> # (함수를 만든다는 사실과 더불어 그 함수의 이름이 greet임을 알렸다.)
>>> # "지금부터 greet라는 이름의 함수를 만들 거다."
>>> # 이어서 엔터키를 누르면 다음과 같이 함수에 담을 내용을 입력할 수 있는 상태가 되는데,
>>> # 여기서 주목할 부분은 '커서(깜빡거리며 입력을 기다리는 것)'의 위치이다.
>>> # 줄을 바꿨는데도 >>> 이 뜨지 않았다. 그리고 커서의 위치가 왼쪽에서 몇 칸 떨어져 있는 상태인데,
>>> # 이 상태를 가리켜 '들여쓰기가 된 상태'라 한다. 이렇듯 들여쓰기가 된 상태에서 문장을 입력해야 함수 greet에 속하는 문장이 된다.
>>> # "파이썬은 들여쓰기 상태로 함수에 속하는 문장인지 아닌지를 판단한다."
>>> # 따라서 다음과 같이 입력하면 안 된다. 그러면 오류가 발생한다.
>>> def greet():
print("반갑습니다.")
SyntaxError: expected an indented block
>>> # 반드시 다음과 같이 들여쓰기가 된 상태로 입력이 이뤄져야 한다. 왼쪽에서부터 몇 칸을 띄우든 상관없지만
>>> # 동일한 간격으로 들여쓰기를 해야 하며 이왕이면 IDLE이 자동으로 해주는 들여쓰기 상태를 유지하는 것이 좋다.
>>> # 이렇게 해서 greet 함수에 담을 내용을 모두 입력했다면 마무리를 해야 한다. 마무리 방법은 위의 상태에서
>>> # (커서 위치가 어디인지 확인하자.) 엔터키를 한번 더 눌러주면 된다.
>>> def greet():
	print("반갑습니다.")
	print("파이썬의 세계로 오신 것을 환영합니다.")
	# 여기에서 엔터키를 한번 더 눌러 마무리한다.

	
>>> greet()
반갑습니다.
파이썬의 세계로 오신 것을 환영합니다.
>>> # 그래서 함수의 마지막 문장과, 이어서 등장하는 >>> 사이에는 한 줄의 공백이 있게 된다.
>>> # 이렇게 해서 함수를 하나 만들어 보았는데, 이를 가리켜 '함수의 정의(definition)'라 한다.
>>> # 즉 우리는 위에서 greet이라는 이름의 함수를 정의한 것이다.
>>> # 그리고 다음과 같이 함수의 실행을 명령하는 것을 '함수의 호출(call)'이라 한다.
>>> # 즉 다음 문장은 greet 함수를 호출하는 문장이다.
>>> greet
<function greet at 0x03C0F070>
>>> greet()
반갑습니다.
파이썬의 세계로 오신 것을 환영합니다.
>>> 
>>> # 물론 함수가 호출되면 그 함수에 속한 문장들이 차례로 실행이 되는데, 위의 예는 그러한 사실을 보여주고 있다.
>>> 
>>> # [연습문제 02-1]
>>> def MH():
	print("1 + 2 + 3 + 4 + 5 = ", 1 + 2 + 3 + 4 + 5)
	print("Simple is the best!")
	print("행복한 파이썬~")

	
>>> MH()
1 + 2 + 3 + 4 + 5 =  15
Simple is the best!
행복한 파이썬~
>>> MH()
1 + 2 + 3 + 4 + 5 =  15
Simple is the best!
행복한 파이썬~
>>> MH()
1 + 2 + 3 + 4 + 5 =  15
Simple is the best!
행복한 파이썬~
>>> 
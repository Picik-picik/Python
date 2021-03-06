Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Chapter 05. 리스트와 문자열
>>> # 05-1 print 함수의 복습과 확장
>>> 
>>> # 이번 장에서는 '문자열'과 '리스트'를 소개하는 것이 목적인데, 그에 앞서 print 함수의 사용 방법을 조금 더 설명하려 한다.
>>> # 앞서 우리는 다음의 수준으로 print 함수를 사용하였다.
>>> 
>>> for i in [1, 2, 3]:	# i에 1, 2, 3을 넣어가며 반복!
	print(i)

	
1
2
3
>>> 
>>> # 기본적으로 print 함수는 출력을 끝내면 줄을 바꿔버린다. 따라서 위와 같이 print 함수를 여러 번 이어서 호출하면
>>> # 여러 줄에 걸쳐서 내용이 출력된다. 그런데 줄을 바꾸지 않고 이어서 출력되도록 하는 방법이 있다. 다음과 같이 하면 된다.
>>> 
>>> for i in [1, 2, 3]:
	print(i, end = '_')

	
1_2_3_
>>> 
>>> # 위의 예제에서는 다음과 같이 print 함수를 호출하였다.
>>> 
>>> #	print(i, end = '_')
>>> 
>>> # 그리고 여기서 print 함수에 두 번째 값으로 넘긴 <end = '_'>이 의미하는 바는 다음과 같다.
>>> 
>>> #	"출력을 마치고 나면 줄 바꾸는 것 대신에 '_'을 출력해주세요."
>>> 
>>> # 따라서 다음 형태로 print 함수를 호출하면, 출력 내용 사이에 줄을 바꾸는 대신 빈칸이 들어가게 할 수도 있다.
>>> # (빈칸의 수는 하나 이상이 될 수 있다. 세 칸 넣으면 세 칸씩 떨어져서 출력된다.)
>>> 
>>> for i in [1, 2, 3]:
	print(i, end = ' ')	# 줄 바꿈 대신 빈 공간을 넣어라.

	
1 2 3 
>>> 
>>> # 일단은 이 정도만 이해하고 print 함수를 활용하자. 갑자기 <end = ' '> 가 어떻게 등장한 것인지
>>> # 궁금하겠지만, 이에 대해서는 10장에서 설명할 테니 지금은 이 정도만 이해하고 활용에 목적을 두자.
>>> 
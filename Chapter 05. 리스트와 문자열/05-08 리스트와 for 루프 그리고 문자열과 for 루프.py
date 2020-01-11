Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 05-8 리스트와 for 루프 그리고 문자열과 for 루프
>>> 
>>> # 리스트와 문자열은 비슷한 면이 많다.
>>> # 연산의 방법과 그 결과도 비슷하다.
>>> # 그래서 이 둘을 비교하며 공부하는 것은 의미가 있다.
>>> 
>>> for i in [1, 2, 3]:
	print(i, end = ' ')

	
1 2 3 
>>> 
>>> # 이렇듯 for 루프의 구성에 리스트를 사용하듯이, 문자열을 이용해서 for 루프를 구성하는 것도 가능하다.
>>> 
>>> for i in 'Happy':
	print(i, end = ' ')

	
H a p p y 
>>> 
>>> # 위의 경우 문자열 'Happy'의 문자가 변수 i에 하나씩 저장되면서 반복이 진행된다.
>>> # 따라서 필요하다면 문자열을 대상으로 얼마든지 for 루프를 구성할 수 있다.
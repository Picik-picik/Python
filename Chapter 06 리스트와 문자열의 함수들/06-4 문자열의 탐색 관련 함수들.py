Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 06-4 문자열의 탐색 관련 함수들
>>> 
>>> # 이어서 소개할 두 함수는 문자열 안에 특정 내용이 있는지, 있다면 어디에 있는지 확인할 때 사용하는 함수들이다.
>>> 
>>> #	s.find(sub)	문자열 s에 sub가 있으면 그 위치의 인덱스 값, 없으면 -1 반환
>>> #	s.rfind(sub)	s.find는 앞에서부터 sub를 찾는 반면 s.rfind는 뒤에서부터 찾는다.
>>> 
>>> # 먼저 다음 예를 통해서 find의 기능을 설명하겠다.
>>> 
>>> str = "What is important is that you should choose what is best for you"
>>> str.find("is")		# "is"가 있는 위치의 인덱스 값은?
5
>>> 
>>> # 출력된 숫자 5는 "is"가 등장한 위치를 알려주는 인덱스 값이다. 즉 5가 반환되었다는 것은 여섯 번째 문자에서부터 "is"가 등장함을 의미한다.
>>> # 위의 예에서 보인 find는 찾는 내용을 문자열의 앞에서부터(왼쪽에서부터 오른쪽으로) 찾아 나간다.
>>> # 위의 예에서 보인 find는 찾는 내용을 문자열의 앞에서부터(왼쪽에서 오른쪽으로) 찾아 나간다.
>>> # 반면 다음 예에서 보이는 rfind는 문자열의 뒤에서부터(오른쪽에서 왼쪽으로) 찾아 나간다.
>>> 
>>> str = "What is important is that you should choose what is best for you"
>>> str.rfind("is")		# 마지막 "is"가 있는 위치의 인덱스 값은?
49
>>> 
>>> # 위 예의 문자열에서는 "is"가 총 3번 등장하고 그 위치의 인덱스 값은 각각 5, 18, 49이다. 그런데 rfind는 뒤에서부터 "is"를 찾기 때문에 마지막 "is"가 시작하는 위치인
>>> # 49가 반환되고 출력되었다. 이렇듯 find와 rfind의 유일한 차이점은 탐색의 방향에 있다. 그리고 두 함수 모두 찾는 내용이 없을 경우 -1을 반환한다는 사실도 기억하기 바란다.
>>> 
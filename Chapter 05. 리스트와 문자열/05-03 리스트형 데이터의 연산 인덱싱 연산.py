Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 05-3 리스트형 데이터의 연산 : 인덱싱 연산
>>> 
>>> # 앞서 int형 그리고 float형 값을(데이터를) 가지고 다음 연산들을 진행해 보았다.
>>> 
>>> #	+	덧셈
>>> #	-	뺄셈
>>> #	*	곱셈
>>> #	**	거듭제곱
>>> #	/	실수형 나눗셈
>>> #	//	정수형 나눗셈
>>> #	%	나머지가 얼마?
>>> 
>>> # 그런데 리스트형 데이터를 대상으로도 다음 과 같이 덧셈 연산을 할 수 있다.
>>> 
>>> [1, 2, 3] + [4, 5]	# 두 리스트를 합한 결과를 반환
[1, 2, 3, 4, 5]
>>> 
>>> # 그리고 다음과 같이 곱셈 연산도 할 수 있다.
>>> 
>>> [1, 2, 3] * 2 		# 리스트의 내용을 두 배 늘린 결과를 반환
[1, 2, 3, 1, 2, 3]
>>> 
>>> # 덧셈의 결과는 두 리스트의 합이고, 곱셈의 결과는 리스트를 곱의 수만큼 늘린 것이다.
>>> # 그런데 리스트를 대상으로는 이들 곱셈과 덧셈보다 중요한 연산이 둘 있으니 이는 다음과 같다.
>>> 
>>> #	[ ]	인덱싱(indexing) 연산
>>> #	[ : ]	슬라이싱(slicing) 연산
>>> 
>>> # 먼저 인덱싱 연산이 무엇인지 보이겠다.
>>> 
>>> st = [1, 2, 3, 4, 5]
>>> n1 = st[0]	# 첫 번째 값을 꺼내서 n1에 저장
>>> n2 = st[4]	# 다섯 번째 값을 꺼내서 n2에 저장
>>> print(n1, n2)
1 5
>>> 
>>> # 위 예에서 변수 st에 리스트를 담았다. 그리고 이 변수를 대상으로 다음 연산을 진행하였다.
>>> 
>>> #	n1 = st[0]	# st[0]을 n1에 저장
>>> 
>>> # 이 연산이 갖는 의미는 다음과 같다. (결국 =의 오른쪽에 있는 값을 가져다 =의 왼쪽에 넣은 것이다.)
>>> 
>>> #	"변수 st에 담긴 리스트에서 첫 번째 값을 꺼내서 변수 n1에 저장해라."
>>> 
>>> # 마찬가지로 다음 연산이 의미하는 바는,
>>> 
>>> # 	n2 = st[4]	# st[4]를 n2에 저장
>>> 
>>> # 다음과 같다. 물론 이때 값을 꺼냈다고 해서 그 값이 리스트에서 사라지는 것은 아니다.
>>> 
>>> #	"변수 st에 담긴 리스트에서 다섯 번째 값을 꺼내서 변수 n2에 저장해라."
>>> 
>>> # 즉 '인덱싱 연산'이란 리스트에 담겨 있는 값들 중 하나를 참조하는 연산이다. 그리고 인덱싱 연산에서
>>> # 리스트의 첫 번째 값을 가리킬 때는 1이 아니라 0을 사용한다. 그리고 두 번째 값을 가리킬 때에는 2가 아니라 1을 사용한다.
>>> # 이렇듯 인덱싱 연산에서 0은 맨 앞을 의미한다.
>>> 
>>> # 지금까지는 인덱싱 연산을 이용한 '값을 꺼냄'의 예를 보였는데, 인덱싱 연산은 '값의 수정'에도 사용할 수 있다.
>>> # 이와 관련해서 다음 예를 보자.
>>> 
>>> st = [1, 2, 3, 4, 5]
>>> st[0] = 5 	# 5를 st[0]에 저장
>>> st[4] = 1 	# 1을 st[4]에 저장
>>> st
[5, 2, 3, 4, 1]
>>> 
>>> # 위 예의 다음 두 문장이 의미하는 바는,
>>> 
>>> #	st[0] = 5 	# 첫 번째 값을 5로 수정
>>> #	st[4] = 1 	# 다섯 번째 값을 1로 수정
>>> 
>>> # 각각 다음과 같다.
>>> 
>>> #	"st에 담긴 리스트의 첫 번째 값을 5로 수정해라."
>>> #	"st에 담긴 리스트의 다섯 번째 값을 1로 수정해라."
>>> 
>>> # 정리하면, 다음과 같이 st[0]가 =의 오른 편에 오면 '값의 꺼냄'을 의미하고,
>>> 
>>> #	num = st[0]	# st[0]의 값 꺼냄!
>>> 
>>> # 다음과 같이 =의 왼편에 오면 '값의 수정'을 의미한다.
>>> 
>>> #	st[0] = 5	# st[0]에 값 저장!
>>> 
>>> # 그러나 두 경우 모두 =의 오른쪽에 있는 값을 가져다 =의 왼쪽에 넣는 것이므로 = 연산의 관점에서 보면 이 둘은 차이가 없다.
>>> # 그리고 인덱싱 연산은 다음과 같이 진행할 수도 있다.
>>> 
>>> st = [1, 2, 3, 4, 5]
>>> print(st[0], st[2], st[4])	# st[0], st[2], st[4]의 값을 print 함수에 전달
1 3 5
>>> 
>>> # 위의 경우 print 함수 호출에 앞서 st[0], st[2], st[4]가 의미하는 값을 꺼내게 된다.
>>> # 즉 다음과 같이 값을 꺼낸 상태에서 print 함수가 호출된다.
>>> 
>>> #	print(st[0], st[2], st[4])   →   print(1, 3, 5)
>>> 
>>> # 그리고 [ ] 사이에 등장하는 값을 가리켜 '인덱스 값'이라 하는데, 이 용어는 자주 등장하므로 기억해 두기 바란다. 이왕디면 다음과 같이 기억해 두면 좋겠다.
>>> 
>>> #	"인덱스 값은 0부터 시작하는, 위치를 가리키는 값이다."
>>> 
>>> # 그럼 이어서 다음 예를 보자. 이 예에서는 인덱스 값으로 음수가 올 수 있음을 보이는데, 출력 결과를 보면서 이것이 의미하는 바가 무엇인지 짐작해보자.
>>> 
>>> st = [1, 2, 3, 4, 5]
>>> print(st[-1], st[-2], st[-3])	# 인덱스 값으로 음수가 사용되었다.
5 4 3
>>> 
>>> # 리스트에 저장된 첫 번째 값을 기준으로, 인덱스 값이 양수이면 오른쪽으로, 음수이면 그 반대로 접근을 하게 된다.
>>> # 따라서 리스트의 길이(저장된 값의 수)에 상관없이, 인덱스 값이 0이면 첫 번째 값에 접근하듯이, 인덱스 값이 -1이면 마지막 값에 접근하게 된다.
>>> 
>>> [연습 문제 05-1]
SyntaxError: invalid syntax
>>> # [연습 문제 05-1]
>>> 
>>> # 문제 1
>>> st = [1, 2, 3, 4]
>>> st[0]
1
>>> st[1]
2
>>> st[2]
3
>>> st[3]
4
>>> 
>>> # 문제 2
>>> st = [1, 2, 3, 4]
>>> st[0]
1
>>> st[-3]
2
>>> st[-2]
3
>>> st[-1]
4
>>> 
>>> st[-4]
1
>>> st[-3]
2
>>> st[-2]
3
>>> st[-1]
4
>>> 
>>> # 문제 3
>>> st = [1, 2, 3, 4]
>>> st[0] += 1
>>> st[1] += 2
>>> st = [1, 2, 3, 4]
>>> st[0] += 1
>>> st[1] += 1
>>> st[2] += 2
>>> st = [1, 2, 3, 4]
>>> st[0] += 1
>>> st[1] += 1
>>> st[2] += 1
>>> st[3] += 1
>>> st
[2, 3, 4, 5]
>>> 
>>> # 문제 4
>>> st = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in range[0, 9]:
	st[i] += 1

	
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    for i in range[0, 9]:
TypeError: 'type' object is not subscriptable
>>> for i in range(10):
	st(i) += 1
	
SyntaxError: cannot assign to function call
>>> st = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in range(10);
SyntaxError: invalid syntax
>>> for i in range(10):
	st[i] += 1

	
>>> st
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> 
>>> # 문제 5
>>> st = [1, 2, 3, 4, 5, 6]
>>> st[0], st[5] = st[5], st[0]
>>> st
[6, 2, 3, 4, 5, 1]
>>> 
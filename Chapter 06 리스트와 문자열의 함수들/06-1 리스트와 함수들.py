Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Chapter 06 리스트와 문자열의 함수들
>>> # 06-1 리스트와 함수들
>>> 
>>> # 지금까지 우리가 함수를 호출하는 방식은 다음과 같았다.
>>> 
>>> st = [1, 3, 5, 7, 9]
>>> num = len(st)	# len 함수는 리스트에 저장된 값의 개수를 반환
>>> num
5
>>> 
>>> # 이러한 유형의 함수 몇을 len 함수와 더불어 소개하면 다음과 같다.
>>> 
>>> #	len(s)	리스트 s의 길이(저장된 값의 수) 반환
>>> #	min(s)	리스트 s의 저장된 값 중에서 가장 작은 값 반환
>>> #	max(s)	리스트 s의 저장된 값 중에서 가장 큰 값 반환
>>> 
>>> st = [2, 5, 3, 7, 4]
>>> min(st)	# 가장 작은 값 반환
2
>>> max(st)	# 가장 큰 값 반환
7
>>> 
>>> st = [1, 2, 3]
>>> st.remove(2)		# 리스트에서 2를 찾아서 삭제
>>> st
[1, 3]
>>> 
>>> # 위의 예에서는 다음 방식으로 remove 함수를 호출해서, 리스트에 저장되어 있던 값 2를 삭제하였다.
>>> # 여기서 변수 이름 옆에 점을 찍고 remove 함수를 호출했다는 사실에 주목하자!
>>> 
>>> #	st.remove(2)
>>> 
>>> # 위의 remove 함수 호출은 그 모양새가 지금까지 봐왔던 함수 호출과 조금 다르다. 자! 그럼 이러한 유형의 함수 호출이 의미하는 바를 설명하겠다.
>>> 
>>> #	st = [1, 2, 3]
>>> 
>>> # 변수 st에 담긴 리스트는 다음과 같은 모양이라고 생각할 수 있다.
>>> 
>>> # 	1, 2, 3		[리스트 내부에 대한 생각]
>>> 
>>> # 그러나 사실 리스트는 다음과 같이 채워져 있다. 리스트 안에 '값'만 존재하는 게 아니라 '함수'도 존재한다.
>>> 
>>> #	1, 2, 3
>>> #	remove(x)	[실질적인 리스트의 내부]
>>> 
>>> # 위와 같이 데이터와(값과) 함수가 묶여서 존재하는 덩어리를 가리켜 '객체(object)'라 한다. 그러니까 리스트는 사실 '객체'이다.
>>> 
>>> #	"리스트는 함수와 데이터가 함께 존재하는 객체이다."
>>> 
>>> # 그리고 객체 안에 존재하는 함수를 호출하는 방법은 다음과 같다.
>>> 
>>> st = [1, 2, 3]
>>> st.remove(2)		# st에 저장된 객체의(리스트의) remove 함수 호출
>>> 
>>> # 위와 같이 호출하면, st에 저장된 객체의 remove 함수가 호출된다. 그리고 객체 안에 존재하는 함수는 같은 객체에 저장되어 있는 데이터를 대상으로 일을 한다.
>>> 
>>> #	"객체 안에 존재하는 함수는 같은 객체에 있는 데이터를 대상으로 일을 한다."
>>> 
>>> # 그러니까 위에서 st에 저장된 리스트를 대상으로 remove(2)를 호출했으니, st의 리스트에서 2를 지워서 다음의 상태가 되게 한다.
>>> 
>>> #	1, 3
>>> #	remove(x)	[삭제 후 리스트 내부]
>>> 
>>> # 그리고 위 그림에서는 리스트에 remove 함수만 있는 것처럼 표현했지만, 사실 다음과 같은 함수들이 함께 존재한다.
>>> # (이들 모두를 외울 필요는 없고 필요할 때 참고할 수 있는 정도로만 기억해 두면 된다.)
>>> 
>>> #	s.append(x)		리스트 s의 끝에 x를 추가
>>> #	s.extend(t)		리스트 s의 끝에 리스트 t의 내용 전부를 추가
>>> #	s.clear()			리스트 s의 내용물 전부 삭제
>>> #	s.insert(i, x)		s[i]에 x를 저장
>>> #	s.pop(i)			s[i]를 반환 및 삭제
>>> #	s.remove(x)		리스트 s에서 제일 앞에 등장하는 x를 하나만 삭제
>>> #	s.count(x)		리스트 s에 등장하는 x의 개수 반환
>>> #	s.index(x)		리스트 s에 처음 등장하는 x의 인덱스 값 반환
>>> 
>>> # 그럼 먼저 다음 예를 통해 append와 extend의 기능을 보이겠다.
>>> # (이후로 잠시 동안 '함수'라는 표현을 생략하겠다.)
>>> # 이 예에서 보이듯이 append는 하나의 값을 추가할 때 사용되고 extend는 다른 리스트의 내용 전체를 추가할 때 사용된다.
>>> 
>>> st = [1, 2, 3]
>>> st.append(4)		# st의 끝에 4 추가
>>> st.extend([5, 6])	# st의 끝에 [5, 6]의 내용 추가
>>> st
[1, 2, 3, 4, 5, 6]
>>> 
>>> # 다음은 원하는 위치에 값을 추가하는 insert와 리스트 내용 전부를 삭제하는 clear의 예이다.
>>> 
>>> st = [1, 2, 4]
>>> st.insert(2, 3)	# 인덱스 값 2의 위치에 3 저장
>>> st
[1, 2, 3, 4]
>>> st.clear()		# 리스트 내용 전부 삭제
>>> st
[]
>>> 
>>> # 위의 예에서는 insert를 통해 인덱스 2의 위치에 값을 저장하였다. 그러면 이 위치에 있던 값이 덮어써지는 것이 아니라, 이 위치부터 시작해서
>>> # 그 뒤에 저장된 모든 값들이 뒤로 한 칸씩 밀리게 된다. 이어서 다음은 빈 리스트를 만든 다음에 append를 통해 값을 추가하는 예이다.
>>> 
>>> st = []		# 빈 리스트 생성
>>> st.append(1)		# 리스트에 1 추가
>>> st.append(9)		# 리스트에 9 추가
>>> st
[1, 9]
>>> 
>>> # 다음은 값의 삭제에 사용되는 pop과 remove의 예이다. 이 둘의 차이점은 pop은 삭제할 때 위치를 지정하는 반면, remove는 삭제할 값을 명시한다는 점이다.
>>> 
>>> st = [1, 2, 3, 4, 5]
>>> st.pop(0)	# 인덱스 값 0의 위치에 저장된 데이터 삭제
1
>>> st
[2, 3, 4, 5]
>>> st.remove(5)		# 리스트에서 5를 삭제
>>> st
[2, 3, 4]
>>> 
>>> # 위의 예에서 pop이 호출되자 삭제한 내용이 출력되었다. 이는 pop이 삭제한 대상을 반환하기 때문에 나나탄 결과이다.
>>> # 반면 remove는 삭제한 대상을 반환하지 않기 때문에 별다른 출력으로 이어지지 않았다.
>>> 
>>> # 마지막으로 특정 데이터의 등장 횟수 또는 등장 위치를 반환하는 count와 index의 예를 보이겠다.
>>> 
>>> st = [1, 2, 3, 1, 2]
>>> st.count(1)		# 1이 몇 번 등장하는지 세어라.
2
>>> 
>>> st.index(2)		# 처음 2가 등장하는 위치의 인덱스 값은?
1
>>> 
>>> # [연습문제 06-1]
>>> 
>>> # 문제 1
>>> st = []		# 빈 리스트 생성
>>> st.append(1)		# 리스트에 1 추가
>>> st.append(2)		# 리스트에 2 추가
>>> st.append(3)		# 리스트에 3 추가
>>> st
[1, 2, 3]
>>> st.remove(1)		# 리스트에서 1 삭제
>>> st.remove(2)		# 리스트에서 2 삭제
>>> st.remove(3)		# 리스트에서 3 삭제
>>> st
[]
>>> 
>>> # 문제 2
>>> st = []
>>> st.append(1, 2, 3)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    st.append(1, 2, 3)
TypeError: append() takes exactly one argument (3 given)
>>> st.extend([1, 2, 3])
>>> ㄴㅅ
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    ㄴㅅ
NameError: name 'ᄂᄉ' is not defined
>>> st
[1, 2, 3]
>>> st.pop(-2)
2
>>> st.clear()
>>> st
[]
>>> st.extend([1, 2, 3])
>>> st.pop(-3)
1
>>> st.clear()
>>> st.extend([1, 2, ,3])
SyntaxError: invalid syntax
>>> st.extend([1, 2, 3])
>>> st.pop(-1)
3
>>> st.pop(-2)
1
>>> st.pop(0_
       
SyntaxError: invalid decimal literal
>>> st.pop(0)
2
>>> st.clear()
>>> st.extend([1, 2, 3])
>>> st.pop(-1)
3
>>> st.pop(1)
2
>>> st.pop(0)
1
>>> st
[]
>>> 
>>> # 문제 2
>>> st = []
>>> st.append(1)
>>> st.append(2)
>>> st.append(3)
>>> st
[1, 2, 3]
>>> st.pop(-1)
3
>>> st.pop(-1)
2
>>> st.pop(-1)
1
>>> st
[]
>>> 
>>> # 문제 3
>>> st = [1, 2, 3, 4]
>>> st[ : ] = []
>>> st
[]
>>> 
>>> # 문제 4
>>> st = []
>>> for i in range(10):
	st.append(i+1)

	
>>> st
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in range(10):
	st.pop(-1)

	
10
9
8
7
6
5
4
3
2
1
>>> st = []
>>> for i in range(10):
	st.append(i+1)
	
SyntaxError: multiple statements found while compiling a single statement
>>> st = []
>>> 
>>> # 문제 4
>>> st = []
>>> for i in range(10):
	st.append(i+1)

	
>>> st
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in range(10):
	st.pop(0, end = ', ')

	
Traceback (most recent call last):
  File "<pyshell#189>", line 2, in <module>
    st.pop(0, end = ', ')
TypeError: pop() takes no keyword arguments
>>> for i in range(10):
	st.pop(0)

	
1
2
3
4
5
6
7
8
9
10
>>> st
[]
>>> 
>>> # 문제 5
>>> st = []
>>> for i in range(10):
	st.append(i + 1)

	
>>> st
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in range(10):
	st.pop(-1)

	
10
9
8
7
6
5
4
3
2
1
>>> st
[]
>>> 
>>> # 문제 6
>>> st = [1, 2]
>>> st[2 : ] = [3, 4, 5]
>>> st
[1, 2, 3, 4, 5]
>>> 
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 04-3 int형으로 변환, float형으로 변환
>>> 
>>> # float형 값을 int형 값으로 바꿔주는 함수가 있고,
>>> # int형 값을 float형 값으로 바꿔주는 함수도 있다.
>>> # 그리고 이 함수들의 이름은 각각 int와 float이다.
>>> 
>>> num = 10
>>> num = float(num)	# num의 값을 float형으로
>>> type(num)
<class 'float'>
>>> 
>>> # 위의 예에서 num에 저장된 값을 10이었는데, float 함수의 호출을 통해서 float형 값인
>>> # 10.0으로 바뀌었다. 그런데 이 float 함수는 다음과 같이 문자열에 담긴 내용도  float형으로 바꿔준다.
>>> 
>>> num = float("3.14")
>>> type(num)	# 아래의 출력 결과는 num에 저장된 값이 float형임을 의미함
<class 'float'>
>>> 
>>> # 따라서 다음과 같이 eval 함수를 호출하는 예를,
>>> 
>>> height = eval(input("키 정보 입력 : "))	# eval 함수 호출
키 정보 입력 : 178.7
>>> print(height)
178.7
>>> 
>>> # 다음과 같이 float 함수를 호출하는 형태로 바꿀 수 있다.
>>> 
>>> height = float(input("키 정보 입력 : "))	# float 함수 호출
키 정보 입력 : 165.3
>>> print(height)
165.3
>>> 
>>> # 그럼 이번에는 int 함수 호출의 예를 보이겠다. 이 함수는 전달된 값을 int형으로 변환해서 변환한다.
>>> 
>>> num = int(3.14)	# 3.14를 int형으로 변환하라!
>>> print(num)
3
>>> 
>>> # int형 값에는 소수점 이하의 값이 존재할 수 없다. 그래서 위 예에서 3.14를 int형으로 바꾸는 과정에서
>>> # 소수점 이하의 값이 사라졌다. 그리고 int형 함수도 문자열에 담긴 내용을 int형으로 바꿔줄 수 있기 때문에 다음의 예를,
>>> 
>>> height = eval(input("키 정보 cm 담위로 입력 : "))		# eval 함수 호출
키 정보 cm 담위로 입력 : 178
>>> print(height)
178
>>> 
>>> # 다음과 같이 int 함수를 호출하는 형태로 바꿀 수 있다.
>>> 
>>> height = int(input("키 정보 cm 단위로 입력 : ")) 		# int 함수 호출
키 정보 cm 단위로 입력 : 178
>>> print(height)
178
>>> 
>>> # 이렇게 해서 eval 함수를 대신할 수 있는 int 함수와 float 함수를 소개하였다.
>>> # 물론 위의 eval 함수는 여전히 매력적이다. 다음과 같이 문장을 구성했을 때 정수가 입력되면
>>> # 그 값을 int형으로 반환하고, 실수가 입력되면 그 값을 float형으로 반환하기 때문이다.
>>> 
>>> #	height = eval(input("키 정보 입력 : "))
>>> 
>>> # 그러나 전에 언급했듯이 eval 함수는 그 능력만큼이나 위험도가 높은 함수이므로 제한적으로 사용하려고 노력해야 한다.
>>> 
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 06-3 문자열과 함수들
>>> 
>>> # 사실 문자열도 리스트와 마찬가지로 '객체(object)'이다. 따라서 문자열 안에도 다음 함수들이 존재한다.
>>> 
>>> #	s.count(sub)		문자열 s에 sub가 등장하는 횟수 반환
>>> #	s.lower()		문자열 s의 내용을 전부 소문자로 바꾼 문자열 반환
>>> #	s.upper()		문자열 s의 내용을 전부 대문자로 바꾼 문자열 반환
>>> #	s.lstrip()			문자열 s의 앞에 위치한 공백을 모두 제거한 문자열 반환
>>> #	s.rstrip()			문자열 s의 뒤에 위치한 공백을 모두 제거한 문자열 반환
>>> #	s.strip()			문자열 s의 앞과 뒤에 위치한 공백을 모두 제거한 문자열 반환
>>> #	s.replace(old, new)	문자열 s의 old를 new로 교체한 문자열 반환
>>> #	s.split()			문자열 s를 공백을 기준으로 나눠서 리스트에 담아서 반환
>>> 
>>> # 먼저 count는 다음과 같이 문자열에 등장하는 문자열의 수를 확인하는데 사용된다.
>>> 
>>> str = "YoonSungWoo"
>>> str.count("o")	# "o"가 몇 번 등장?
4
>>> str.count("oo")	# "oo"가 몇 번 등장?
2
>>> 
>>> # 그리고 lower와 upper는 다음과 같이 문자열의 내용을 소문자 또는 대문자로 바꿔서 반환한다.
>>> 
>>> org = "Yoon"
>>> lcp = org.lower()	# 모든 문자를 소문자로 바꿔서 반환
>>> ucp = org.upper()	# 모든 문자를 대문자로 바꿔서 반환
>>> org		# 원본은 그대로 존재한다.
'Yoon'
>>> lcp
'yoon'
>>> ucp
'YOON'
>>> 
>>> # 위의 예를 통해서 알 수 있듯이 lower와 upper는 문자열을 수정하는 함수가 아니고, 수정된 내용의 새로운 문자열을 생성해서 반환하는 함수이다.
>>> # (문자열은 수정 자체가 불가능하다는 사실을 잊지 말자.)
>>> 
>>> # 이어서 lstrip과 rstrip의 예를 보이겠다. 이 두 함수는 각각 문자열의 앞과 뒤에 위치한 공백이 제거된 문자열을 생성해서 반환한다.
>>> 
>>> org = "	MIDDLE       "
>>> cp1 = org.lstrip()		# 앞쪽에(왼쪽에) 있는 공백들 모두 제거
>>> cp2 = org.rstrip()		# 뒤쪽에(오른쪽에) 있는 공백들 모두 제거
>>> org
'\tMIDDLE       '
>>> cp1
'MIDDLE       '
>>> cp2
'\tMIDDLE'
>>> org = "         MIDDLE       "
>>> cp1 = org.lstrip()		# 앞쪽에(왼쪽에) 있는 공백들 모두 제거
>>> cp2 = org.rstrip()		# 뒤쪽에(오른쪽에) 있는 공백들 모두 제거
>>> org
'         MIDDLE       '
>>> cp1
'MIDDLE       '
>>> cp2
'         MIDDLE'
>>> 
>>> # 위의 예에서 보이듯이 문자열의 앞 또는 뒤에 위치한 공백은 그 수에 상관없이 모두 제거된다. 그리고 이어서 보이는 strip은 문자열의 앞과 뒤에 존재하는 공백을 모두 제거한다.
>>> 
>>> org = "         MIDDLE       "
>>> cpy = org.strip()		# 앞과 뒤에 있는 공백들 모두 제거
>>> org
'         MIDDLE       '
>>> cpy
'MIDDLE'
>>> 
>>> 
>>> # 공백을 제거하는 함수가 무슨 큰 도움이 될까 생각되겠지만 문자열 관련된 코드를 작성할 때 의외로 유용하게 사용되는 함수들이다.
>>> # 이런 함수들이 없었다면 이러한 기능의 함수를 직접 만들어서 사용해야할 판이다.
>>> 
>>> # 다음은 문자열의 내용 일부를 바꾸는 replace의 예를 보여준다. 앞서 소개한 함수들과 마찬가지로 문자열의 내용을 수정하는 것이 아니라 수정된 내용의 문자열을 새로 생성해서 반환을 한다.
>>> 
>>> org = "YoonSungWoo"
>>> rps = org.replace("oo", "ee")	# "oo"를 전부 "ee"로 교체
>>> rps
'YeenSungWee'
>>> 
>>> # 위의 예에서 보이듯이 "oo"가 "ee"로 전부 바뀌었다. 그렇다면 전부가 아니라 앞에 등장하는 하나만 바꾸려면 어떻게 해야 할까? 다음과 같이 숫자 1을 추가로 전달하면 된다.
>>> # (2를 전달하면 두 개가 바뀐다.)
>>> 
>>> org = "YoonSungWoo"
>>> rps = org.replace("oo", "ee", 1)	# 첫 번째로 등장하는 "oo" 하나를 "ee"로 교체
>>> rps
'YeenSungWoo'
>>> 
>>> # 마지막으로 split을 소개할 차례인데, 다음 예제를 보면서 이 함수의 기능을 파악해보자.
>>> org = "ab cd ef"
>>> ret = org.split 	# 공백을 기준으로 문자열을 쪼개서 리스트에 담아!
>>> ret
<built-in method split of str object at 0x035C5778>
>>> ret = org.split()	# 공백을 기준으로 문자열을 쪼개서 리스트에 담아!
>>> ret
['ab', 'cd', 'ef']
>>> 
>>> 
>>> # 위의 예에서 보이듯이, split은 공백을 기준으로 문자열을 나눠서 리스트에 담는다. 그리고 그 리스트를 반환한다. 그런데 이 함수는 다음과 같이 사용할 수도 있다.
>>> 
>>> org = "ab_cd_ef"
>>> ret = org.split('_')	# '_'를 기준으로 문자열을 쪼개서 리스트에 담아!
>>> ret
['ab', 'cd', 'ef']
>>> 
>>> # 위의 예에서는 split을 호출하면서 '_'를 전달하였다. 따라서 이번에는 문자열을 나누는 기준이 공백이 아니라 '_'가 되었다.
>>> 
>>> # [연습문제 06-2]
>>> 
>>> # 문제 1
>>> str = "The Espresso Spirit"
>>> icp = str.lower()
>>> ucp = str.upper()
>>> icp
'the espresso spirit'
>>> ucp
'THE ESPRESSO SPIRIT'
>>> str
'The Espresso Spirit'
>>> 
>>> # 문제 2
>>> def birth_only(pn):
	ret = pn.split('-')
	return ret[0]	# 첫 번째 저장된 것만 반환
p1 = "070609-2011xxx"
SyntaxError: invalid syntax
>>> def birth_only(pn):
	ret = pn.split('-')
	return ret[0]	# 첫 번째 저장된 것만 반환

>>> p1 = "070609-2011xxx"
>>> p1 = birth_only(p1)
>>> p1
'070609'
>>> p2 = "090716-1012xxx"
>>> p2 = birth_only(p2)
>>> p2
'090716'
>>> 
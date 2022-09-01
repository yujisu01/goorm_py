# 2. 문자열

# (1) 사칙연산
print("(1) 사칙연산")

str='hung'
str1='jik'
print(str+str1)

# (2) 문자열 함수
print("(2) 문자열 함수")

	# <1> join : 여러개의 문자열을 하나로 결합
str= '^'.join(['j','o','i','n']) # 각각 배열요소 사이에 문자열(^) 넣고 결합하게 됨
print(str) 					 # a^b^c

str=''.join(['j','o','i','n'])  # 그냥 합치고 싶을때
print(str)					# abc  

	# <2> partition : 인자값을 기준으로 첫번째 조건이 발견되면 분리하여 반환한다.
str= "partition_chosun_korea"
arr=str.partition('_');
print(arr) 					# ('partition','_','chosun_korea')

	# <3> split : 인자값을 기준으로 분리하여 리스트로 반환
str= "split_chosun_korea"
arr= str.split('_');
print(arr) 					# ('split','chosun','korea')

	# <4> foramt : %연산자의 포맷 스트링을 사용하는 방법 
print("format int:%d, Str:%s, float:%f" % (43,"jisu",170.5))
# Int: 43, Str: jisu, float:170.500000

	# <5> len : 문자열 길이값을 구해준다 (java의 length)
str = "len"
print(len(str)) 		# 3

	# <6> find : 문자열의 첫 시작위치를 구해준다
str= "findfindfind"
print(str.find('n'))	# 2 (인덱스는 항상 0부터 시작)

	# <7> upper : 모든 문자를 대문자로 변경한다
str = "upper"
print(str.upper())		# YUJISU

	# <8> lower : 모든 문자를 소문자로 변경한다
str = "LOWER"
print(str.lower())		# yujisu

	# <9> lstrip, rstrip, strip : 좌/우/양쪽 공백제거
str= " strip "
print(str.strip())   	# yujisu
str1= " rstrip "
print(str1.rstrip())
str2= " lstrip "
print(str2.lstrip())
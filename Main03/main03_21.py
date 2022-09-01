# 지금까지 파이썬에서 안나왔던 기출문제

sum=10				# (1) 전역변수 선언

def fun1():			
    sum=20
    print(sum)		# (2) fun1()의 sum값 (=20) 출력
def fun2():			
    global sum		# (5) global로 선언함으로써 전역변수를 선언, 
    sum=30			# (5-1) 전역변수(=10)값에 sum(=30)을 대입해줌
    
print(sum)			# (1-1) (1)의 전역변수 sum(=10) 출력
fun1()
print(sum)			# (3) fun1()의 지역변수 sum출력하고, 여기에서는 전역변수 sum(=10)출력
fun2()				# (4) fun2() 호출
print(sum)			# (5-2) 변경된 전역변수 sum값 (=30) 출력





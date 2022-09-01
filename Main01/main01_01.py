# 1. 파이썬 기초문법 예제

# (1) 사칙연산
print("(1) 사칙연산")
print(2+5) # 7
print(3/2) # 1
print(3/2.0) # 1.5
print(3*4) # 12

# (2) 변수사용
print("(2) 변수사용")
a=3
b=2.0	# float 으로 잡음 
# print문법같은 경우, (?,end='\n') 기본으로 역슬래쉬(엔터)기능이 있다.
print(a/b) # 1.5

# (3) 조건문
print("(3) 조건문")
a=10
if a>10:
    print("a가 10보다 크다")
elif a>5:
    print("a가 5보다 크다")
else:
    print("a가 5보다 작다")
    
# (4) for반복문
print("(4 )for반복문")
# 뒤에 있는 요소들을 하나하나 출력해서 앞의 변수(i)에다가 대입을 함
for i in[1,2,3]:
    print(i)
    
# 출력:
# 1
# 2
# 3

# (5) while반복문
print("(5) while반복문")

i=0 
sum=0 
while i<3:
    sum=sum+i;
    i=i+1 	# i++ 
print(sum)  # 3 출력

# (6) range
print("(6) range")

print(range(3)) # [0,1,2]
print(range(3,6)) # [3,4,5]
print(range(3,15,3)) # [3,6,9,12]

int_val=range(2,10,2)
for i in int_val:
    print(i) # 2 4 6 8
    
# (7) 함수
print("(7) 함수")

def sum(i,j): return i+j
print(sum(10,2))  			# 12

# j=10 은 인자가 하나 들어오면 j에는 기본적으로 10을 대입하겠다
def sum2(i,j=10): return i+j 
print(sum2(10,2))			# 12
print(sum2(10))				# 20 


class arr:
    a=["Yeoul","Uwangju","Jncheon","Iaejeon","Saegu","Uusan"]
str=''
for i in arr.a:
    str=str+i[0]
print(str)

# (1) arr이라는 클래스안에있는 a(리스트)라는 멤버변수에 있는 값을 
#		하나씩 뽑아서 i값에 넣겠다. 
# (2) str에 누적산 할거임. Seoul의 i[0]번지는 S, Gwangju의 i[0]번지는 G...
# (3) 각 문자열의 0번째 인덱스(첫번째글자) 를 str에 누적산 시켜서 출력시켜준다.
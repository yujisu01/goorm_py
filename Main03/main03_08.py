a=[0,10,20,30,40,50,60,70,80,90]
print(a[:7:2])
print(a[:7:3])
print(a[4:-1])


# (1) [:7:2]  시작주소 없고, 0~6번인덱스까지 출력, 2씩건너뛰어서 ㄱㄱ
# (2) [:7:3]  시작주소 없고, 0~6번인덱스까지 출력, 3씩건너뛰어서 ㄱㄱ
# (3) [4:-1]  a[4]부터 시작, 끝주소 -1임(80까지 출력)
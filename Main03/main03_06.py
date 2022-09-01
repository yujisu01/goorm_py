# 기출

data=[[1,2,3],[4,5],[6,7,8,9]]
print(data[0])
print(data[2][1])
for sub in data:
    for item in sub:
        print(item,end="")
    print()
    
# (1) data[0] 의 [1,2,3] 출력
# (2) data[2][1] 의 값 7 출력
# (3) data에 있는 각각의 요소들을 다 뽑아서 sub에 넣고-> 
# 		[1,2,3][4,5][6,7,8,9]
# 	sub에서 가져온 리스트를 item에 하나하나씩 다 대입하겠다 ->
# 		1,2,3
# 		4,5
# 		6,7,8,9
# cs()라는 함수를 만들고, return값 s
def cs(n):
    s=0
    for num in range(n+1):		# for문은 0~5까지 
        s+= num					# 0+1+2+3+4+5..(누적산)
    return s
print(cs(5))
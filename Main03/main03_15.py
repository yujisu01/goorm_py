class FourCal:
    def Setdata(sel,fir,sec):
        sel.fir=fir
        sel.sec=sec
    def add(sel):
        result=sel.fir+sel.sec
        return result
a=FourCal()
a.Setdata(4,2)
print(a.add())

# (1) FourCal라는 클래스 생성하고, def() 함수선언, Setdata() 메서드 선언
# (2) a라는 인스턴스에 FourCal()이라는 클래스를 생성시킴
# (3) a.Setdata(4,2)에 들어감-> 인자가 세개임 ->sel(=this) 인거 유추함
# (4) sel.fir에는 4 대입, sel.sec에는 2 대입 (인자로 받은거 대입)
# (5) (내가 가지고 있는)sel.fir+ (내가 가지고 있는)sel.sec = 4+2=6
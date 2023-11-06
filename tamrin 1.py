a = [i for i in range(1,50+1)]
b = [i for i in range(50,100+1)]
c = [i for i in range(100,150+1)]
d = [i for i in range(150,200+1)]
e = [i for i in range(200,250+1)]
f = [i for i in range(250,300+1)]
g = [i for i in range(300,350+1)]
h = [i for i in range(350,400+1)]
i = [i for i in range(400,450+1)]
j = [i for i in range(500,550+1)]

zz = a,b,c,d,e,f,g,h,i,j

for i in zz:
    for b in i:
        print(b)
#2. Generate fibnoacci series for 1 to 20
n1=0
n2=1
num=20
for i in range(n1,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)

a=int(input("Enter the range of fibonacci series: "))
fno=0
sno=1
for i in range (0,a+1):
    print(fno," ")
    print(sno," ")
    print(tno," ")
    tno=fno+sno
    sno=tno
    fno=sno
print("Result: ",tno)

fno = 1
sno = 1
num = int(input("Enter the range: "))
i = 1
print(fno, ' ')
print(sno, ' ')
while i <= num:
    tno = fno + sno
    print(tno, ' ')
    fno = sno
    sno = tno
    i = i + 1

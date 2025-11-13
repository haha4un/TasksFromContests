numrow = '12345678'
alphrow ='abcdefgh'

n = int(input())
for i in range(n):
    a, b = [x for x in input()]

    curinalp = alphrow.index(a)
    curinnum = numrow.index(b)

    c = 0
    if (0<= curinalp + 2 <= 7 and 0<= curinnum + 1 <= 7): c+=1
    if (0<= curinalp - 2 <= 7 and 0<= curinnum - 1 <= 7):c+=1
    if (0<= curinalp + 2 <= 7 and 0<= curinnum - 1 <= 7): c+=1
    if (0<= curinalp - 2 <= 7 and 0<= curinnum + 1 <= 7): c+=1
    if (0<= curinnum + 2 <= 7 and 0<= curinalp + 1 <= 7): c+=1
    if (0<= curinnum - 2 <= 7 and 0<= curinalp - 1 <= 7): c+=1
    if (0<= curinnum + 2 <= 7 and 0<= curinalp - 1 <= 7): c+=1
    if (0<= curinnum - 2 <= 7 and 0<= curinalp + 1 <= 7): c+=1
    print(c)

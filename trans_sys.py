x=int(input('Введите основание системы... ', ))
v=int(input('Число в десятичной системе = ', ))
temp = ""
while v>0:
    y=v%x
    if y==10:
        temp+='A'
    elif y==11:
        temp+='B'
    elif y==12:
        temp+="C"
    elif y==13:
        temp+="D"
    elif y==14:
        temp+="E"
    elif y==15:
        temp+="F"
    elif y==16:
        temp+="G"
    elif y==17:
        temp+="H"
    elif y==18:
        temp+="I"
    elif y==19:
        temp+="J"
    elif y==20:
        temp+="K"
    else:
        temp+=str(y)
    v=v//x
print(temp[::-1])


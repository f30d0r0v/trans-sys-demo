x=int(input('Введите основание системы... ', ))
v=int(input('Число в десятичной системе = ', ))
while v>0:
    y=v%x
    if y==10:
        print('A')
    elif y==11:
        print('B')
    elif y==12:
        print("C")
    elif y==13:
        print("D")
    elif y==14:
        print("E")
    elif y==15:
        print("F")
    elif y==16:
        print("G")
    elif y==17:
        print("H")
    elif y==18:
        print("I")
    elif y==19:
        print("J")
    elif y==20:
        print("K")
    else:
        print(y)
    v=v//x
print('Ответ читать с конца! Если основание системы больше, чем 21, то в тех местах, где будут дву- или более значные числа,пишите заглавные латинские буквы: А=10...К=20, L=21...')

# Функция сложения двух чисел
def pluss(a,b, f):
    if (a<0) and (b<0):
        s = pluss(abs(a), abs(b), 1)
    if (a<0):
        s = minuss(b, abs(a))
    elif (b<0):
        s = minuss(a, abs(b))
    else:
        # Целая часть
        a_list = str(a)
        if '.' in a_list:
            a_zel = a_list[:a_list.index('.')]
        else:
            a_zel = a_list
        b_list = str(b)
        if '.' in b_list:
            b_zel = b_list[:b_list.index('.')]
        else:
            b_zel = b_list
 
        # Переворот целой части
        a_zel = a_zel[::-1]
        b_zel = b_zel[::-1]
        b_zel = list(b_zel)
        a_zel = list(a_zel)
        if len(a_zel)>len(b_zel):
            while(len(a_zel)-len(b_zel)):
                b_zel.append(0)
        else:
            while(len(b_zel)-len(a_zel)):
                a_zel.append(0)
        n_zel = len(a_zel)
        for i in range(n_zel):
            a_zel[i] = int(a_zel[i])
            b_zel[i] = int(b_zel[i])

        # Сложение целой части
        s_zel=[0]*(n_zel+1)
        for i in range(n_zel):
            s_zel[i] = s_zel[i]+ a_zel[i]+b_zel[i]
            while s_zel[i]>4:
                s_zel[i+1] = 1
                s_zel[i] = s_zel[i]-5

        # Дробная часть
        # Если оба числа имеют дробную
        # Перевод чисел в строку, а затем в массив из чисел
        if ('.' in a_list) and ('.' in b_list):
            a_drob = a_list[a_list.index('.')+1:]
            b_drob = b_list[b_list.index('.')+1:]
            a_drob = list(a_drob)
            b_drob = list(b_drob)
            if len(a_drob) > len(b_drob):
                while(len(a_drob)-len(b_drob)):
                    b_drob.append(0)
            else:
                while(len(b_drob)-len(a_drob)):
                    a_drob.append(0)
            n_drob = len(a_drob)
            for i in range(n_drob):
                a_drob[i] = int(a_drob[i])
                b_drob[i] = int(b_drob[i])
            # Поворот массивов дробных частей для удобства
            a_drob = a_drob[::-1]
            b_drob = b_drob[::-1]

            # Если в дробной части есть целая часть
            s_drob = [0]*(n_drob+1)
            for i in range(n_drob):
                s_drob[i] = s_drob[i]+a_drob[i]+b_drob[i]
                while s_drob[i] > 4:
                    s_drob[i+1] = 1
                    s_drob[i] = s_drob[i]-5

            s_drob = s_drob[::-1]
            s_drob = ''.join(str(e) for e in s_drob)
            s_drob = int(s_drob)
            s_drob_zel = s_drob // (10**n_drob)
            s_drob = s_drob % (10**n_drob)
            s_zel[0] = s_zel[0]+s_drob_zel
            i = 0
            while s_zel[i]>4:
                s_zel[i+1]+=1
                s_zel[i]-=5
                i+=1
        # Если А дробное, В не дробное
        if ('.' in a_list) and ('.' not in b_list):
            a_drob = a_list[a_list.index('.')+1:]
            b_drob = '0'*len(a_drob)
            a_drob = list(a_drob)
            b_drob = list(b_drob)
            if len(a_drob)>len(b_drob):
                while(len(a_drob)-len(b_drob)):
                    b_drob.append(0)
            else:
                while(len(b_drob)-len(a_drob)):
                    a_drob.append(0)
            n_drob = len(a_drob)
            for i in range(n_drob):
                a_drob[i] = int(a_drob[i])
                b_drob[i] = int(b_drob[i])
            
            a_drob = a_drob[::-1]
            b_drob = b_drob[::-1]

            s_drob = [0]*(n_drob+1)
            for i in range(n_drob):
                s_drob[i] = s_drob[i]+a_drob[i]+b_drob[i]
                while s_drob[i]>4:
                    s_drob[i+1]=1
                    s_drob[i]=s_drob[i]-5

            s_drob = s_drob[::-1]
            s_drob = ''.join(str(e) for e in s_drob)
            s_drob = int(s_drob)
            s_drob_zel = s_drob // (10**n_drob)
            s_drob = s_drob % (10**n_drob)
            s_zel[0] = s_zel[0]+s_drob_zel
            i = 0
            while s_zel[i]>4:
                s_zel[i+1]+=1
                s_zel[i]-=5
                i+=1
        # Если А не дробное, В дробное
        if ('.' not in a_list) and ('.' in b_list):
            b_drob = b_list[b_list.index('.')+1:]
            a_drob = '0'*len(b_drob)
            a_drob = list(a_drob)
            b_drob = list(b_drob)
            if len(a_drob)>len(b_drob):
                while(len(a_drob)-len(b_drob)):
                    b_drob.append(0)
            else:
                while(len(b_drob)-len(a_drob)):
                    a_drob.append(0)
            n_drob = len(a_drob)
            for i in range(n_drob):
                a_drob[i] = int(a_drob[i])
                b_drob[i] = int(b_drob[i])
            
            a_drob = a_drob[::-1]
            b_drob = b_drob[::-1]

            s_drob = [0]*(n_drob+1)
            for i in range(n_drob):
                s_drob[i] = s_drob[i]+a_drob[i]+b_drob[i]
                while s_drob[i]>4:
                    s_drob[i+1]=1
                    s_drob[i]=s_drob[i]-5

            s_drob = s_drob[::-1]
            s_drob = ''.join(str(e) for e in s_drob)
            s_drob = int(s_drob)
            s_drob_zel = s_drob // (10**n_drob)
            s_drob = s_drob % (10**n_drob)
            s_zel[0] = s_zel[0]+s_drob_zel
            i = 0
            while s_zel[i]>4:
                s_zel[i+1]+=1
                s_zel[i]-=5
                i+=1
        # Поворот целой части
        # Перевод дробной части в число
        # Сложение дробной и целой части
        s_zel = s_zel[::-1]
        s_zel = ''.join(str(e) for e in s_zel)
        s = s_zel
        if ('.' in a_list) or ('.'in b_list):
            s_drob = str(s_drob)
            s = ''
            s = s_zel+'.'+s_drob
        # Проверка на запасную часть в числе
        # Запасная часть создана для того, чтобы если в сумме
        # целых чисел перейдет разряд
        if s[0]=='0':
            s = s[1:]
            if int(s_zel) == s:
                s = int(s)
            else:
                s = float(s)
            
    if (f == 1):
        return s*(-1)
    else:
        return s


# Функция подсчета разности двух чисел        
def minuss(a,b):
    flag = False
    if (a<0):
        s = pluss(b, abs(a), 1)
    elif (b<0):
        s = pluss(a, abs(b), 0)
    else:
        flag = False
        # Проверка на больше меньше, надо чтобы всегда А было больше В
        if (a<b):
            a,b=b,a
            flag = True
        
        # Разбиение на целую часть
        a_list = str(a)
        if '.' in a_list:
            a_zel = a_list[:a_list.index('.')]
        else:
            a_zel = a_list
        b_list = str(b)
        if '.' in b_list:
            b_zel = b_list[:b_list.index('.')]
        else:
            b_zel = b_list

        # Переворот целой части
        a_zel = a_zel[::-1]
        b_zel = b_zel[::-1]
        b_zel = list(b_zel)
        a_zel = list(a_zel)


        # Добавление дополнительных нулей для удобства подсчета
        if len(a_zel)>len(b_zel):
            while(len(a_zel)-len(b_zel)):
                b_zel.append(0)
        else:
            while(len(b_zel)-len(a_zel)):
                a_zel.append(0)
        n_zel = len(a_zel)

        # Преобразование в массив цифр
        for i in range(n_zel):
            a_zel[i] = int(a_zel[i])
            b_zel[i] = int(b_zel[i])
        
        # Сумма целой части
        s_zel=[0]*n_zel
        for i in range(n_zel):
            if a_zel[i]<b_zel[i]:
                a_zel[i+1]-=1
                a_zel[i]+=5
            s_zel[i]=a_zel[i]-b_zel[i]
        s_drob = 0
        s = 0
        # Дробная часть
        # Если оба числа дробные
        if ('.' in a_list) and ('.' in b_list):
            a_drob = a_list[a_list.index('.')+1:]
            b_drob = b_list[b_list.index('.')+1:]
            a_drob = list(a_drob)
            b_drob = list(b_drob)

            # Добавление дополнительных нулей для удобста
            if len(a_drob)>len(b_drob):
                while(len(a_drob)-len(b_drob)):
                    b_drob.append(0)
            else:
                while(len(b_drob)-len(a_drob)):
                    a_drob.append(0)
            n_drob = len(a_drob)

            # Перевод дробной части в массив цифр
            for i in range(n_drob):
                a_drob[i] = int(a_drob[i])
                b_drob[i] = int(b_drob[i])
            
            a_drob = a_drob[::-1]
            b_drob = b_drob[::-1]

            # Создание пустой дробной суммы
            s_drob = [0]*(n_drob+1)
            # Разность дробной части
            for i in range(n_drob):
                if a_drob[i]<b_drob[i] and (i <= (n_drob-2)):
                    a_drob[i+1] = a_drob[i+1]-1
                    a_drob[i] += 5
                elif a_drob[i]<b_drob[i] and (i ==(n_drob-1)):
                    a_drob[i] += 5
                    s_zel[0]-=1
                s_drob[i] = a_drob[i] - b_drob[i]

            # Перевод дробной части обратно в число    
            s_drob = s_drob[::-1]
            s_drob = ''.join(str(e) for e in s_drob)
            s_drob = int(s_drob)
            s_drob = s_drob / (10**n_drob)

            # Склеивание дробной и целлой части
            s_zel = s_zel[::-1]
            s_zel = ''.join(str(e) for e in s_zel)
            s_zel = int(s_zel)
            s = s_zel + s_drob


        # Если А дробное, а В не дробное
        if ('.' in a_list) and ('.' not in b_list):
            a_drob = a_list[a_list.index('.')+1:]
            b_drob = [0]*len(a_drob)
            a_drob = list(a_drob)
            b_drob = list(b_drob)

            # Перевод дробной части в массив цифр
            # с дополнительнымим нулями для удобства
            # в обратном порядке
            if len(a_drob)>len(b_drob):
                while(len(a_drob)-len(b_drob)):
                    b_drob.append(0)
            else:
                while(len(b_drob)-len(a_drob)):
                    a_drob.append(0)
            n_drob = len(a_drob)
            for i in range(n_drob):
                a_drob[i] = int(a_drob[i])
                b_drob[i] = int(b_drob[i])
            
            a_drob = a_drob[::-1]
            b_drob = b_drob[::-1]

            # Пустая разность дробной части
            s_drob = [0]*(n_drob+1)


            # Разность дробных частей
            for i in range(n_drob):
                if a_drob[i]<b_drob[i] and (i <= (n_drob-2)):
                    a_drob[i+1] = a_drob[i+1]-1
                    a_drob[i] += 5
                elif a_drob[i]<b_drob[i] and (i ==(n_drob-1)):
                    a_drob[i] += 5
                    s_zel[0]-=1
                s_drob[i] = a_drob[i] - b_drob[i]

            # Пееревод дробной разности в число    
            s_drob = s_drob[::-1]
            s_drob = ''.join(str(e) for e in s_drob)
            s_drob = int(s_drob)
            s_drob = s_drob / (10**n_drob)

            # Склеивание дробной и целой части
            s_zel = s_zel[::-1]
            s_zel = ''.join(str(e) for e in s_zel)
            s_zel = int(s_zel)
            s = s_zel + s_drob


        # Если B дробное, а A не дробное
        if ('.' not in a_list) and ('.' in b_list):
            b_drob = b_list[b_list.index('.')+1:]
            a_drob = [0]*len(b_drob)
            a_drob = list(a_drob)
            b_drob = list(b_drob)

            # Перевод дробной части в массив цифр
            # с дополнительнымим нулями для удобства
            # в обратном порядке
            if len(a_drob)>len(b_drob):
                while(len(a_drob)-len(b_drob)):
                    b_drob.append(0)
            else:
                while(len(b_drob)-len(a_drob)):
                    a_drob.append(0)
            n_drob = len(a_drob)
            for i in range(n_drob):
                a_drob[i] = int(a_drob[i])
                b_drob[i] = int(b_drob[i])
            
            a_drob = a_drob[::-1]
            b_drob = b_drob[::-1]

            # Пустая разность дробной части
            s_drob = [0]*(n_drob+1)


            # Разность дробных частей
            for i in range(n_drob):
                if a_drob[i]<b_drob[i] and (i <= (n_drob-2)):
                    a_drob[i+1] = a_drob[i+1]-1
                    a_drob[i] += 5
                elif a_drob[i]<b_drob[i] and (i ==(n_drob-1)):
                    a_drob[i] += 5
                    s_zel[0]-=1
                s_drob[i] = a_drob[i] - b_drob[i]

            # Пееревод дробной разности в число    
            s_drob = s_drob[::-1]
            s_drob = ''.join(str(e) for e in s_drob)
            s_drob = int(s_drob)
            s_drob = s_drob / (10**n_drob)

            # Склеивание дробной и целой части
            s_zel = s_zel[::-1]
            s_zel = ''.join(str(e) for e in s_zel)
            s_zel = int(s_zel)
            s = s_zel + s_drob

        if ('.' not in a_list) and ('.' not in b_list):
            s_zel = s_zel[::-1]
            s_zel = ''.join(str(e) for e in s_zel)
            s_zel = int(s_zel)
            s = s_zel + s_drob

    if flag:
        s *= -1
    return s

a = -111.111
b = -222.222
print('erfe', pluss(a,b,0))


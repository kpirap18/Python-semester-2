def bliz(a_a):
    global x,y
    for i in range(len(a_a)):
        if (i % 2 ==0):
            x.append(a_a[i])
        else:
            y.append(a_a[i])
    print(x, '\n',y)
    mins = ((x[0]-x[1])**2+(y[0]-y[1])**2)**(1/2)
    print('min',mins)
    mini = 0
    minj = 1
    n = round(len(a_a)/2)
    for i in range(n):
        for j in range(n):
            if i!=j:
                s = ((x[i]-x[j])**2+(y[i]-y[j])**2)**(1/2)
                print(s)
                if mins>s:
                    mins = s
                    mini = i
                    minj = j
    print(mins, mini, minj)
    return x[mini], y[mini], x[minj], y[minj]
    









s = [1, 2, 5, 4, 7, 8, 5, 8]
q,w,e,r = bliz(s)

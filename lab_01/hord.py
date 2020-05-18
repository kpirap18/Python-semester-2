from math import sin

def F(s):
    return sin(s)

def Method_hord2(a1,b1,max_iter,eps1):
    error =0
    iter_n = 0
    f = F(b1)
    x = a1
    rez = b1
    f = F(b1)
    f0 = F(a1)
    rez = rez-f/(f-f0)*(rez-x)
    #print(rez)
    while (abs(F(rez))>eps1):
        if f!=f0 and F(rez)*F(a1)<0:
            f = F(rez)
            f0 =F(a1)
            x = rez
            b1 = rez
            rez = rez -f/(f-f0)*(rez-a1)
            iter_n += 1
        
            print(a1,' ',rez,' ',iter_n)
        elif  f!=f0 and F(rez)*F(b1)<0:
            f = F(rez)
            f0 =F(b1)
            a1 = rez
            x = rez
            rez = rez -f/(f0-f)*(b1-rez)
            iter_n += 1
        
            #print(rez,' ',b1,' ',iter_n)
    if iter_n>max_iter:
        error =1
    #print('oooooo',time(),s)
    return rez,iter_n,error

s = Method_hord2(1,4,100,0.001)
print(s)

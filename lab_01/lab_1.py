'''           ***Козлова Ирина ИУ7-22б***
   Рассчет корней функии на данном интервале и с данном шагом.
   Интервал и Шаг вводится пользователем.'''

from tkinter import *
import matplotlib.pyplot as plt
from tkinter import messagebox
from math import sin,cos
import numpy as np
from hord import *

''' Производная функции sin(x)
    Нужна для нахождения экстремумов'''
def Fi(s):
    return cos(s)

'''Функция, которая считывает диапазон значений
       и переводит это в список вида [a,b],
       где а-начало интервала, b-конец интервала'''
def list_get(rang):
    try:
        list_a_b = [float(x) for x in rang.get().strip().split()]

        if len(list_a_b) == 0 or len(list_a_b) > 2:
            raise ValueError
        return list_a_b

    except ValueError:
        messagebox.showerror('Ошибка ввода данных',
                             'Проверьте введенные данные')


''' Функция рассчитывает корни для данного диапазона с данным шагом.
    Диапазон и шаг вводятся пользователлем.
    '''
def calc_roots(range_, shag_, eps_, iter_):
    try:
        # Проверка на неправильный ввод
        range_list = list_get(range_)
        a=range_list[0]
        b = range_list[1]
        if a >= b:
            messagebox.showerror('Ошибка ввода данных', 'Интервал должен \
быть возрастающим (start < end)')
            return False

        shag = float(shag_.get().strip())
        if shag < 0:
            messagebox.showerror('Ошибка ввода данных',
                                 'Шаг должен быть положительным')
            return False

        eps = float(eps_.get().strip())
        if not (0 < eps < shag / 2):
            messagebox.showerror('Ошибка ввода данных',
                                 'Точность должна \nлежать в интервале \
(0;step/2)')
            return False

        iterr = int(iter_.get().strip())
        if iterr < 0:
            messagebox.showerror('Ошибка ввода данных',
                                 'Количество итераций строго положительное')
            return False

        n = 1

        n_list = list()
        x_list = list()
        fx_list = list()
        left_l = list()
        right_l = list()
        iter_list = list()
        error_list = list()

        while a+shag*(n-1)<b:
            left = a+shag*(n-1)
            right = a+shag*(n) if a+shag*(n)<b else b
            if F(left)*F(right)<=0:
                x,it,err = Method_hord2(left,right,iterr,eps)
            else:
                n+=1
                continue
            if (err == 0 or err==1) and \
               (len(x_list) == 0 or abs(x - x_list[-1]) > 2 * eps):
                n_list.append(n)
                x_list.append(x)
                fx_list.append(F(x))
                left_l.append(left)
                right_l.append(right)
                iter_list.append(it)
                error_list.append(err)
            
                
            n+=1
        return n_list, x_list, fx_list, left_l, right_l, iter_list, error_list
    

    except ValueError:
        messagebox.showerror('Ошибка ввода данных',
                             'Проверьте введенные данные')

    except TypeError:
        pass
    
    
''' Функция вызываетсчя при нажатии на кнопку"найти корни."
    Делает новое окно, в котором воспроизводится
    "Таблица приближенных корней"'''    
def find_root(a,s,eps,f):
    all_roots = calc_roots(a,s,eps,f)
    if all_roots:
        if not len(all_roots[0]):
            messagebox.showinfo('Корни не найдены',
                                'Корни не найдены на заданном интервале')
        else:

            window = Toplevel(roots)
            window.grab_set()
            window.focus_set()
            window.geometry('600x500+700+100')
            window.title('Таблица')
            window['bg'] = '#c4adf0'
            w_window_l = Label(window,text = 'Таблица приближенных корней, \
найденных на интервале',
                               font = 'consolas 14',bg='#f0ade2',fg = 'black')
            w_window_l.place(x=300,y=25,anchor ='center')

            n_label = Label(window, text = ' № ',font = 'consolas 9',
                            fg = 'black')
            n_label.place(x=5,y=50)

            a_b_label = Label(window, text = '       [a,b]       ',
                              font = 'consolas 9',fg = 'black')
            a_b_label.place(x=35,y=50)

            x_label = Label(window, text = '     x      ',
                            font = 'consolas 9',fg = 'black')
            x_label.place(x=180,y=50)
            
            fx_label = Label(window, text = '      F(x)     ',
                             font = 'consolas 9',fg = 'black')
            fx_label.place(x=275,y=50)

            iter_label = Label(window, text = 'Кол-во итераций',
                               font = 'consolas 9',fg = 'black')
            iter_label.place(x=390,y=50)              

            err_label = Label(window, text = 'Код ошибки',
                              font = 'consolas 9',fg = 'black')
            err_label.place(x=505,y=50)

            n = len(all_roots[0])


            for i in range (n):
                if all_roots[6][i]==1:
                    print('SOS')
                    n_label = Label(window, text = '{:3d}'.format(i+1),
                                    font = 'consolas 9',fg = 'black')
                    n_label.place(x=5,y=50+30*(i+1))

                    a_b_label = Label(window, text = '[{:8.4f};{:8.4f}]'\
                                      .format(all_roots[3][i],all_roots[4][i]),
                                      font = 'consolas 9',fg = 'black')
                    a_b_label.place(x=35,y=50+30*(i+1))

                    x_label = Label(window, text = '              -          \
  ',
                                    fg = 'black')
                    x_label.place(x=180,y=50+30*(i+1))
                    
                    fx_label = Label(window, text = '                -        \
       ',
                                     fg = 'black')
                    fx_label.place(x=275,y=50+30*(i+1))

                    iter_label = Label(window, text = '{:15.0f}'.format\
                                       (all_roots[5][i]),
                                       font = 'consolas 9',fg = 'black')
                    iter_label.place(x=390,y=50+30*(i+1))              

                    err_label = Label(window, text = '{:10.0f}'.format\
                                      (all_roots[6][i]),
                                      font = 'consolas 9',fg = 'black')
                    err_label.place(x=505,y=50+30*(i+1))
                else:
                   
                    n_label = Label(window, text = '{:3d}'.format(i+1),
                                    font = 'consolas 9',fg = 'black')
                    n_label.place(x=5,y=50+30*(i+1))

                    a_b_label = Label(window, text = '[{:8.4f};{:8.4f}]'.format\
                                        (all_roots[3][i],all_roots[4][i]),
                                          font = 'consolas 9',fg = 'black')
                    a_b_label.place(x=35,y=50+30*(i+1))

                    x_label = Label(window, text = '{:12.5f}'.format\
                                        (all_roots[1][i]),
                                        font = 'consolas 9',fg = 'black')
                    x_label.place(x=180,y=50+30*(i+1))
                        
                    fx_label = Label(window, text = '{:15.0e}'.format\
                                         (all_roots[2][i]),
                                         font = 'consolas 9',fg = 'black')
                    fx_label.place(x=275,y=50+30*(i+1))

                    iter_label = Label(window, text = '{:15.0f}'.format\
                                           (all_roots[5][i]),
                                           font = 'consolas 9',fg = 'black')
                    iter_label.place(x=390,y=50+30*(i+1))              

                    err_label = Label(window, text = '{:10.0f}'.format\
                                          (all_roots[6][i]),
                                          font = 'consolas 9',fg = 'black')
                    err_label.place(x=505,y=50+30*(i+1))



            error_code_j = Button(window, text='Код ошибки',
                                  width = 15,height = 1,
                                  bg = 'white',fg = 'black',
                                  command=lambda:messagebox.showinfo\
                                  ('Код ошибки','0 - нет ошибки\n\
1 - кол-во итераций больше максимального'))
            error_code_j.place(x=10,y = 50+45*n)
    
''' Функция, рисующая график.
    вызывается при нажании на кнопку "Построить график".
    Строит график с помощью библиотеки Matplotlib.pyplot'''
def draw(a,s,eps,f):
    all_roots = calc_roots(a,s,eps,f)
    d = list_get(a)
    print(d[0],d[1])
    x = np.linspace(d[0],d[1],500000)
    y = np.sin(x)
    plt.cla()
    plt.title('$sin(x)$')
    plt.grid(True)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    
    plt.plot(x,y,'b')
    
    extr_list_x = list()
    extr_list_y = list()
    for i in range(1,499999):
        if abs(Fi(x[i]))<= 0.0001 and Fi(x[i-1])*Fi(x[i+1]):
            extr_list_x.append(x[i])
            extr_list_y.append(F(x[i]))


    plt.scatter(extr_list_x,extr_list_y,color = 'red',label='Extremums')
    plt.scatter(all_roots[1],all_roots[2],color = 'green',label='Roots')


    plt.legend(loc = 'lower left')
    plt.show()
    
    



''' Первое окно программы '''
roots = Tk()
roots['bg'] = '#adf0cd'
roots.geometry('500x280+500+200')
roots.title('Chord method')

''' Окна для ввода данных.
    В данные окна уже записаны константы.
    Пользовватель может их менять'''
start_label = Label(roots, text = 'Нахождниe корней функции (sin(x)) \
с помощью метода хорд',font = 'consolas 13',fg = 'black')
start_label.grid(row = 1,column =0,columnspan = 3)

start_label1 = Label(roots, text = '',font = 'consolas',
                     bg = '#adf0cd',fg = 'black')
start_label1.grid(row = 2,column =0,columnspan = 3)

range_label = Label(roots, text = 'Правая и левая граница\n \
(через пробел)',font = 'consolas 10',
                    bg = '#adf0cd',fg = 'black')
range_label.grid(row = 3,column = 0)

range_entry_start = '0 10'
range_entry = Entry(roots, width=20)
range_entry.insert(0, range_entry_start)
range_entry.grid(row=3, column=1, rowspan=2)



shag_label = Label(roots, text = 'Шаг',
                    font = 'consolas 10',bg = '#adf0cd',fg = 'black')
shag_label.grid(row = 7,column = 0,rowspan = 2)


shag_entry_start = '1'
shag_entry = Entry(roots, width=20)
shag_entry.insert(0, shag_entry_start)
shag_entry.grid(row=7, column=1, rowspan=2)


eps_label = Label(roots, text = 'Точность измерений',
                    font = 'consolas 10',bg = '#adf0cd',fg = 'black')
eps_label.grid(row = 10,column = 0,rowspan = 2)


eps_entry_start = '0.001'
eps_entry = Entry(roots, width=20)
eps_entry.insert(0, eps_entry_start)
eps_entry.grid(row=10, column=1, rowspan=2)




iter_label = Label(roots, text = 'Максимальное количество итераций',
                    font = 'consolas 10',bg = '#adf0cd',fg = 'black')
iter_label.grid(row = 13,column = 0,rowspan = 2)



iter_entry_start = '100'
iter_entry = Entry(roots, width=20)
iter_entry.insert(0, iter_entry_start)
iter_entry.grid(row=13, column=1, rowspan=2)


#Кнопки(Найти корни, построить график, выход)
find_roote = Button(roots, text='Найти корни',width = 15,height = 1,
                   bg = 'white',fg = 'black',
                   command=lambda: find_root(range_entry,shag_entry,
                                             eps_entry,iter_entry))
find_roote.place(anchor = 'center',x=100, y=200)

draw_graf = Button(roots, text='Построить график',width = 15,height = 1,
                   bg = 'white',fg = 'black',
                   command = lambda: draw(range_entry,shag_entry,
                                          eps_entry,iter_entry))
draw_graf.place(anchor = 'center',x=250, y=200)

exit_but =  Button(roots, text='Выход',width = 15,height = 1,
                   bg = 'white',fg = 'black',
                   command = lambda: roots.destroy())
exit_but.place(anchor = 'center',x=400, y=200)
roots.mainloop()

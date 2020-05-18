''' Данная программа создана для сравнения Пирамидальной сортировки
    на разных размров массива.
                                              Козлова Ирина ИУ7-22Б
'''
from tkinter import *
from tkinter import messagebox
from random import randint
from time import time
from hearsort import *
import numpy as np
import matplotlib.pyplot as plt


''' Функция преобразовывает введенные числа в массив чисел.
    Данная функция используется для пошагового вывода результата.
    Если вводится больше 10, то выдается ошбка.

    rang - введенные числа
    list_a_b - массив чисел, который подается на выход
'''
def list_get(rang):
    try:
        list_a_b = [int(x) for x in rang.get().strip().split()]
        
            
        
        if len(list_a_b) == 0 or len(list_a_b) > 10:
            raise ValueError
              
        return list_a_b
    except ValueError:
        messagebox.showerror('Ошибка ввода данных',
                             'Проверьте введенные данные.'
                             'Некоректные данные или'
                             'введено больше 10 чисел')
    except IndexError:
        messagebox.showerror('Ошибка ввода данных',
                             'Проверьте введенные данные.'
                             'Некоректные данные или'
                             'введено больше 10 чисел')
    except TypeError:
        pass

''' Функция для записи в таблицу

    to_w - куда требуется записать
    out_w - что требуется записать
'''    
def wr_label(to_w, out_w):
    out_w['text'] = ''
    out_w['text'] += to_w

''' Функция для очистки полей ввода

    ent - поля ввода, которые надо очистить
'''
def clean_entry(*ent):
    for i in ent:
        i.config(state = 'normal')
        i.delete(0,END)

''' Функция для очистки полей вывода

    ent - поля вывода, которые надо очистить
'''
def clean_entry_out(ent):
    for i in ent:
        i.config(state = 'normal')
        i.delete(0,END)
        i.config(state='readonly')

''' Функция для очистки Label

    lab - что нужно стереть из окна программы
'''
def clean_lab(*lab):
    for i in lab:
        i['text'] = ''
        
''' Функция для иллюстрации сортировки по шагам
    Данная функция показывает как работает Пирамидальная сортировка
    по шагам, то есть выводит каждый шаг работы данной сортировки.
'''        
def sort_step():
    
    ''' При нажатии на Enter '''
    def enter_sort_step(event):
        wr_label(heapSort_sbs(list_get(wel_entry)),res_label)

    def clean_lab_enter(event):
        clean_lab(res_label)

    sort_window = Toplevel(roots)
    sort_window.grab_set()
    sort_window.geometry('500x800+40+0')
    sort_window.title('По шагам пирамидальная сортировка')
    sort_window.config(bg="#fcb4d5")

    wel_label = Label(sort_window, text = 'Введите массив (до 10 элементов)\n'
                      'через пробел',
                      font = 'consolas 12',
                      bg = '#fcb4d5', fg = 'black')
    wel_label.pack()

    wel_entry = Entry(sort_window, width = 50)
    wel_entry.pack()
    wel_entry.focus_set()

    sort_button = Button(sort_window,
                         text = 'Sort',
                         font = 'consolas 12',
                         bg = 'white',
                         fg = 'black',
                         command=lambda:wr_label(heapSort_sbs(
                             list_get(wel_entry)),res_label))
    sort_button.pack()
    
    res_label = Label(sort_window,
                      text = '',
                      width = 80,
                      height = 40,
                      bg = '#fcb4d5', fg = 'black',
                      font = 'consolas 10')
    res_label.pack()

    exit_but =  Button(sort_window, text='Exit',width = 20,height = 2,
                   font='consolas 10',
                   bg = 'white',fg = 'black',
                   command = lambda: sort_window.destroy())
    exit_but.pack()

    wel_entry.bind('<Return>', enter_sort_step)
    wel_entry.bind('<Key>', clean_lab_enter)

''' Функция вывода информации о программе.
    Данная функция выводит окно, в котором выводится информация
    для чего предназначена данная программа, кто автор, когда написана
'''
def proprog():
    window = Toplevel(roots)
    window.geometry('300x200+600+300')
    window.config(bg = '#8dfcf7')
    window.title('About program')
    window_l = Label(window, text ='Данная программа предназначена\n'
                     'для сравнения Пирамидальной сортировки\n'
                     'на различных массивах\n\n'
                     'Автор: Козлова Ирина ИУ7-22Б\n'
                     '                   март 2020',
                     font = 'consolas 10',
                     bg = '#8dfcf7', fg = 'black')

    window_l.pack()
    exit_but =  Button(window, text='Выход',width = 15,height = 1,
                   bg = 'white',fg = 'black',
                   command = lambda: window.destroy())
    exit_but.place(anchor = 'center',x=150, y=150)

''' Функция подсчета времени, затраченного на сортировку
    Данная функция замеряет время, затарченное а сортировку
    массива различной длины.

    ko - размер массива
'''
def sort_time(ko):
    try:
        
        if ko<1:
            messagebox.showerror(
                "Ошибка ввода данных",
                "Данные введены "
                "некорректно, проверьте "
                "правильность ввода!")
        else:
            arr_random = list()
            arr_time = list()
        
            for i in range(ko):
                arr_random.append(randint(-10000,10000))
                
            upr_arr = arr_random[:]
            heapSort(upr_arr)
            time_s = time()
            heapSort(upr_arr)
            time_end = time()

            res_time = '{0:.6f}'.format(time_end - time_s) + ' c'
            arr_time.append(res_time)
            
            sl_arr = arr_random[:]
            time_s = time()
            heapSort(sl_arr)
            time_end = time()
            
            res_time = '{0:.6f}'.format(time_end - time_s) + ' c'
            arr_time.append(res_time)

            obr_arr = arr_random[:]
            heapSort(obr_arr)
            obr_arr.reverse()
            time_s = time()
            heapSort(obr_arr)
            time_end = time()
              
            res_time = '{0:.6f}'.format(time_end - time_s) + ' c'
            arr_time.append(res_time)

            return arr_time

    except TypeError:
        pass
    except IndexError:
        pass
    except ValueError:
        for i in n1_outtt:
            i.config(state='readonly')
        messagebox.showerror('Ошибка ввода данных','Данные введены неверно'
                                                   'Проверьте ввод данных')
        
        
''' Функция записи результатов на экран
    Данная функция записывает результаты в нужные окна

    n1_ent -
    n1_outtt -
'''    
def sort_com(n1_ent, n1_outtt):
    try:
        kol = int(n1_ent.get())
        if kol<1:
            raise ValueError
        else:
            for i in n1_outtt:
                i.config(state = 'normal')
                i.delete(0,END)
                i.config(state = 'readonly')
                
            sort_arr_time = sort_time(kol)

            p = 0
            for i in n1_outtt:
                i.config(state = 'normal')
                i.insert(0,sort_arr_time[p])
                i.config(state = 'readonly')
                p+=1
   

    except IndexError:
        pass
    except ValueError:
        messagebox.showerror('Ошибка ввода данных','Данные введены неверно'
                                                   'Проверьте ввод данных')

''' Функция рисования графика зависимости времени от размера'''
def graf():
    window = Toplevel(roots)
    window.geometry('300x200+600+300')
    window.config(bg = '#8dfcf7')
    window.title('About Grafic')
    window_l = Label(window, text ='Данный график зависимости времени\n'
                     'Пирамидальной сортировки \n'
                     'от размерности массива\n'
                     '\n'
                     'Значения размеров равномерно разделены\n'
                     'на промежутке от 500 до 5000\n',
                     font = 'consolas 10',
                     bg = '#8dfcf7', fg = 'black')

    window_l.pack()
    exit_but =  Button(window, text='Выход',width = 15,height = 1,
                   bg = 'white',fg = 'black',
                   command = lambda: window.destroy())
    exit_but.place(anchor = 'center',x=150, y=150)
    
    graf_x = np.linspace(100,1000,10)
    graf_y = []
    for i in range(10):
        arr_rant = []
        for j in range(int(graf_x[i])):
            arr_rant.append(randint(-10000,10000))
        
        time_s = time()
        heapSort(arr_rant)
        time_stop = time()
        graf_y.append(time_stop-time_s)

    plt.cla()
    plt.title('График зависимости времени от размера массива')
    plt.grid(True)
    plt.xlabel('$N(колличество)$')
    plt.ylabel('$Time$')
    plt.plot(graf_x,graf_y,'b')
    plt.show()

''' Главное окно программы '''
roots = Tk()
roots['bg'] = '#e0b0ff'
roots.geometry('600x400+500+200')
roots.title('HeapSort')

''' Создание меню '''
mainmenu = Menu(roots)
roots.config(menu=mainmenu)

cleanmenu = Menu(mainmenu, tearoff=0)
cleanmenu.add_command(label = 'Clear field N1',
                      command = lambda: clean_entry(n1_entry))
cleanmenu.add_command(label = 'Clear field result N1',
                      command = lambda: clean_entry_out(n1_out))
cleanmenu.add_command(label = 'Clear field N2',
                      command = lambda: clean_entry(n2_entry))
cleanmenu.add_command(label = 'Clear field result N2',
                      command = lambda: clean_entry_out(n2_out))
cleanmenu.add_command(label = 'Clear field N3',
                      command = lambda: clean_entry(n3_entry))
cleanmenu.add_command(label = 'Clear field result N3',
                      command = lambda: clean_entry_out(n3_out))
cleanmenu.add_command(label = 'Clear all fields',
                      command = lambda: (clean_entry(n1_entry, n2_entry, n3_entry),
                                         clean_entry_out(n1_out),
                                         clean_entry_out(n2_out),
                                         clean_entry_out(n3_out)))

filemenu1 = Menu(mainmenu, tearoff=0)
filemenu1.add_command(label = 'Step by step',
                      command = lambda: sort_step())


aboutmenu = Menu(mainmenu, tearoff=0)
aboutmenu.add_command(label ='About the program',
                      command = lambda: proprog())

mainmenu.add_cascade(label = 'Clean', menu = cleanmenu)
mainmenu.add_cascade(label = 'Operations', menu = filemenu1)
mainmenu.add_cascade(label = 'Help', menu = aboutmenu)

''' Заполнение окна программы Label, Entry и кнопками '''
wel_label = Label(roots, text = '   Сравнение "Пирамидальной сортировки"'
                  'на различных массивах   ', font = 'consolas 11',
                  bg = '#e0fdff', fg = 'black')
wel_label.place(x = 50, y = 0)

n1_label = Label(roots, text = 'N1',
                 font = 'consolas 10',
                  bg = '#e0b0ff', fg = 'black')
n1_label.place(x = 200,y = 30)

n1_entry = Entry(roots, width = 18)
n1_entry.place(x = 150, y = 60)
n1_entry.focus_set()

n2_label = Label(roots, text = 'N2',
                 font = 'consolas 10',
                  bg = '#e0b0ff', fg = 'black')
n2_label.place(x = 348,y = 30)

n2_entry = Entry(roots, width = 18)
n2_entry.place(x = 300, y = 60)

n3_label = Label(roots, text = 'N3',
                 font = 'consolas 10',
                  bg = '#e0b0ff', fg = 'black')
n3_label.place(x = 500,y = 30)

n3_entry = Entry(roots, width = 18)
n3_entry.place(x = 450, y = 60)

upr_label = Label(roots, text = 'Упорядоченный по\n возрастанию массив',
                 font = 'consolas 10',
                  bg = '#e0b0ff', fg = 'black')
upr_label.place(x = 0,y = 142)

upr_label = Label(roots, text = 'Массив заполненный\n случайными числами',
                 font = 'consolas 10',
                  bg = '#e0b0ff', fg = 'black')
upr_label.place(x = 0,y = 193)

upr_label = Label(roots, text = 'Упорядоченный по\n убыванию массив',
                 font = 'consolas 10',
                  bg = '#e0b0ff', fg = 'black')
upr_label.place(x = 5,y = 240)

n1_sort_upr = Entry(roots, width = 18)
n1_sort_upr.place(x = 150, y = 150)
n1_sort_sl = Entry(roots, width = 18)
n1_sort_sl.place(x = 150, y = 200)
n1_sort_obr = Entry(roots, width = 18)
n1_sort_obr.place(x = 150, y = 250)

n2_sort_upr = Entry(roots, width = 18)
n2_sort_upr.place(x = 300, y = 150)
n2_sort_sl = Entry(roots, width = 18)
n2_sort_sl.place(x = 300, y = 200)
n2_sort_obr = Entry(roots, width = 18)
n2_sort_obr.place(x = 300, y = 250)

n3_sort_upr = Entry(roots, width = 18)
n3_sort_upr.place(x = 450, y = 150)
n3_sort_sl = Entry(roots, width = 18)
n3_sort_sl.place(x = 450, y = 200)
n3_sort_obr = Entry(roots, width = 18)
n3_sort_obr.place(x = 450, y = 250)

n1_out = [n1_sort_upr, n1_sort_sl, n1_sort_obr]
n2_out = [n2_sort_upr, n2_sort_sl, n2_sort_obr]
n3_out = [n3_sort_upr, n3_sort_sl, n3_sort_obr]

for i in n1_out:
    i.config(state = 'readonly')
    
for i in n2_out:
    i.config(state = 'readonly')

for i in n3_out:
    i.config(state = 'readonly')
    
sort_all_button = Button(roots, text = 'Sort',
                         width = 20, height = 2,
                         font = 'consolas 10',
                         bg = 'white', fg = 'black',
                         command = lambda:(sort_com(n1_entry, n1_out),
                                           sort_com(n2_entry, n2_out),
                                           sort_com(n3_entry, n3_out)))
sort_all_button.place(x = 225, y = 90)

exit_but =  Button(roots, text='Exit',width = 20,height = 2,
                   font='consolas 10',
                   bg = 'white',fg = 'black',
                   command = lambda: roots.destroy())
exit_but.place(x=100, y=300)
graf_but =  Button(roots, text='Grafic',width = 20,height = 2,
                   font='consolas 10',
                   bg = 'white',fg = 'black',
                   command = lambda: graf())
graf_but.place(x=300, y=300)

roots.mainloop()

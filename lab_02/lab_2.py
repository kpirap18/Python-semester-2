'''           ***Козлова Ирина ИУ7-22б***
   Вычисление суммы или разности двух чисел в пятеричной системе счисления.
   Числа можно вводить как в интерфейсе, так и с клавиатуры.
   Числа могут быть как дробные, так и целые.
'''

from tkinter import *
from tkinter import messagebox
from c5c import *


''' Функция преобразовывает введенные числа в массив чисел.
    Если введены цифры, которые не входят в алфавит данной системы счисления,
    то выводится ошибка.

    rang - введенные числа
    list_a_b - массив чисел, который подается на выход
    list_chek - массив для проверки на правильность ввода
    в соответсвии алфавита СС
'''
def list_get(rang):
    try:
        list_a_b = [float(x) for x in rang.get().strip().split()]
        if (abs(int(list_a_b[0])) == list_a_b[0]) and\
           (abs(int(list_a_b[1])) == list_a_b[1]):
            list_a_b[0] = int(list_a_b[0])
            list_a_b[1] = int(list_a_b[1])
        list_chek = str(list_a_b[0])+str(list_a_b[1])
        list_chek = list(list_chek)
        for i in range(len(list_chek)):
            if (list_chek[i] !='.') and (list_chek[i] !='-'):
                if int(list_chek[i]) >= 5:
                    raise ValueError
        
        if len(list_a_b) == 0 or len(list_a_b) > 2:
            raise ValueError
              
        return list_a_b
    except ValueError:
        messagebox.showerror('Ошибка ввода данных',
                             'Проверьте введенные данные111')
    except IndexError:
        messagebox.showerror('Ошибка ввода данных',
                             'Проверьте введенные данные222')
        
'''Функция вычисляет сумму,вызывается при нажатие кнопки "Сложить"
   На вход подается блок ввода и блок вывода.

   a_entry - блок ввода
   b_entry -  блок вывода
   a_and_b - массив введеных чисел
   b - сумма, подсчитанная с помощью функции pluss()
   b1 - строка вывода
'''
def plus(a_entry,b_entry):
    a_and_b = list_get(a_entry)
    b_entry.config(state = 'normal')
    b_entry.delete(0, END)
    try:
        if int(a_and_b[0])==(a_and_b[0]):
            a_and_b[0] = int(a_and_b[0])
        if int(a_and_b[1])==(a_and_b[1]):
            a_and_b[1] = int(a_and_b[1])
        b = pluss(a_and_b[0],a_and_b[1], 0)
        
        b1 = str(a_and_b[0])+' + '+str(a_and_b[1])+' = '+str(b)
        b_entry.insert(0, b1)
    except ValueError:
        messagebox.showerror('Ошибка ввода данныых', 'Данные введены неверно\n'
                             'Проверьте праивльность ввода!')
    except TypeError:
        pass

    
'''Функция вычисляет разность,вызывается при нажатие кнопки "Вычесть"
   На вход подается блок ввода и блок вывода.

   a_entry - блок ввода
   b_entry -  блок вывода
   a_and_b - массив введеных чисел
   b - сумма, подсчитанная с помощью функции pluss()
   b1 - строка вывода
'''
def minus(a_entry,b_entry):
    a_and_b = list_get(a_entry)
    b_entry.config(state = 'normal')
    b_entry.delete(0, END)
    try:
        if int(a_and_b[0])==(a_and_b[0]):
            a_and_b[0] = int(a_and_b[0])
        if int(a_and_b[1])==(a_and_b[1]):
            a_and_b[1] = int(a_and_b[1])
        b = minuss(a_and_b[0],a_and_b[1])
        
        b1 = str(a_and_b[0])+' - '+str(a_and_b[1])+' = '+str(b)
        b_entry.insert(0, b1)
    except ValueError:
        messagebox.showerror('Ошибка ввода данныых', 'Данные введены неверно\n'
                             'Проверьте праивльность ввода!')
    except TypeError:
        pass

    
'''Функция очищяет поля ввода/вывода
   На вход подается блоки ввода или локи вывода для очистки.

   *h - блоки ввода/вывода'''
def clean_(*h):
    for a in h:
        a.config(state = 'normal')
        a.delete(0,END)

''' Функция выводит информационное окно о программе.
    При вызове данной функции выводится информационное окно, в котором
    информация о программе, о авторе, о дате создания.

    window - информационное окно
    exit_but - кнопка выхода из информационного окна
'''
def proprog():
    window = Toplevel(roots)
    window.geometry('300x200+600+300')
    window.config(bg = '#8dfcf7')
    window.title('About program')
    window_l = Label(window, text ='Данная программа предназначена\n'
                     'для сложения или вычитания\n'
                     'чисел в пятиричной системе\n\n'
                     'Автор: Козлова Ирина ИУ7-22Б\n'
                     '                   март 2020',
                     font = 'consolas 10',
                     bg = '#8dfcf7', fg = 'black')

    window_l.pack()
    exit_but =  Button(window, text='Выход',width = 15,height = 1,
                   bg = 'white',fg = 'black',
                   command = lambda: roots.destroy())
    exit_but.place(anchor = 'center',x=150, y=150)




''' Первое окно программы '''
roots = Tk()
roots['bg'] = '#e6e6fa'
roots.geometry('400x500+500+200')
roots.title('Calculator')

'''Создание меню, в котором есть команды : "очистить", "Сложить",
   "Вычесь","О программе"
'''
mainmenu = Menu(roots)
roots.config(menu=mainmenu)

cleanmenu = Menu(mainmenu, tearoff=0)
cleanmenu.add_command(label = 'Clear field А and B',
                      command = lambda: clean_(a_entry))
cleanmenu.add_command(label = 'Clear field result',
                      command = lambda: clean_(b_entry))
cleanmenu.add_command(label = 'Clear both fields',
                      command = lambda: clean_(a_entry, b_entry))

filemenu1 = Menu(mainmenu, tearoff=0)
filemenu1.add_command(label = 'Plus',
                      command = lambda: plus(a_entry, b_entry))
filemenu1.add_command(label = 'Minus',
                      command = lambda: minus(a_entry, b_entry))

aboutmenu = Menu(mainmenu, tearoff=0)
aboutmenu.add_command(label ='About the program',
                      command = lambda: proprog())

mainmenu.add_cascade(label = 'Clean', menu = cleanmenu)
mainmenu.add_cascade(label = 'Operations', menu = filemenu1)
mainmenu.add_cascade(label = 'Help', menu = aboutmenu)

''' Окна для ввода данных.
    В данные окна уже записаны константы.
    Пользовватель может их менять
'''
start_label = Label(roots, text = ' Сложение и вычитание \
чисел в пятиричной СС ',
                    font = 'consolas 13',bg = '#bdbdf2',fg = 'black')
start_label.pack()

start_label1 = Label(roots, text = '',font = 'consolas',
                     bg = '#e6e6fa',fg = 'black')
start_label1.pack()

a_label = Label(roots, text = 'A and B by space',font = 'consolas 14',
                bg = '#e6e6fa',fg = 'black')
a_label.pack()

a_entry_start = '111 222'
a_entry = Entry(roots, width=30)
a_entry.insert(0, a_entry_start)
a_entry.pack()

b_label = Label(roots, text = 'Result',font = 'consolas 14',
                bg = '#e6e6fa',fg = 'black')
b_label.pack()


b_entry = Entry(roots, width=30, bg = 'white', state= 'readonly')
b_entry.pack()


'''Кнопки 0, 1, 2, 3, 4, -, С, Сумма, Разность, Выход
   пробел, точка "."
'''

'''Вывод кнопок 1, 2, 3, 4, -, c, 0'''
label_but = ['1','2','3','4','-','0']
but = list()
for i in range(6):
    but.append(Button(text = label_but[i],
                          width = 5,
                          height = 2,
                          font = 'consolas 14',
                          bg = 'white',
                          fg = 'black',
                          command = lambda i=i:
                          (a_entry.insert(END, label_but[i]),
                          b_entry.config(state = 'normal'),
                          b_entry.delete(0, END),
                          b_entry.config(state = 'readonly'))))
    if i<2:
        but[i].place(x = 20 + i%2*55, y = 200)
    elif i<4:
        but[i].place(x = 20 + i%2*55, y = 259)
    elif i<6:
        but[i].place(x = 20 + i%2*55, y = 318)

'''Вывод остальных кнопок
   Выход, С, пробел, сумма, разность
'''        
clear_but = Button(text="<- ",
                   width=7,
                   height=2,
                   font='consolas 14',
                   bg='#fdeaa8',
                   fg= 'black',
                   command = lambda i=i:
                          (a_entry.delete(len(a_entry.get()) - 1, END),
                          b_entry.config(state = 'normal'),
                          b_entry.delete(0, END),
                          b_entry.config(state = 'readonly')))
clear_but.place(x=133, y=200)

clear_but1 = Button(text="C ",
                   width=6,
                   height=2,
                   font='consolas 14',
                   bg='#fdeaa8',
                   fg= 'black',
                   command = lambda i=i:
                          (a_entry.delete(0, END),
                          b_entry.config(state = 'normal'),
                          b_entry.delete(0, END),
                          b_entry.config(state = 'readonly')))
clear_but1.place(x=203, y=200)

plus_but = Button(text='Plus ',
                   width=13,
                   height=2,
                   font='consolas 14',
                   bg='#ffb841',
                   fg= 'black',
                   command=lambda: plus(a_entry, b_entry))
plus_but.place(x=133, y=259)

minus_but = Button(text='Minus ',
                   width=13,
                   height=2,
                   font='consolas 14',
                   bg='#ffb841',
                   fg= 'black',
                   command=lambda: minus(a_entry, b_entry))
minus_but.place(x=133, y=318) 

t_but =  Button(roots, text='.',width = 5,height = 2,
                   font='consolas 14',
                   bg = 'white',fg = 'black',
                   command = lambda: a_entry.insert(END, '.'))
t_but.place(x=20, y=375)

sp_but =  Button(roots, text='Space',width = 19,height = 2,
                   font='consolas 14',
                   bg = '#ffffbd',fg = 'black',
                   command = lambda: a_entry.insert(END, ' '))
sp_but.place(x=75, y=375)

exit_but =  Button(roots, text='Exit',width = 10,height = 2,
                   font='consolas 14',
                   bg = '#6495ed',fg = 'black',
                   command = lambda: roots.destroy())
exit_but.place(x=270, y=375)
roots.mainloop()

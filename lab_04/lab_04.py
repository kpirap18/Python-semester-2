''' Данная программа создана для нахождения треугольника
    с вершинами – точками первого множества, внутри которого
    находится одинаковое количество точек из первого
    и из второго множеств.
                                              Козлова Ирина ИУ7-22Б
'''
from tkinter import *
from tkinter import messagebox
from math import *
from itertools import *
from lab_04_1 import *

''' Функция вывода информации о программе.
    Данная функция выводит окно, в котором выводится информация
    для чего предназначена данная программа, кто автор, когда написана
'''
def proprog():
    window = Toplevel(roots)
    window.geometry('300x200+600+300')
    window.config(bg = '#fadbc8')
    window.title('About program')
    window_l = Label(window, text ='Данная программа предназначена\n'
                             'для нахождения треугольника с вершинами\n'
                             'из первого множества, внутри которого\n'
                             'находится одинаковое количество точек\n'
                             'из первого и второго множеств.\n'
                             'Автор: Козлова Ирина ИУ7-22Б\n'
                             '                   апрель 2020',
                     font = 'consolas 10',
                     bg = '#fadbc8',
                     fg = 'black')

    window_l.pack()
    exit_but =  Button(window,
                       text='Выход',
                       bg = 'white',
                       fg = 'black',
                       command = lambda: window.destroy())
    exit_but.place(anchor = 'center',x = 150, y = 150)


''' Функция для очистки полей ввода

    ent - поля ввода, которые надо очистить
'''
def clean_entry(*ent):
    for i in ent:
        i.config(state = 'normal')
        i.delete(0,END)

''' Функция преобразовывает введенные числа в массив чисел.
    Данная функция используется для перевода в массив введенной
    информации о точках (координаты x и y).

    rang - введенные числа
    list_a_b - массив чисел, который подается на выход
'''
def list_get(rang):
    try:
        list_a_b = [float(x) for x in rang.get().strip().split()]
        
        if len(list_a_b) == 0 or isinstance(list_a_b, (str, type(None))):
            raise ValueError
        return list_a_b
    except ValueError:
        messagebox.showerror('Ошибка ввода данных',
                             'Некоректные данные.\n'
                             'Проверьте введенные данные.')
    except IndexError:
        messagebox.showerror('Ошибка ввода данных',
                             'Некоректные данные.\n'
                             'Проверьте введенные данные.')

''' Функция для нахождения длин сторон треугольника.
    Данная функция находит длинц строки с помошью
    функции hypot из модуля math.

    a - координаты первой точки
    b - координаты второй точки
    c - координаты третий точки
    a_side - длина первой стороны
    b_side - длина второй стороны
    c_side -  длина третей стороны
'''
def trian_side(a, b, c):
    a_side = hypot(a[0] - b[0],a[1] - b[1])
    b_side = hypot(b[0] - c[0],b[1] - c[1])
    c_side = hypot(a[0] - c[0],a[1] - c[1])
    return a_side, b_side, c_side

'''Функция для определения треугольника.
    Данная функция определяет, является ли фигура со сторонами a, b, с
    треугольником или нет.

    a - первая сторона
    b - вторая сторона
    c - третья сторона
'''
def is_trian(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return True
    else:
        return False
'''Функция визуализации треугольника и точек из 1 и 2 множества.
    Данная функция визуализирует треугольник и показывает,
    что кол-во точек из 1 и 2 множества равно в треугольнике.

    entry1 - точки 1 множества
    entry2 - точки 2 множества
'''    
def draw(entry1, entry2):
    entry_1 = list_get(entry1)
    entry_2 = list_get(entry2)

    '''Проверка на полноту координат'''
    if entry_1 and entry_2:
        if ((len(entry_1) % 2) or (len(entry_2) % 2)):
            messagebox.showerror('Неполные данные',
                             'Координаты точек введены '
                             'неполностью.\nПроверьте'
                             'введенные данные!!!')
            return False

        '''Разделенее на координаты X и Y'''
        entry_1_x = entry_1[::2]
        entry_1_y = entry_1[1::2]
        
        entry_2_x = entry_2[::2]
        entry_2_y = entry_2[1::2]
        
        all_entry_x = entry_1_x + entry_2_x
        all_entry_y = entry_1_y + entry_2_y
        
        entry_1_xy = [ (entry_1_x[i], entry_1_y[i])
                       for i in range (len(entry_1_x))]
        entry_2_xy = [ (entry_2_x[i], entry_2_y[i])
                       for i in range (len(entry_2_x))]
        
        all_entry_xy = [(all_entry_x, all_entry_y)
                        for i in range(len(all_entry_x))]

        rez_xy = None

        ''' Подборка координат теругольника и проверка
            кол-ва точек внутри треугольника из 1 и 2 множества'''
        for trin_xy in combinations(entry_1_xy, 3):
            count_1 = list()
            count_2 = list()
            trian_sides = trian_side(*trin_xy)
            if is_trian(*trian_sides):
                for i in range(len(entry_1_xy)):
                    first_c = ((trin_xy[0][0] - entry_1_xy[i][0])*
                               (trin_xy[1][1] - trin_xy[0][1]) -
                               (trin_xy[1][0] - trin_xy[0][0]) *
                               (trin_xy[0][1] - entry_1_xy[i][1]))
                    second_c = ((trin_xy[1][0] - entry_1_xy[i][0]) *
                               (trin_xy[2][1] - trin_xy[1][1]) -
                               (trin_xy[2][0] - trin_xy[1][0]) *
                               (trin_xy[1][1] - entry_1_xy[i][1]))
                    third_c = ((trin_xy[2][0] - entry_1_xy[i][0]) *
                               (trin_xy[0][1] - trin_xy[2][1]) -
                               (trin_xy[0][0] - trin_xy[2][0]) *
                               (trin_xy[2][1] - entry_1_xy[i][1]))
                    if ((first_c > 0 and second_c > 0 and third_c > 0) or
                        (first_c < 0 and second_c < 0 and third_c < 0)):
                        count_1.append(entry_1_xy[i])

                for i in range(len(entry_2_xy)):
                    first_c = ((trin_xy[0][0] - entry_2_xy[i][0])*
                               (trin_xy[1][1] - trin_xy[0][1])-
                               (trin_xy[1][0] - trin_xy[0][0])*
                               (trin_xy[0][1] - entry_2_xy[i][1]))
                    second_c =((trin_xy[1][0] - entry_2_xy[i][0])*
                               (trin_xy[2][1] - trin_xy[1][1])-
                               (trin_xy[2][0] - trin_xy[1][0])*
                               (trin_xy[1][1] - entry_2_xy[i][1]))
                    third_c = ((trin_xy[2][0] - entry_2_xy[i][0])*
                               (trin_xy[0][1] - trin_xy[2][1])-
                               (trin_xy[0][0] - trin_xy[2][0])*
                               (trin_xy[2][1] - entry_2_xy[i][1]))
                    if ((first_c > 0 and second_c > 0 and third_c > 0) or
                        (first_c < 0 and second_c < 0 and third_c < 0)):
                        count_2.append(entry_2_xy[i])

                if (len(count_1) == len(count_2) and
                    len(count_1) + len(count_2) != 0):
                    rez_xy = trin_xy
                    break
                
        '''Если не найден треугольник'''            
        if rez_xy is None:
            messagebox.showinfo(
                'Что-то пошло не так',
                'Треугольник не найден. \n'
                'Попробуйте другие точки!')
            return False

        '''Окно для рисования треугольника'''
        draw_root = Toplevel(roots)
        draw_root['bg'] = '#d0f0c0'
        draw_root.grab_set()
        draw_root.geometry('600x710+500+0')
        draw_root.title('Triangle visualization')

        canv = Canvas(draw_root, width = 600, height = 600, bg = '#ffffcd')
        canv.pack()

        '''Маштабирование'''
        xmax = all_entry_x[0]
        xmin = all_entry_x[0]
        ymax = all_entry_y[0]
        ymin = all_entry_y[0]

        for i in range(len(all_entry_x)):
            if all_entry_x[i] > xmax:
                xmax = all_entry_x[i]
            if all_entry_x[i] < xmin:
                xmin = all_entry_x[i]
            if all_entry_y[i] > ymax:
                ymax = all_entry_y[i]
            if all_entry_y[i] < ymin:
                ymin = all_entry_y[i]

        s_x = (600 - 50)/(xmax - xmin)
        s_y = (600 - 50)/(ymax - ymin)
        o_x = -xmin * s_x + 25
        o_y = -ymin * s_y + 25

        '''Прорисовка точек из 1 и 2 множества'''
        for i in range(len(entry_1_x)):
            x = entry_1_x[i] * s_x + o_x
            y = 600 - (entry_1_y[i] * s_y + o_y)
            canv.create_oval(x-6,y-6,
                             x+6,y+6,
                             fill='#b3007d')
        for i in range(len(entry_2_x)):
            x = entry_2_x[i] * s_x + o_x
            y = 600 - (entry_2_y[i] * s_y + o_y)
            canv.create_oval(x-6,y-6,
                             x+6,y+6,
                             fill='#42aaff')
        
        '''Рисование треугольника'''
        rez_draw_xy = list()
        for i in range(len(rez_xy)):
            rez_draw_xy.append(rez_xy[i][0]*s_x+o_x) 
            rez_draw_xy.append(600 - (rez_xy[i][1]*s_y+o_y))
            
        canv.create_line(rez_draw_xy[0],
                         rez_draw_xy[1],
                         rez_draw_xy[2],
                         rez_draw_xy[3],
                         width = 3,
                         fill = 'green')
        canv.create_line(rez_draw_xy[2],
                         rez_draw_xy[3],
                         rez_draw_xy[4],
                         rez_draw_xy[5],
                         width = 3,
                         fill = 'green')
        canv.create_line(rez_draw_xy[4],
                         rez_draw_xy[5],
                         rez_draw_xy[0],
                         rez_draw_xy[1],
                         width = 3,
                         fill = 'green')

        '''Вывод информации про треугольник '''
        r = Label(draw_root,
                  text = 'Информация о точках\n'
                         'Феолетовые точки - точки первого множества\n'
                         'Голубые точки - точки второго множества',
                  font = 'consolas 12',
                  bg = '#d0f0c0',
                  fg = 'black')
        r.pack()
        
        exit_but =  Button(draw_root, text='Exit',
                           font='consolas 12',
                           bg = 'white',
                           fg = 'black',
                           command = lambda: draw_root.destroy())
        exit_but.pack()

'''Точки 1 множества'''
def paint(event):
    global xy1,c1
    python_green = "green"
    x1, y1 = (event.x - 6), (event.y - 6)
    x2, y2 = (event.x + 6), (event.y + 6)
    xy1.append(event.x)
    xy1.append(event.y)
    c1.create_oval(x1, y1, x2, y2, fill=python_green)
    return event

'''Точки 2 множества'''
def delt(event):
    global xy2,c1
    python_white = "blue"
    x1, y1 = (event.x - 6), (event.y - 6)
    x2, y2 = (event.x + 6), (event.y + 6)
    xy2.append(event.x)
    xy2.append(event.y)
    c1.create_oval(x1, y1, x2, y2, fill=python_white, outline=python_white)

'''Для ввода точек через экран'''    
def special():
    global xy1, xy2,c1,root
    ''' Главное окно программы '''
    root = Tk()
    root['bg'] = '#aadaad'
    root.geometry('600x600+500+0')
    root.title("Geometric task")
    c1 = Canvas(root, width=400, height=400, bg="white")
    width = 400
    height = 400
    for line in range(0, width, 20): # range(start, stop, step)
        c1.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')
    for line in range(0, height, 20):
        c1.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')
    c1.pack()

    root.bind('<Button-1>', paint)
    root.bind('<Button-3>', delt)

    roots_label1 = Label(root, text = '',
                        font = 'consolas 12',
                        bg = '#aadaad',
                        fg = 'black')
    roots_label1.pack()

    e_but =  Button(root,
                      text='Visualization',
                      font='consolas 12',
                      bg = 'white',
                      fg = 'black',
                      command = lambda: draw1(xy1[0:len(xy1)-2],xy2, root))
    e_but.pack()

    roots_label01 = Label(root, text = '',
                        font = 'consolas 12',
                        bg = '#aadaad',
                        fg = 'black')
    roots_label01.pack()

    exit_but =  Button(root,
                       text='Exit',
                           font='consolas 12',
                           bg = 'white',
                           fg = 'black',
                           command = lambda: root.destroy())
    exit_but.pack()
        
    root.mainloop()

    
''' Главное окно программы '''
roots = Tk()
roots['bg'] = '#fffacd'
roots.geometry('500x400+500+100')
roots.title('Triangle')

''' Создание меню '''
mainmenu = Menu(roots)
roots.config(menu=mainmenu)

cleanmenu = Menu(mainmenu, tearoff=0)
cleanmenu.add_command(label = 'Clear field 1',
                      command = lambda: clean_entry(set_entry_1))
cleanmenu.add_command(label = 'Clear field 2',
                      command = lambda: clean_entry(set_entry_2))

filemenu1 = Menu(mainmenu, tearoff=0)
filemenu1.add_command(label = 'Visualization',
                      command = lambda: draw(set_entry_1, set_entry_2))
filemenu1.add_command(label = 'Paint points',
                      command = lambda: special())

aboutmenu = Menu(mainmenu, tearoff=0)
aboutmenu.add_command(label ='About the program',
                      command = lambda: proprog())

mainmenu.add_cascade(label = 'Clean', menu = cleanmenu)
mainmenu.add_cascade(label = 'Operations', menu = filemenu1)
mainmenu.add_cascade(label = 'Help', menu = aboutmenu)

roots_label = Label(roots,
                    text = 'Нахождение треугольника по условию',
                    font = 'consolas 14',
                    bg = '#fffadc',
                    fg = 'black')
roots_label.place(x = 90, y = 0)

roots_label1 = Label(roots,
                     text = 'Введите координаты точек первого множества',
                     font = 'consolas 12',
                     bg = '#fffacd',
                     fg = 'black')
roots_label1.place(x = 60, y = 30)

set_entry_1 = Entry(roots, width = 60)
set_entry_1.insert(0,'')
set_entry_1.place(x = 70, y = 60)
c = set_entry_1

roots_label2 = Label(roots,
                     text = 'Введите координаты точек второго множества',
                     font = 'consolas 12',
                     bg = '#fffacd',
                     fg = 'black')
roots_label2.place(x = 60, y = 90)

set_entry_2 = Entry(roots, width = 60)
set_entry_2.insert(0,'')
set_entry_2.place(x = 70, y = 120)

'''Ввод клавиатуры для ввода координат'''
label_but = ['1','2','3','4','5','6','7','8','9']
but = list()
for i in range(9):
    but.append(Button(text = label_but[i],
                          width = 3,
                          height = 2,
                          font = 'consolas 14',
                          bg = '#d9f5fa',
                          fg = 'black',
                          command = lambda i=i:
                          (c.insert(END, label_but[i]))))
               
    if i<3:
        but[i].place(x = 50 + i%3*38, y = 170)
    elif i<6:
        but[i].place(x = 50 + i%3*38, y = 220)
    elif i<9:
        but[i].place(x = 50 + i%3*38, y = 270)
        
clear_but = Button(text=" <- ",
                   width=3,
                   height=2,
                   font='consolas 14',
                   bg='#42aaff',
                   fg= 'black',
                   command = lambda i=i:
                          (c.delete(len(c.get()) - 1, END)))
clear_but.place(x=163, y=170)

clear_but1 = Button(text=" C ",
                   width=3,
                   height=2,
                   font='consolas 14',
                   bg='#42aaff',
                   fg= 'black',
                   command = lambda i=i:
                          (c.delete(0, END)))
clear_but1.place(x=200, y=170)

o_but = Button(text="0",
                   width=3,
                   height=2,
                   font='consolas 14',
                   bg='#d9f5fa',
                   fg= 'black',
                   command = lambda i=i:
                          (c.insert(END, '0')))
o_but.place(x=163, y=220)


o_but = Button(text=".",
                   width=3,
                   height=2,
                   font='consolas 14',
                   bg='#d9f5fa',
                   fg= 'black',
                   command = lambda i=i:
                          (c.insert(END, '.')))
o_but.place(x=200, y=220)


'''Для смены полей ввода'''
def c_ch(event):
    global c,set_entry_2, set_entry_1
    if c == set_entry_2:
        c = set_entry_1
    if c == set_entry_1:
        c = set_entry_2

ss_but = Button(text="Enter",
                   width=7,
                   height=2,
                   font='consolas 14',
                   bg='#d9f5fa',
                   fg= 'black',
                   command = lambda: c_ch(1))
ss_but.place(x=160, y=270)

o_but = Button(text="  ",
                   width=18,
                   height=1,
                   font='consolas 14',
                   bg='#d9f5fa',
                   fg= 'black',
                   command = lambda i=i:
                          (c.insert(END, ' ')))
o_but.place(x=50, y=320)

vis_button = Button(roots,
                    text = 'Visualization',
                    font = 'consolas 12',
                    bg = 'white',
                    fg = 'black',
                    command=lambda:draw(set_entry_1, set_entry_2))
vis_button.place(x = 300, y = 200)

'''Переменные для ввода точек "тыкать"'''
def new():
    global root, c, xy1, xy2
    root = 0
    c1 = 0     
    xy1 = list()
    xy2 = list()
vis1_button = Button(roots,
                    text = 'Paint points',
                    font = 'consolas 12',
                    bg = 'white',
                    fg = 'black',
                    command=lambda i = i:
                     ( new(),
                       special()))
vis1_button.place(x = 305, y = 250)

exit_but =  Button(roots,
                   text='Exit',
                   font='consolas 12',
                   bg = 'white',
                   fg = 'black',
                   command = lambda: roots.destroy())
exit_but.place(x = 345, y = 300)

'''Для смены полей ввода'''
def c_ch(event):
    global c,set_entry_2, set_entry_1
    if c == set_entry_2:
        c = set_entry_1
    if c == set_entry_1:
        c = set_entry_2
roots.bind("<Return>", c_ch)

'''Переменные для ввода точек "тыкать"'''
root = 0
c1 = 0     
xy1 = list()
xy2 = list()

roots.mainloop()

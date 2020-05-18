from tkinter import *
from tkinter import messagebox
from math import *
from itertools import *

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
def trian_side1(a, b, c):
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
def is_trian1(a, b, c):
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
def draw1(entry_1, entry_2, root):
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
            trian_sides = trian_side1(*trin_xy)
            if is_trian1(*trian_sides):
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
        draw_root = Toplevel(root)
        draw_root['bg'] = '#d0f0c0'
        draw_root.grab_set()
        draw_root.geometry('600x750+500+0')
        draw_root.title('Triangle visualization')

        canv = Canvas(draw_root, width = 600, height = 600, bg = '#d0f2c0')
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
            y = (entry_1_y[i] * s_y + o_y)
            canv.create_oval(x-6,y-6,
                             x+6,y+6,
                             fill='#b3007d')
        for i in range(len(entry_2_x)):
            x = entry_2_x[i] * s_x + o_x
            y = (entry_2_y[i] * s_y + o_y)
            canv.create_oval(x-6,y-6,
                             x+6,y+6,
                             fill='#42aaff')
        
        '''Рисование треугольника'''
        rez_draw_xy = list()
        for i in range(len(rez_xy)):
            rez_draw_xy.append(rez_xy[i][0]*s_x+o_x) 
            rez_draw_xy.append((rez_xy[i][1]*s_y+o_y))
            
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
                           command = lambda: root.destroy())
        exit_but.pack()

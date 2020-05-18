''' Данная программа написана для защиты лабораторной
    работы №2 по программированию на языке Python
    Автор: Козлова Ирина, МГТУ им Баумана ИУ7-22Б '''

from tkinter import *
from tkinter import messagebox

''' Функция преобразовывает считываемую строку в массив

    rang - переменная для считывания информации
    list_a_b - список координат (x и y вместе)
'''
def list_get(rang):
    try:
        list_a_b = []
        
        list_a_b = [float(x) for x in rang.get().strip().split()]
        
        if len(list_a_b) == 0 or len(list_a_b) > 10 or\
           (len(list_a_b) % 2 != 0):
            raise ValueError
              
        return list_a_b
    except ValueError:
        messagebox.showerror('Ошибка ввода данных',
                             'Проверьте введенные данные')
    except IndexError:
        messagebox.showerror('Ошибка ввода данных',
                             'Проверьте введенные данные')

''' Функция для поиска ближайших точек из введенных

    x, y - координаты точек
    mini, minj - номера искомых точек
    s, mins - расстояние и миниальное расстояние
'''
def bliz():
    global x, y
    mins = ((x[0]-x[1])**2+(y[0]-y[1])**2)**(1/2)
    mini = 0
    minj = 1
    n = round(len(x))
    for i in range(n):
        for j in range(n):
            if i!=j:
                s = ((x[i]-x[j])**2+(y[i]-y[j])**2)**(1/2)
                if mins>s:
                    mins = s
                    mini = i
                    minj = j
    return x[mini], y[mini], x[minj], y[minj]

''' Функция для поиска дальних точек из введенных

    x, y - координаты точек
    maxi, maxj - номера искомые точки
    s, maxs - расстояние и максимальное расстояние
'''
def dal(enty):
    global x, y
    maxs = ((x[0]-x[1])**2+(y[0]-y[1])**2)**(1/2)
    maxi = 0
    maxj = 1
    n = round(len(x))
    for i in range(n):
        for j in range(n):
            if i!=j:
                s = ((x[i]-x[j])**2+(y[i]-y[j])**2)**(1/2)
                if maxs<s:
                    maxs = s
                    maxi = i
                    maxj = j
    return x[maxi], y[maxi], x[maxj], y[maxj]    

''' Данная функция срабаттывает при нажатии на кнопку Rast

    a - для определении какое расстояние необходимо искать
    x, y - координаты точек
    a_a - список координат точек(x и y подряд)
    x1, x2, y1, y2 - координты искоых точек
    s - переменная для записи текста на экран
    window - окно для вывода информации
    ent - переменная для вывода текста (s)
'''  
def rast(ent):
    try:
        global x, y
        x = []
        y = []
        a_a = list_get(ent)
        
        for i in range(len(a_a)):
            if (i % 2 ==0):
                x.append(a_a[i])
            else:
                y.append(a_a[i])
        a = sel.get()
        if a == 1:
            x1,y1,x2,y2 = bliz()
            window = Toplevel(roots)
            window.grab_set()
            window.focus_set()
            window.geometry('300x100+700+100')
            window.title('Nearest Point')
            window['bg'] = '#ea8df7'
            s = 'Nearest points'+'\nFirst point '+str(x1)+' '+str(y1)+\
                '\nSecond point '+str(x2)+' '+str(y2)+'\nDistance '+\
                str(round(((x1-x2)**2+(y1-y2)**2)**(1/2),6))
                
            ent = Label(window, text = s,
                        font = 'consolas 15', bg = '#ea8df7')
            ent.pack()
        elif a == 2:
            x1,y1,x2,y2 = dal(ent)
            window = Toplevel(roots)
            window.grab_set()
            window.focus_set()
            window.geometry('300x100+700+100')
            window.title('Farthest Point')
            window['bg'] = '#ea8df7'
            s = 'Farthest point'+'\nFirst point '+str(x1)+' '+str(y1)+\
                '\nSecond point '+str(x2)+' '+str(y2)+'\nDistance '+\
                str(round(((x1-x2)**2+(y1-y2)**2)**(1/2),6))
                
            ent = Label(window, text = s,
                        font = 'consolas 15', bg = '#ea8df7')
            ent.pack()
    except:
        pass

''' Функция для вывода всех точек на экран

    x, y - координаты точек
    a_a - список координат точек(x и y подряд)
    window - окно для вывода информации
    e - переменная для вывода текста на экран
    s - переменная для записи текста
'''
def spicok(ent):
    try:
        global x, y
        x = []
        y = []
        a_a = list_get(ent)
        for i in range(len(a_a)):
            if (i % 2 ==0):
                x.append(a_a[i])
            else:
                y.append(a_a[i])
        window = Toplevel(roots)
        window.grab_set()
        window.focus_set()
        window.geometry('300x500+700+100')
        window.title('All points')
        window['bg'] = '#ea8df7'
        e = Label(window, text = 'All points',
                  font = 'consolas 17', bg = '#ea8df7')
        e.pack()
        for i in range(len(x)):
            s = str(i+1)+' point ('+str(x[i])+','+str(y[i])+')'
            e = Label(window, text = s,
                      font = 'consolas 14', bg = '#ea8df7')
            e.pack()
    except:
        pass
   
''' Главное окно программы '''
roots = Tk()
roots['bg'] = '#e6e6fa'
roots.geometry('400x200+500+200')
roots.title('Points')

x = []
y = []

''' Окно для ввода '''
a_label = Label(roots, text = 'X and Y of point(max 5 points)',
                font = 'consolas 14',bg = '#e6e6fa',fg = 'black')
a_label.pack()
a_entry = Entry(roots, width=50)
a_entry.pack()

''' Переключатели '''
sel = IntVar()
rad1 = Radiobutton(roots, text='Nearest points ',font = 'consolas 14',
                bg = '#e6e6fa', value=1, variable = sel )
rad1.pack()

rad2 = Radiobutton(roots, text='Farthest points',font = 'consolas 14',
                bg = '#e6e6fa', value=2,variable = sel)
rad2.pack()

''' Кнопки Rast и Spicok'''
btn = Button(roots, text="Rast",width = 15,height = 1,font = 'consolas 14',
                   bg = '#afdafc',fg = 'black',
             command= lambda: rast(a_entry))
btn.pack()
btn1 = Button(roots, text="Spicok",width = 15,height = 1,font = 'consolas 14',
                   bg = '#afdafc',fg = 'black',
              command= lambda: spicok(a_entry))
btn1.pack() 
roots.mainloop()

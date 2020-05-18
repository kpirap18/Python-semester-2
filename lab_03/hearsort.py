''' Пирамидальная сортировка или сортировка кучей.
    Козлова Ирина ИУ7-22Б
''' 

''' Функция для формировании дерева (или как еще называют кучи).

    arr - исходный массив (в конце функции он изменяется и превращается в кучу или дерево)
    n - размер массива
    i - узел кучи
'''
def heapify(arr, n, i):
    ''' Данный узел, как наибольший корень. '''
    largest = i
    ''' Левый корень поддерева. '''
    l = 2 * i + 1
    ''' Правый корень подерева. '''
    r = 2 * i + 2   

    ''' Проверка на поиск левых и правых поддеревьев. '''
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    ''' Замена корня, если есть больше. '''
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]         
        ''' Если требуется, формирование новой кучи или дерева. '''
        heapify(arr, n, largest)
    

''' Функция пирамидальной сортировки, кучей.

    arr - исходный массив, который изменяется в конце
'''
def heapSort(arr):
    n = len(arr)

    ''' Формирование кучи (родитель больше потомков). '''
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    ''' Корень заменяется с последнем элементом. '''
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

''' Функция печати каждого шага данной сортировки. '''
def heapSort_sbs(arr):
    n = len(arr)
    ''' Строка вывода '''
    str_arr = ''
    
    ''' Формирование кучи (родитель больше потомков). '''
    for i in range(n, -1, -1):
        heapify(arr, n, i)
        arr_copy = arr[:]
    str_arr += ' Сформированная куча (дерево): '+str(arr_copy)+'\n\n'

    ''' Корень заменяется с последнем элементом. '''
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        arr_copy = arr[:]
        str_arr += 'Замена начало и конца массива: '+str(arr_copy)+'\n\n'
        heapify(arr, i, 0)
        arr_copy = arr[:]
        str_arr += ' Сформированная куча (дерево): '+str(arr_copy)+'\n\n'
    return str_arr
    
''' тест 
arr = [4,8,5,-8,-7,2,45]

n = len(arr)

print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i]),
print(heapSort_sbs(arr))
'''

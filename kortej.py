################## Первое задание ########################
print("################ Первое задание #################")
print(" ")
c = (([1, 2], ['012', 'abc']), [4, 3])

print(c[0][1][1][2])
print(" ")
print("#################################################")
##########################################################

################## Второе задание ########################

print("################  Второе задание  ###############")
print(" ")
integer_number = 10
float_number = 3.14
complex_number = 2 + 3j
single_element_tuple = ('Текст',)
empty_tuple = ()
empty_list = []

main_tuple = (integer_number, float_number, complex_number, single_element_tuple, empty_tuple, empty_list)

print(single_element_tuple[0])
print(" ")
print("#################################################")

##########################################################

################## Третье задание ########################

print("################  Третье  задание  ###############")
print(" ")
empty_tuple = ()
string_element = "Апрель"
complex_number = 2 + 3j

inner_tuple_1 = (complex_number, (string_element, empty_tuple))

float_number = 3.14
inner_tuple_2 = (float_number, inner_tuple_1)

integer_number = 15
matryoshka_tuple = (integer_number, inner_tuple_2)

print(matryoshka_tuple[1][1][1][0])
print(" ")
print("#################################################")

##########################################################

################## Четвертое задание #####################

print("################  Четвертое задание ###############")
print(" ")
tuple4 = (1, 2, 3, 4, 5)
first_element = tuple4[0]
third_element = tuple4[2]
first_three = tuple4[0:3]

print(first_element)
print(third_element)
print(first_three)

tuple2 = (1, 2, 3, 4, 5)
first_element2 = tuple2[-5]
third_element2 = tuple2[-3]
first_three2 = tuple2[-5:-2]

print(first_element2)
print(third_element2)
print(first_three2)
print(" ")
print("#################################################")

##########################################################

################## Пятое задание #########################

print("################  Пятое задание  ###############")
print(" ")
f = ((1, 2, ("OK!", 3)), ('tuple', 4), 5)

result = f[0][2][0]
print(result)

print(" ")
print("#################################################")
##########################################################

################## Шестое задание ########################

print("################  Шестое задание  ###############")
print(" ")
g = (3, 's', 1, 5, 's')
count_elements = len(g)
count_s = g.count('s')
index_s = g.index('s')
print("количество всех элементов: ", count_elements, "количество строк s: ", count_s, "индекс первого вхождения s", index_s)
print(" ")
print("#################################################")

##########################################################

################## Седьмое задание #######################

print("################ Седьмое задание ###############")
print(" ")
my_tuple = (['кит', 1, 3], 5)

my_list = my_tuple[0]

my_list[0] = 'кот'

my_list.remove(1)

my_list[-1] = 3 ** 2

new_tuple = (my_list, my_tuple[1])

print("Изменённый кортеж:", new_tuple)

try:
    new_tuple[1] *= 2
except TypeError as er:
    print("Ошибка:", er)
print(" ")
print("#################################################")

##########################################################

################## Восьмое задание #######################

print("################ Восьмое задание ###############")
print(" ")
def tpl_sort(input_tuple):
    if all(isinstance(x, int) for x in input_tuple):
        return tuple(sorted(input_tuple))
    return input_tuple

# Пример использования
test_tuple = (3, 1, 4, 1, 5, 9)
result = tpl_sort(test_tuple)
print(result)  

# Тест с нецелым числом
test_tuple_with_float = (3, 1, 4.5, 1, 5, 9)
result_with_float = tpl_sort(test_tuple_with_float)
print(result_with_float)  
print(" ")
print("#################################################")
##########################################################

################## Девятое задание #######################

print("################ Девятое задание ###############")
print(" ")
def slicer(input_tuple, element):

    if element not in input_tuple:
        return ()  
    first_index = input_tuple.index(element)

    try:
        second_index = input_tuple.index(element, first_index + 1)
        
      
        return input_tuple[first_index:second_index + 1]
    
    except ValueError:
      
        return input_tuple[first_index:]
# Случай 1: Элемент появляется дважды
print(slicer((1, 2, 3, 2, 4, 5), 2))  

# Случай 2: Элемент появляется один раз
print(slicer((1, 2, 3, 4, 5), 3))  

# Случай 3: Элемент не появляется вовсе
print(slicer((1, 2, 3, 4, 5), 6))  
print(" ")
print("#################################################")

##########################################################

################## Десятое задание #######################

print("################ Десятое задание ###############")
print(" ")
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'grade', 'city'])

students = (
    Student('Иван', 20, 4.5, 'Москва'),
    Student('Мария', 21, 4.8, 'Санкт-Петербург'),
    Student('Петр', 19, 4.2, 'Казань'),
    Student('Анастасия', 20, 4.9, 'Екатеринбург'),
    Student('Дмитрий', 22, 4.1, 'Ростов-на-Дону'),
    Student('Елена', 21, 4.6, 'Новосибирск'),
    Student('Сергей', 20, 4.7, 'Красноярск')
)

def good_students(students_tuple):
 
    # Вычисление средней оценки
    average_grade = sum(student.grade for student in students_tuple) / len(students_tuple)
    
    # Формирование списка имен студентов, которые хорошо учатся
    good_students_names = [student.name for student in students_tuple if student.grade >= average_grade]
    
    # Вывод сообщения
    if good_students_names:
        print(f"Ученики {', '.join(good_students_names)} в этом семестре хорошо учатся!")
    else:
        print("Нет студентов, которые хорошо учатся.")

# Вызов функции
good_students(students)
print(" ")
print("#################################################")
##########################################################


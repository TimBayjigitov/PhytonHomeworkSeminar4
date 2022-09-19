# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4
# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

students = {}
students = \
    {
        'Ангела Меркель': 5,
        'Андрей Валетов': 5,
        'Фредди Меркури': 3,
        'Анастасия Пономарева': 4

    }

with open('file.txt', 'w', encoding ='utf8') as stud:
    for i, mark in students.items():
        stud.write(i + ' ' + str(mark) + '\n')

with open('file.txt', 'a', encoding ='utf8') as stud:
    k = 5
    for i, mark in students.items():
        if students[i] == k:
            stud.write('\n'+i.upper() + ' ' + str(mark))
            j = i.upper()
        else:
            stud.write('\n'+i + ' ' + str(mark))





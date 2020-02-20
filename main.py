#!/usr/bin/env python3

import sys

# обрабатываем входные параметры и открываем файл
file_to_open = 'test.txt'
if len(sys.argv) > 2:
    print("Too much param")
    exit()
else:
    if len(sys.argv) == 2:
        file_to_open = sys.argv[1]
f = open(file_to_open)

# Выводим шапку
print("%-20s| %-9s| %-9s| %-9s| %-9s| %-20s| %-12s| %-12s| %-12s| %-20s| %-12s" %
      ("Indicator", "Proper", "Lock", "Commit", "Child", "Locking", "Version", "Num act", "Num last", "User", "File"))
print("-"*200)

# Для каждой строки в файле выполняем следующую операцию
for a in f:
    # удаляем бесполезные строчки с ">"
    if a.find(">")>0:
        continue

    # Имеется двумерный массив сокращение-ассоциация для каждого варианта параметра. Сравниваем все варианты.
    # Если находим подходящий - выводим и звершаем цикл, переходим к следующему параметру.
    # Там где вариантов параметра всего два можно использвоать обычный условынй оператор

    # 1 столбец - элемент был добавлен, удален или иным образом изменен
    col_1_dic = [["A", "Addition"], ["D", "Deletion"], ["M", "Modified"], ["R", "Replaced"], ["C", "Conflict"],
                 ["X", "External definition"], ["I", "Ignored"], ["?", "No version control"], ["!", "Missing"],
                 ["~", "Type changed"], [" ", "No modificat"]]
    for i in col_1_dic:
        if i[0] == a[0]:
            sys.stdout.write("%-20s| " % i[1])
            break

    # 2 столбец - состояние свойств файла или каталога
    col_2_dic = [["M", "Modified"], ["C", "Conflict"], [" ", "No"]]
    for i in col_2_dic:
        if i[0] == a[1]:
            sys.stdout.write("%-9s| " % i[1])
            break

    # 3 столбец - если каталог рабочей копии заблокирован
    if "L" == a[2]:
        sys.stdout.write("%-9s| " % "Locked")
    else:
        sys.stdout.write("%-9s| " % "-")

    # 4 стоблец - если элемент запланирован для добавления с историей
    if "+" == a[3]:
        sys.stdout.write("%-9s| " % "+++")
    else:
        sys.stdout.write("%-9s| " % "-")

    # 5 стоблец - если элемент переключается относительно родительского элемента
    if "S" == a[4]:
        sys.stdout.write("%-9s| " % "Switch")
    else:
        sys.stdout.write("%-9s| " % "Parent")

    # 6 стоблец - информация о блокировке
    col_6_dic = [[" ", "No"], ["K", "Locked in this copy"], ["O", "Locked  by another user"],
                 ["T", "Locked, but stolen"], ["B", "Locked, but broken"]]
    for i in col_6_dic:
        if i[0] == a[5]:
            sys.stdout.write("%-20s| " % i[1])
            break

    # 7 столбец - устаревшая информация
    if "*" == a[6]:
        sys.stdout.write("%-12s| " % "Need update")
    else:
        sys.stdout.write("%-12s| " % "Up-to-date")

    # Теперь обработаем параметры файла, которые не явялеются сокращением. Отрежем начало и разделим на массив. 
    a = a[10:]
    b = a.split()
    
    # Некоторые параметры имеют только имя файла, поэтому проверим колличество парметров перед выводом на экран 

    # 8 столбец - номер рабочей ревизии артефакта
    if len(b)>1:
        sys.stdout.write("%-12s| " % b[0])
    else:
        sys.stdout.write("%-12s| " % "-")

    # 9 столбец - номер ревизии последнего изменения файла
    if len(b) > 1:
        sys.stdout.write("%-12s| " % b[1])
    else:
        sys.stdout.write("%-12s| " % "-")

    # 10 столбец - имя пользователя внесшего изменения
    if len(b) > 1:
        sys.stdout.write("%-20s| " % b[2])
    else:
        sys.stdout.write("%-20s| " % "-")

    # 11 столбец - имя файла
    if len(b) > 1:
        sys.stdout.write("%-12s\n" % b[3])
    else:
        sys.stdout.write("%-12s\n" % b[0])
#11.11.2022
#тип данных - list, tuple
#списки(list), кортежи(tuple)

# new = list(range(1, 4))
# print(new)
#
# new = tuple(new)
# print(new)
# object = (3,)
#
# print(object)
# print(type(object))


# new = list(range(1, 4))
#
# object = [1, 1, 1, 2, 2, 2, 2]
# new = object.copy()
# new[-1] = 5
# print(object == new)
# print(object is new)
#
# print(object)
# print(new)

# max_ap = 1
# for i in object:
#     if object.count(i) > max_ap:
#         max_ap = object.count(i)
#         print('max', max_ap)
#
# print(i if object.count(i) == max_ap else 0)


# print(object.count(5)) - посчитать сколько одинаковых значений
# object.sort() - сортировка
# object.sort(reverse=True) - сортировать наоборот
#print(min(object))
#print(max(object))

"""добавление"""
#object.append('bishkek') - только добавлят в конец списка
#object.insert(3, 100) - на любоев место - индекс, что угодно
#object.extend(new) - расширение списка
#object += new расширени списка

"""удаление"""
#del object[4:7] - удаление с какого по какой
#object = [i for i in object if type(i) != str]
#object.remove(True) - удаление по значению
#object.remove(4.7) - удаление по значению
#не удаляет все похожие значения, а первое по счету
#object.pop(0) - удаляет по индексу
#deleted = object.pop(0) - возвращает удаленное значение

"""изменение"""
# object[0] = object[0].title() - заглавная по индексу
# object[2] += 15 - прибавить по индексу к значениям int
# del object[-1][1], object[-1][1] - удаление по индексу
# object[object.index(False)] = 'Bishkek' - поставить новое значение вместо другого
#object[0],  object[3] = object[3], object[0] - меняет местами


# Задание 3
# 1-ая должна принимать список. Добавлять в этот список элементы 'Element', 'start', 'finish'. Все элементы первоначального списка должны находиться между элементами 'start', 'finish'
# list1 = ['hello', 5, 'John', ]
# list1.insert(0,'Element')
# list1.insert(1, 'start')
# list1.extend(['finish'])
# print(list1)


a = ['hello', 5, 'John', ]
def func(new_list1):
    list1 = ['Element', 'start', 'finish']
    for i in new_list1:
        list1.extend(a)
        list2 = list1
        list2.append(list2.pop(list2.index('finish')))
        
    return list1


print(func([a]))

#2
a = ('x', 5, 'John')
newdict1 = {x: x for x in range(3)}
def func(dict1):
    newdict = dict()
    for key, value_ b in dict1:
       newdict.setdefault(key(a)).append(newdict1)
    return newdict

print(func([a]))
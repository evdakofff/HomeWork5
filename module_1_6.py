#Задание 1: Словари
my_dict = {'Dmitry': 1991, 'Nelly': 1997, 'Anna': 1999}
print('Dict:'+str(my_dict))
print('Existing value:'+ str(my_dict['Nelly']))
print('Not existing value:'+ str(my_dict.get('Pavel', 'Такой ключ отсутствует в словаре')))
my_dict.update({'Ivan': 1992,
               'Evgeny': 1990})
a = my_dict.pop('Ivan')
print('Deleted value:'+ str(a))
print('Modified dictionary:'+ str(my_dict))

#Задание 2: Множества
my_set = {'12', 3, True, '3', 12, False,'12', 3, True, '3', 12, False}
my_set.update(['4', 3.5])
print('Set:'+ str(my_set))
my_set.discard(3.5)
print('Modified set:'+ str(my_set))
import copy

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [list1, list2]

list4 = copy.deepcopy(list3)

for sublist in list3:
    print(f'sublist id: {id(sublist)}')
print('-' * 25)

for sublist in list4:
    print(f'sublist id: {id(sublist)}')
print('-' * 25)

list4[0].append(100)
print(list4)
print(list3)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [list1, list2]

# Copy using the copy method
list4 = list3.copy()
for item in list4:
    print(f'item: {item}')

# Copy using slice syntax
list5 = list3[:]
for item in list5:
    print(f'item: {item}')

list1_id = id(list1)
print(f'list1_id: {list1_id}')

list2_id = id(list2)
print(f'list2_id: {list2_id}')

print('=' * 25)
for sublist in list3:
    print(f'sublist id: {id(sublist)}')
print('-' * 25)

for sublist in list4:
    print(f'sublist id: {id(sublist)}')
print('-' * 25)

list5 = list3[:]
for sublist in list5:
    print(f'sublist id: {id(sublist)}')
print('=' * 25)

list5[0].append(100)
print(list5)
print(list4)
print(list3)

print('=' * 25)

for sublist in list3:
    print(f'sublist id: {id(sublist)}')

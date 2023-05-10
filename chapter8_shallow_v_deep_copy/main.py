list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3=[list1, list2]
print(list3)

list1_id = id(list1)
print(f'list1_id: {list1_id}')

list2_id = id(list2)
print(f'list2_id: {list2_id}')

for sublist in list3:
    print(f'sublist id: {id(sublist)}')

# COpy using the copy method
list4 = list3.copy()
print(list4)
for sublist in list4:
    print(f'sublist id: {id(sublist)}')

# Copy using slice syntax
list5 = list3[:]
print(list5)
for sublist in list5:
    print(f'sublist id: {id(sublist)}')


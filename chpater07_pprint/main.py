import pprint

data = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]]
print(data)
pprint.pprint(data)


grades = [{'Name': 'John', 'Grades': [55, 34, 76], 'Course': 'Csi'},
          {'Name': 'Adam', 'Grades': [71, 55, 64], 'Course': 'MedPharm'},
          {'Name': 'Natalia', 'Grades': [85, 91, 78], 'Course': 'BioSci'},
          {'Name': 'Denise', 'Grades': [68, 71, 82], 'Course': 'Chem'}]
print(grades)

pprint.pprint(grades)

pprint.pprint(grades, width=40)
pprint.pprint(grades, width=20)

pprint.pprint(grades, depth=2)
pprint.pprint(grades, depth=2, width=40)

pprint.pprint(grades, indent=6)

print('-' * 25)
marks_range = list(range(0, 100))
print(marks_range)
pprint.pprint(marks_range, width=40)
pprint.pprint(marks_range, width=40, compact=True)  # added in Python 3.4

print('-' * 25)
data_str = str(grades)
print(data_str)

data_str = pprint.pformat(grades)
print(data_str)

data_str = pprint.pformat(grades, depth=2, width=40, indent=2)
print(data_str)

import ctypes

class Data:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Data({self.value})'


if __name__ == '__main__':
    print('Create data item')
    data = Data(1)

    print('Obtain the id of list object')
    data_id = id(data)

    print('Find the reference count of data')
    ref_count = ctypes.c_long.from_address(data_id).value
    print(f"Reference count for data is: {ref_count}")

    print('Add some more references')
    other_data1 = data
    other_data2 = data

    print('Find the reference count of data now')
    ref_count = ctypes.c_long.from_address(data_id).value
    print(f"Reference count for data is now: {ref_count}")

    print('Reset data to None')
    data = None
    print('Find the reference count of data now')
    ref_count = ctypes.c_long.from_address(data_id).value
    print(f"Reference count for data is now: {ref_count}")

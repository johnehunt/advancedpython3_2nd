import ctypes
import weakref


from main import Data

if __name__ == '__main__':
    print('Create data item')
    data = Data(1)

    print('Obtain the id of list object')
    data_id = id(data)

    print('Find the reference count of data')
    ref_count = ctypes.c_long.from_address(data_id).value
    print(f"Reference count for data is: {ref_count}")

    print('Initial weak ref count')
    weak_ref_count = weakref.getweakrefcount(data)
    print(f"Number of weak references: {weak_ref_count}")

    print('Add a weakref reference')
    weakref_data = weakref.ref(data)

    print('Find the reference count of data now')
    ref_count = ctypes.c_long.from_address(data_id).value
    print(f"Reference count for data is now: {ref_count}")

    print('Find the weak ref count')
    weak_ref_count = weakref.getweakrefcount(data)
    print(f"Number of weak references: {weak_ref_count}")


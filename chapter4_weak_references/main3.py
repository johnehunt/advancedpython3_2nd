import weakref
from main import Data

if __name__ == '__main__':
    print('Create data item')
    data = Data(1)

    # creates a Weak Value Dictionary
    weak_dict = weakref.WeakValueDictionary()

    # inserting value into the dictionary
    weak_dict['info'] = data

    # getting the weak ref count
    print(f'Weak reference count is: {weakref.getweakrefcount(weak_dict)}')
    print(f'weak_dict: {weak_dict}')
    print(f"weak_dict['info']: {weak_dict['info']}")

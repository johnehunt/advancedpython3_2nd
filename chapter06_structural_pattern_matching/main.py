from dataclasses import dataclass


@dataclass
class Click:
    x: int
    y: int


def handle_click(point):
    match point:
        case Click(x, y):
            print(f'Click x={x}, y={y}')
        case _:
            print('Not a click')


cursor = Click(10, 5)
handle_click(cursor)
handle_click('aclick')

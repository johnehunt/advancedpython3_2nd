def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper


@uppercase_decorator
def greeter(name):
    return f"Hello, {name}!"


print(greeter('Denise'))


def my_decorator(func):
    def inner_function():
        print('Before exexcution')
        result = func()
        print('After execution')
        return result
    return inner_function

@my_decorator
def my_function():
    print('The actual functiona is called')
    return 'Hello World'

my_function()
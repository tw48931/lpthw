import functools

def log(func):
    @functools.wraps(func)
    def wrapper():
        print('begin call')
        func()
        print('end call')
    return wrapper

@log    
def func1():
    print('Hello, world!')

@log
def func2():
    print('Songzhentian is handsome!')

func1()
func2()
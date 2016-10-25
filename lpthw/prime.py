def _odd_iter():
    n = 3
    while True:
        yield n
        n = n + 2
    
def _not_divisible(n):
    return lambda x: x % n > 0
    
def prime():
    yield 2
    list = _odd_iter()
    while True:
        n = next(list)
        yield n
        list = filter(_not_divisible(n), list)
        
for x in prime():
    if x < 1000:
        print(x)
    else:
        break
def is_palindrome(n):
    L1 = list(str(n))
    L2 = list(str(n))
    L1.reverse()
    if L1 == L2:
        return True
    else:
        return False
     
output = filter(is_palindrome, range(1, 1000))
print(list(output))
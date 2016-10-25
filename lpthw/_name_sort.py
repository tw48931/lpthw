from operator import itemgetter
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(L, key=itemgetter(0)))
print(sorted(L, key=itemgetter(0), reverse=True))
print(sorted(L, key=itemgetter(1)))
print(sorted(L, key=itemgetter(1), reverse=True))

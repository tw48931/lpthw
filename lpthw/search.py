import os
s = raw_input('Please enter string you want search:')

def search(s):
	print [x for x in os.listdir('.') if os.path.isfile(x) and (s in x)]

search(s)
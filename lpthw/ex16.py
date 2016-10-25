from sys import argv

script, filename = argv

txt = open(filename, 'w')
txt.truncate()

line1 = raw_input("Please enter line1:")
line2 = raw_input("Please enter line2:")
line3 = raw_input("Please enter line3:")

txt.write(line1),
txt.write(line2),
txt.write(line3),

txt.close()


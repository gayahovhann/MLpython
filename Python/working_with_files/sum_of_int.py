num_file = open("number_file.txt", "r" )

every_line = num_file.readline()
s = 0
x = every_line.split(",")

print(x)
for i in x:
    s+= int(i)
print(s)
num_file.close()
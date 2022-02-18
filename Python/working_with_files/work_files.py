# myfile = open("demofile.txt","r")
# print(myfile.readline())


# for line in myfile.readlines():
#     print(line)

fl = open("demofile.txt", "a")
fl.write("It is just example for learning   ")
fl.close()
 
fl = open("demofile.txt", "r")
print(fl.read())
fl.close()
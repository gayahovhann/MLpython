my_file = open("name_surname_age.txt", "r")
every_line = my_file.readlines()


for i in every_line[1:]:
    every_line_list = i.split()

    if every_line_list[0][0] == "B":
        print(every_line_list)
    if int(every_line_list[2]) > 20:
        print (every_line_list)
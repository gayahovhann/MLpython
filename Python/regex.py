import re
#example1
s1 = 'All I want for Christmas is you, baby'

match1 = re.search(r'is', s1)
print(match1.start())
print(match1.end())

#example2
s2 = 'Take me. to church'
match = re.search(r'\.', s2)
print(match)

#example3
str3 = """Hello my Number is 123456789 and
            my friend's number is 987654321"""
ragex = '\d'
match3 = re.findall(ragex, str3)
print(match3)

#example4
p = re.compile('[a-e]')
print(p.findall("My name is Universe"))

#example5
p5 = re.compile('\d')
print(p5.findall('The war has began on 24th February 2022'))

p5 = re.compile('\d+')
print(p5.findall('The war has began on 24th February 2022'))

#example6
p6 = re.compile('\w')
print(p6.findall("He said *  in some_lang."))
 
p6 = re.compile('\w+')
print(p6.findall("He said *  in some_lang."))

p6 = re.compile('\W')
print(p6.findall("He said *  in some_lang."))

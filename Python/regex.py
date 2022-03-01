example1
import re
s1 = 'All I want for Christmas is you, baby'

match1 = re.search(r'is', s1)
print(match1.start())
print(match1.end())
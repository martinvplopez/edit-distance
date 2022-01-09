from editDistance import *
from editDistance_Test import *

# Lectura fichero entrada
first_line = input().split()
lstr1 = int(first_line[0])
lstr2 = int(first_line[1])
str1 = ""
str2 = ""

if lstr1 >= lstr2:
    for i in range(1, lstr1 + 1):
        parts = input().split()
        if len(parts) == 2:
            str1 = str1 + parts[0]
            str2 = str2 + parts[1]
        else:
            str1 = str1 + parts[0]
else:
    for i in range(1, lstr2 + 1):
        parts = input().split()
        if len(parts) == 2:
            str1 = str1 + parts[0]
            str2 = str2 + parts[1]
        else:
            str2 = str2 + parts[0]
print(str1)
print(str2)


# Ejecución comportamiento Memoization y Tabulation
changes, changed = editDistanceMemo(str1,str2)
print(changes, changed)
print(editDistance.editDistanceTabu(str1, str2))

# Unit Test
test=TestEdit()
test.test_distance2()
test.test_distance1()
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
print("\nString1:",str1,"String2:",str2, "\n")


# Ejecución comportamiento Memoization y Tabulation
mchanges, mchanged = editDistanceMemo(str1, str2)
print("*Memoization*")
print("Numero de operaciones",mchanges)
print("Cambios realizados", mchanged, "\n")

tchanges, tchanged = editDistanceTabu(str1, str2)
print("*Tabulation*")
print("Numero de operaciones",tchanges)
print("Cambios realizados", tchanged)

# Unit Test
test=TestEdit()
test.test_distance2()
test.test_distance1()
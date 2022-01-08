import editDistance
from editDistance_Test import *

# Lectura fichero entrada
line= input().split()
str1= line[0]
str2= line[1]

# Ejecución comportamiento Memoization y Tabulation
print(editDistance.editDistanceMemo(str1,str2))
print(editDistance.editDistanceTabu(str1,str2))

# Unit Test
test=TestEdit()
test.test_distance2()
test.test_distance1()
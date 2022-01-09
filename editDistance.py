# Levenshtein Problem
# Este problema cuantifica el coste de hacer que dos strings sean iguales (cada operación tiene coste 1 (insertar, eliminar, sustituir)):
# Ejemplo: (gata,cata)-> 1, (niña,mima)-> 2

import numpy as np


def editDistance(str1, str2):
    def t(n, m):
        # If first string is empty there will be m insertions to be like str2
        if n == 0:
            return m
        # If second string is empty there will be n deletions to be empty
        if m == 0:
            return n
        # If chars are equal no operation is needed
        if str1[n - 1] == str2[m - 1]:
            return t(n - 1, m - 1)
        # If they don´t match we have to compute the minimum cost of the three possible
        else:
            return 1 + min(t(n - 1, m), t(n, m - 1), t(n - 1, m - 1))
    return t(len(str1), len(str2))


def editDistanceMemo(str1, str2):

    memo = {}
    changed = {}

    def t(n, m):
        key = (n, m)
        if key in memo:
            return memo[key]
        if n == 0 and m == 0:
            memo[key] = 0
            return memo[key]
        if n == 0:
            t(0, 0)
            memo[key] = m
            return memo[key]
        if m == 0:
            t(0, 0)
            memo[key] = n
            return memo[key]
        if str1[n - 1] == str2[m - 1]:
            memo[key] = t(n - 1, m - 1)
            return memo[key]
        memo[key] = 1 + min(t(n - 1, m), t(n, m - 1), t(n - 1, m - 1))
        return memo[key]

    def fill_taken(str1, str2):
        i = len(str1)
        k = len(str2)

        if i >= k:
            while i > 0 or k > 0:
                key1 = (i, k)
                key2 = (i - 1, k)

                if k == 0:
                    for l in range(i):
                        changed[i] = str1[i-1]
                        i = i - 1

                elif key2 in memo and memo[key1] <= memo[key2]:
                    i = i - 1
                    k = k - 1
                    key2 = (i, k)
                    if memo[key1] == memo[key2] + 1:
                        changed[i+1] = str1[i]
                elif key2 in memo:
                    if memo[key1] == memo[key2] + 1:
                        changed[i] = str1[i - 1]
                        i = i - 1
                else:
                    i = i - 1
                    k = k - 1


        else:
            while i > 0 or k > 0:
                key1 = (i, k)
                key2 = (i, k - 1)

                if i == 0:
                    for l in range(k):
                        changed[k] = str2[k-1]
                        k = k - 1

                elif key2 in memo and memo[key1] <= memo[key2]:
                    i = i - 1
                    k = k - 1
                    key2 = (i, k)
                    if memo[key1] == memo[key2] + 1:
                        changed[k+1] = str2[k]
                elif key2 in memo:
                    if memo[key1] == memo[key2] + 1:
                        changed[k] = str2[k - 1]
                        k = k - 1
                else:
                    i = i - 1
                    k = k - 1

    changes = t(len(str1), len(str2))
    fill_taken(str1, str2)

    return changes, changed

def editDistanceTabu(str1, str2):
    n = len(str1) + 1
    m = len(str2) + 1
    table = np.zeros((n, m), dtype=int)
    for i in range(1, n):
        table[i][0] = i
    for j in range(1, m):
        table[0][j] = j

    for i in range(1, n):
        for j in range(1, m):
            if str1[i-1] == str2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = min(table[i - 1][j - 1], table[i - 1][j], table[i][j - 1]) + 1

    return table[n-1][m-1]

#print(editDistanceTabu("cat", "gato"))
#print(editDistanceTabu("jajaja", "papa"))
# print(editDistanceMemo("cat", "gato")) # 2
# print(editDistance("sunday", "saturday")) # 3
# print(editDistanceMemo("geek", "gesek")) # 1
# print(editDistanceMemo("jajaja", "papa")) # 4
#print(editDistanceMemo("",""))
# print(editDistanceMemo("jajaaajkhfhafhafjafakfjaoifwo2iofaoijfpqoqwiuhefkjhafahfjhaf afah", "jfakfjafjañlfjpqpowjweoufwwufwuwf")) # Not possible with naive version

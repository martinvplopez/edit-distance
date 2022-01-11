# Levenshtein Problem
# Este problema cuantifica el coste de hacer que dos strings sean iguales (cada operación tiene coste 1 (insertar, eliminar, sustituir)):
# Ejemplo: (gata,cata)-> 1, (niña,mima)-> 2

import numpy as np


def editDistance(str1, str2):
    def t(m, n):
        # If first string is empty there will be m insertions to be like str2
        if m == 0:
            return n
        # If second string is empty there will be n deletions to be empty
        if n == 0:
            return m
        # If chars are equal no operation is needed
        if str1[m - 1] == str2[n - 1]:
            return t(m - 1, n - 1)
        # If they don´t match we have to compute the minimum cost of the three possible
        else:
            return 1 + min(t(m - 1, n), t(m, n - 1), t(m - 1, n - 1))
    return t(len(str1), len(str2))


def editDistanceMemo(str1, str2):

    memo = {}
    changed = {}

    def t(m, n):
        key = (m, n)
        if key in memo:
            return memo[key]
        if m == 0 and n == 0:
            memo[key] = 0
            return memo[key]
        if m == 0:
            t(0, 0)
            memo[key] = n
            return memo[key]
        if n == 0:
            t(0, 0)
            memo[key] = m
            return memo[key]
        if str1[m - 1] == str2[n - 1]:
            memo[key] = t(m - 1, n - 1)
            return memo[key]
        memo[key] = 1 + min(t(m - 1, n), t(m, n - 1), t(m - 1, n - 1))
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

    return changes, dict(sorted(changed.items()))

def editDistanceTabu(str1, str2):

    m = len(str1) + 1
    n = len(str2) + 1
    table = np.zeros((m, n), dtype=int)
    changed = {}

    def fill_table():
        for i in range(1, m):
            table[i][0] = i
        for j in range(1, n):
            table[0][j] = j

        for i in range(1, m):
            for j in range(1, n):
                if str1[i - 1] == str2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = min(table[i - 1][j - 1], table[i - 1][j], table[i][j - 1]) + 1

        return

    def fill_taken(str1, str2):

        i = len(str1)
        k = len(str2)

        if i >= k:
            while i > 0 or k > 0:
                if k == 0:
                    for l in range(i):
                        changed[i] = str1[i - 1]
                        i = i - 1
                elif k > 0 and table[i][k] <= table[i - 1][k]:
                    if table[i][k] == table[i - 1][k - 1] + 1:
                        changed[i] = str1[i - 1]
                    i = i - 1
                    k = k - 1
                else:
                    changed[i] = str1[i - 1]
                    i = i - 1

        else:
            while i > 0 or k > 0:
                if i == 0:
                    for l in range(k):
                        changed[k] = str2[k - 1]
                        k = k - 1
                elif i > 0 and table[i][k] <= table[i][k - 1]:
                    if table[i][k] == table[i - 1][k - 1] + 1:
                        changed[k] = str2[k - 1]
                    i = i - 1
                    k = k - 1
                else:
                    changed[k] = str2[k - 1]
                    k = k - 1

    fill_table()
    fill_taken(str1, str2)

    return table[m - 1][n - 1], dict(sorted(changed.items()))

# print(editDistanceMemo("jajaaajkhfhafhafjafakfjaoifwo2iofaoijfpqoqwiuhefkjhafahfjhaf afah", "jfakfjafjañlfjpqpowjweoufwwufwuwf")) # Not possible with naive version

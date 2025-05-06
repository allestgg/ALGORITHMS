def search_substring(s, sub):
    n = len(s)
    m = len(sub)
    ocurrences = []
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if s[i+j] != sub[j]:
                break
            j += 1
        if j == m:
            ocurrences.append(i)
    return ocurrences

main_string = "abracadabra"
substring = "abra"
results = search_substring(main_string, substring)
print("Ocurrences found it at positions:", results)

# cadena = 11
# subcadena = 4
# 11 - 4 = 7 a partir de 8 ya no cabe la subcadena por lo tanto se suma 1
# abracada 
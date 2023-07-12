def string(str1, str2):
    if len(str1) != len(str2):
        return False
    
    N = len(str1)
    i = 0
    while i < N and str1[i] == str2[i]:
        i = i + 1
    return i == N
    
print(string("ruk", "ruk"))
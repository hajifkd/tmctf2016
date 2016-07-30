nl = [0, 2, 1, 12, 7, 15, 5, 4, 8, 16, 17, 3, 9, 10, 14, 11, 13, 6, 0]
h1 = "654321"
h2 = "qwerty"
h3 = "admin "
pw = ["*"] * (len(nl) - 1)
for i in range(len(nl) / 3):
    pw[nl[i * 3 + 1]] = h1[i]
    pw[nl[i * 3 + 2]] = h2[i]
    pw[nl[i * 3 + 3]] = h3[i]

print ''.join(pw)

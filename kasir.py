# Kode Asli
def p(x, y, z):
    a = x * y
    a = a + (a * 0.11)
    if a > 1000000:
        a = a - 50000
    print("Total: ", a)
    b = z - a
    print("Kembali: ", b)
    return a, b
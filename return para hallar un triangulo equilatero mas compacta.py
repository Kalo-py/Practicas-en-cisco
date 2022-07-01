def esUnTriangulo(a, b, c):
    if a + b <= c or b + c <= a or \
    c + a <= b:
        return False
    return True

print(esUnTriangulo(1, 1, 1))
print(esUnTriangulo(1, 1, 3))

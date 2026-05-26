# Dot product
def dot_product(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result

# Test with example vectors
v1 = [1, 0]
v2 = [0, 1]
v3 = [1, 2]
v4 = [3, 4]

print("Dot product [1,0]·[0,1] =", dot_product(v1, v2))
print("Dot product [1,2]·[3,4] =", dot_product(v3, v4))

# condition evaluation to check if orthogonal
if dot_product(v1, v2) == 0:
    print("[1,0] and [0,1] are orthogonal")
else:
    print("[1,0] and [0,1] are NOT orthogonal")
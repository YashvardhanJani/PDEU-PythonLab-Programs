# 05. Generate all Pythagorean Triplets with side length <= 30.

def pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):  
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c <= limit:
                triplets.append((a, b, int(c)))
    return triplets

limit = 30
triplets = pythagorean_triplets(limit)
print("Pythagorean triplets with side length <= 30:")
for triplet in triplets:
    print(triplet)

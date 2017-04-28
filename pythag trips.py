
def is_triple(a, b, c):
    return a**2 + b**2 == c**2




for a in range(1, 100):
    for b in range(a, 100):
        for c in range(b, 100): 
            if is_triple(a, b, c):
                print a, b, c

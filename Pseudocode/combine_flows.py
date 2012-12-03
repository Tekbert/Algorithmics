
for (a,b) in arcs:
    if f(a,b) > upper_capacity(a,b):
        overflow = f(a,b) - upper_capacity(a,b)
        f(a,b) = f(a,b) - overflow
        f(b,a) = f(b,a) - overflow

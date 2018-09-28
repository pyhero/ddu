a = 5.5
b = 5.4
c = 0.5
d = 0.4
e = -1.2
f = -1.5


def int_t(f):
    if isinstance(f, float):
        if f - int(f) >= 0.5:
            return int(f) + 1
        else:
            return int(f)


print(int_t(a))
print(int_t(b))
print(int_t(c))
print(int_t(d))
print(int_t(e))
print(int_t(f))

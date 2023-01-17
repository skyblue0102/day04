#tuple

a = 'harry',
b = ('harry',)
c = () #empty tuple
d = 'harry', 'ron'  # packing
e = ('hermione')  # string
f = ('harry', 'ron')  # packing
g = ('hermione', )  # string
print(g, id(g))
g = g + f
print(g, id(g))
print(g)
print(g+f)
print(f[1])
x, y = f  #unpacking ('harry', 'ron')
print(y)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

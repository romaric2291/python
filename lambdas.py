

a = lambda x:x**2
print(a(3))
print(a(8))

b = [1,2,3,4]

print(list(map(a,b)))

x = [x**2 for x in b]

print(x)
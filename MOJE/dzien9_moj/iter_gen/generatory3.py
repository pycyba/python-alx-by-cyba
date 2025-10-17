# generator można też tworzyć jako "comprehension"

kwadraty10 = (x*x for x in range(1, 10))
print(kwadraty10)
for x in kwadraty10:
    print(x)
print()

def kwadraty(n):
    return (x*x for x in range(1, n+1))

for x in kwadraty(20):
    print(x)

print()
print(sum(x*x for x in range(1, 11)))

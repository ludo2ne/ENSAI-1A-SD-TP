import random

l10 = list(range(0, 11))
print(l10)

l10desc = list(range(10, -1, -1))
print(l10desc)


l20rand = []
for _ in range(20):
    l20rand.append(random.randint(1, 9))
print(l20rand)


# l20rand = [random.randint(1, 9) for _ in range(20)]


for i, v in enumerate(l20rand):
    if i == v:
        print("index=valeur ", i)


for i, v in enumerate(l20rand):
    if v % 2 == 1:
        l20rand[i] = v * 2


print("x2 ", l20rand)


l20rand = list(set(l20rand))
print("sans doublon ,", l20rand)

l20randnoduplicate = []
for v in l20rand:
    if v not in l20randnoduplicate:
        l20randnoduplicate.append(v)

print("sans doublon2 ,", l20randnoduplicate)


l20rand.sort()


print("sort ", l20rand)


chaine = "I can see that you're giving up It should not mean that much to me"
cpt = 0

for c in chaine:
    if c == "e":
        cpt += 1

print("nb e : ", cpt)
print("nb e2 : ", chaine.count("e"))

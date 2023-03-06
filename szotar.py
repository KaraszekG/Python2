print("Ismerkedés a szótárakkal.")

a = ()
print(type(a))

b = []
print(type(b))

c = {}
print(type(c))

d = set()
print(type(d))
print(d)

d.add(1)
d.add("aaaaaaaaaaaaaa")
d.add(2)

print(d)

d = {1, 2, 3, 4}
print(type(d))
print(d)

c = {1, 2, 3, 4}
print(type(d))
print(c)

gyumolcs = {"nev":"alma",
            "szin":"piros",
            "fajta":"idared"}
print(type(gyumolcs))
print (gyumolcs)
print(gyumolcs["nev"])
print(gyumolcs.get("nev"))
gyumolcs.clear()
print (gyumolcs)

gyumolcs = {"nev":"alma",
            "szin":"piros",
            "fajta":"idared"}
alma = gyumolcs
print (alma)

gyumolcs["szin"] = "Zöld"
print (gyumolcs)
print(alma)

alma = gyumolcs.copy()
alma["szin"] = "Piros"

print(gyumolcs)
print(alma)

szo = "szép"
masik = szo
szo = "fekete"
print(szo, masik)


lista = [1, 2, 3, 456]
l = lista
lista.append("ll")
print(l, lista)




















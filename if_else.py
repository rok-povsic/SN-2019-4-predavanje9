ime = "Franci"

if ime == "Miha":
    print("Pozdravljeni, Miha!")
elif ime == "Franci":
    print("Zdravo, Franci!")
else:
    print("Pozdravljen, neznanec")

starost = int(input("Vpisi stevilo: "))
if starost > 25:
    print("Star si vec kot 25")
elif starost >= 18:
    print("Odrasel si")
else:
    print("Mlad si")

a = "100"
b = "20"
if b > a:
    print("b je vecje kot a")
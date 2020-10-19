N = 0
while True:
    N = int(input())
    if 0 < N <= 100:
        break
    print("Masukan salah, Ulangi!")

angka = []
urutan = 0
positifpertama = -1
negatifpertama = -1
nolpertama = -1

for i in range(N):
    urutan += 1
    bilangan = int(input())
    angka.append(bilangan)
    if (positifpertama == -1) and bilangan > 0:
        positifpertama = urutan
    if (negatifpertama == -1) and bilangan < 0:
        negatifpertama = urutan
    if (nolpertama == -1) and bilangan == 0:
        nolpertama = urutan
    
x = int(input())
if x == 0:
    if nolpertama == -1:
        print("Tidak ada 0")
    else:
        print(nolpertama)
elif x == 1:
    if positifpertama == -1:
        print("Tidak ada positif")
    else:
        print(positifpertama, angka[positifpertama-1])
elif x == -1:
    if negatifpertama == -1:
        print("Tidak ada negatif")
    else:
        print(negatifpertama, angka[negatifpertama-1])
else:
    print("Tidak diproses")

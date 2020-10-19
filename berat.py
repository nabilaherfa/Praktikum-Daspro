banyakSiswa = 0
jumlahBerat = 0
kecil50 = 0
besar100 = 0

while True:
    berat = int(input())
    if berat == -999:
        break
    if berat < 30 or berat > 200:
        continue
    if berat <= 50:
        kecil50 += 1
    if berat >= 100:
        besar100 += 1
    banyakSiswa += 1
    jumlahBerat += berat

if banyakSiswa == 0:
    print("Data kosong")
else:
    print(banyakSiswa)
    print(kecil50)
    print(besar100)
    print(round(jumlahBerat/banyakSiswa))
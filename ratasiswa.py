#Nama : Nabilah Erfariani
#NIM : 16519108
#Tanggal : 22 April 2020
#rogram yang membaca data siswa dari suatu tempat kursus dari suatu file teks
#dan mengurutkan data tersebut ke layar berdasarkan NoInduk secara terurut
#membesar serta menuliskan
#kembali data tersebut dalam keadaan terurut ke layar dan mencari rata-rata
#nilaisiswa
#KAMUS

#Program RataSiswa
import tulisdata

# KAMUS
# namafile: string


# ALGORITMA PROGRAM UTAMA
namafile = input()
tulisdata.TulisDataSiswa(namafile)


fileObject = open(namafile)
arraySiswa = fileObject.readlines()
arraySiswaLength = 0
for row in arraySiswa:
  arraySiswaLength += 1
A = [(99999999,"a",1) for i in range( (arraySiswaLength//3) ) ]
j = 0

#Proses file to Array of tuples
for i in range(0, arraySiswaLength, 3):
        if (i+2 < arraySiswaLength ):
            A[j] = (int(arraySiswa[i] ), str.rstrip(arraySiswa[i+1] ), int(arraySiswa[i+2] ) )
        j += 1
nilai = arraySiswaLength//3
#Insertion sort 
for i in range(nilai):
  extract = A[i]
  for j in range(i-1, -1, -1):
    if A[j][0] > extract[0]:
      A[j+1] = A[j]
      A[j] = extract
    else:
      A[j+1] = extract
      break
#Konsolidasi dan perhitungan rata-rata sekaligus mengeprint output
i = 0
while(i<nilai):
  noInduk = A[i][0]
  sumTotal = 0
  cnt = 0
  while (noInduk == A[i][0] ):
    sumTotal += A[i][2]
    cnt += 1
    i += 1
    if (i == nilai ): break
  ans = float(sumTotal/cnt)
  print(str(noInduk) + "=", end='')
  print("%.2f" % ans)

#Jika kosong
if (nilai == 0): print("File kosong")

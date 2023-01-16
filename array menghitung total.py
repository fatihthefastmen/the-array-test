#deklarasikan array
array = []
#membuat variable total
total = 0
#membuat variable n untuk menampung jumlah array
# n = jumlah elemen
n = int(input("masukan jumlah elemen array : "))
for x in range(n) :
#menginputkan nilai  yang akan bertambah 1
    nilai = float (input("masukan nilai ke- {} :".format(x+1)))
    array.append(nilai)
    #menampilkan jumlah dari nilai
    print("\nmasukan nilai total adalah: {}".format(sum(array)))
    print("hasil rata rata adalah : {}".format(sum(array)))

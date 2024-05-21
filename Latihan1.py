n = int(input('Masukkan jumlah kategori: '))

data_aplikasi = {}

for i in range(n):
    nama_kategori = input('Masukkan nama kategori:')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)

    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)

    data_aplikasi[nama_kategori] = aplikasi

print(data_aplikasi)

daftar_aplikasi_list = []

for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))

print(daftar_aplikasi_list)

hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])

print(hasil)

kemunculan_aplikasi = {}

for aplikasi_set in daftar_aplikasi_list:
    for aplikasi in aplikasi_set:
        if aplikasi in kemunculan_aplikasi:
            kemunculan_aplikasi[aplikasi] += 1
        else:
            kemunculan_aplikasi[aplikasi] = 1

print("Kemunculan aplikasi:", kemunculan_aplikasi)


aplikasi_unik = {aplikasi for aplikasi, count in kemunculan_aplikasi.items() if count == 1}

print("Aplikasi yang hanya muncul di satu kategori:", aplikasi_unik)
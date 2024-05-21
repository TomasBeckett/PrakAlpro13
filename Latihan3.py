def main():
    def baca_file(nama_file):
        try:
            with open(nama_file, 'r') as file:
                isi = file.read().lower()
                kata_kata = set(isi.split())
                return kata_kata
        except FileNotFoundError:
            print(f"Error: File '{nama_file}' tidak ditemukan.")
            return None
        except IOError:
            print(f"Error: File '{nama_file}' tidak bisa dibaca.")
            return None

    nama_file1 = input("Masukkan nama file pertama: ")
    nama_file2 = input("Masukkan nama file kedua: ")

    kata_kata_file1 = baca_file(nama_file1)
    kata_kata_file2 = baca_file(nama_file2)

    if kata_kata_file1 is None or kata_kata_file2 is None:
        return

    kata_kata_common = kata_kata_file1.intersection(kata_kata_file2)
    print("Kata-kata yang muncul pada kedua file:")
    for kata in kata_kata_common:
        print(kata)

main()

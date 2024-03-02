import time
print((5*"=" + " Tugas Operasi Aritmatika Sederhana " + 5*"=").center(50))
print((5*"=" + " + , - , * , // , %, ** " + 5*"=").center(50))
nama = input("Nama: ")
nim = int(input("NIM: "))

print("\n")

print(f"Nama: {nama}")
print(f"NIM: {nim}")

print("\n")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka pertama: "))

tambah = angka1 + angka2
kurang = angka1 - angka2
kali = angka1 * angka2
bagi = angka1 // angka2
modulus = angka1 % angka2
pangkat = angka1 ** angka2

print("\n")
print((5*"=" + " Hasilnya Adalah " + 5*"=").center(50))
print("\n")
print(f"Angka {angka1} + {angka2} = {tambah}")
print(f"Angka {angka1} - {angka2} = {kurang}")
print(f"Angka {angka1} * {angka2} = {kali}")
print(f"Angka {angka1} // {angka2} = {bagi}")
print(f"Angka {angka1} % {angka2} = {modulus}")
print(f"Angka {angka1} ** {angka2} = {pangkat}")
print("\n")
print((5*"=" + " SELESAI " + 5*"=").center(50))
time.sleep(5)


import os

os.system('clear')

nama = input("Masukkan nama anda : ")

os.system('clear')

print("Halo. Selamat datang di program konversi suhu ini", nama, "!!")

jenis_suhu = ["derajat Celcius", "derajat Fahrenheit", "derajat Reamur", "Kelvin"]

while True :
    print("Satuan suhu apa yang sekarang sedang kamu gunakan?")
    print("     1. Celcius")
    print("     2. Fahrenheit")
    print("     3. Reamur")
    print("     4. Kelvin")
    sekarang = int(input("Masukkan pilihan kamu (1/2/3/4) : "))

    os.system('clear')

    print("Baik satuan awal kamu adalah", jenis_suhu[int(sekarang) - 1])
    suhu = input("Masukkan nilai suhu yang akan kamu konversi : ")

    os.system('clear')

    if sekarang == 1 :
        fah = "{:.2f}".format(((float(suhu) * 9) / 5) + 32);
        ream = "{:.2f}".format((float(suhu) * 4) / 5);
        kelv = "{:.2f}".format(float(suhu) + 273.15);
        print("Satuan awal kamu adalah      :", float(suhu), jenis_suhu[0])
        print("Hasil konversi ke Fahrenheit :", fah, jenis_suhu[1])
        print("Hasil konversi ke Reamur     :", ream, jenis_suhu[2])
        print("Hasil konversi ke Kelvin     :", kelv, jenis_suhu[3])

    elif sekarang == 2 :
        celc = "{:.2f}".format(((float(suhu) - 32) * 5) / 9);
        ream = "{:.2f}".format(((float(suhu) - 32) * 4) / 9);
        kelv = "{:.2f}".format((((float(suhu) - 32) * 5) / 9) + 273.15);
        print("Satuan awal kamu adalah      :", float(suhu), jenis_suhu[1])
        print("Hasil konversi ke Celcius    :", celc, jenis_suhu[0])
        print("Hasil konversi ke Reamur     :", ream, jenis_suhu[2])
        print("Hasil konversi ke Kelvin     :", kelv, jenis_suhu[3])

    elif sekarang == 3 :
        celc = "{:.2f}".format((float(suhu) * 5) / 4);
        fah = "{:.2f}".format(((float(suhu) * 9) / 4) + 32);
        kelv = "{:.2f}".format(((float(suhu) * 5) / 9) + 273.15);
        print("Satuan awal kamu adalah      :", float(suhu), jenis_suhu[2])
        print("Hasil konversi ke Celcius    :", celc, jenis_suhu[0])
        print("Hasil konversi ke Fahrenheit :", fah, jenis_suhu[1])
        print("Hasil konversi ke Kelvin     :", kelv, jenis_suhu[3])

    elif sekarang == 4 :
        celc = "{:.2f}".format((float(suhu) - 273.15));
        fah = "{:.2f}".format((((float(suhu) - 273.15) * 9) / 5) + 32);
        ream = "{:.2f}".format(((float(suhu) - 273.15) * 4) / 5);
        print("Satuan awal kamu adalah      :", float(suhu), jenis_suhu[3])
        print("Hasil konversi ke Celcius    :", celc, jenis_suhu[0])
        print("Hasil konversi ke Fahrenheit :", fah, jenis_suhu[1])
        print("Hasil konversi ke Reamur     :", ream, jenis_suhu[2])

    print("\nApakah masih mau melakukan konversi?")
    yesno = input("Yes(y) or no(n) : ")

    if (yesno == 'n') or (yesno == 'N') :
        break

    os.system('clear')

os.system('clear')
print("Terima kasih telah menggunakan.")
print("Program ini dibuat oleh --> Gabriel Cesar Hutagalung <--")
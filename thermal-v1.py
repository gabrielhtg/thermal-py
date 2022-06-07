import os
os.system('clear')

nama = input("Masukkan nama kamu : ")
os.system('clear')

while True :
    print("------------------------------------------------------------------------------------")
    print("Masukkan satuan suhu yang sekarang sedang kamu gunakan!")
    print("     1. Celcius")
    print("     2. Fahrenheit")
    print("     3. Reamur")
    print("     4. Kelvin")
    print("------------------------------------------------------------------------------------")
    satuan1 = input("Masukkan pilihan kamu sesuai dengan angka yang tertera : ")
    print("------------------------------------------------------------------------------------")
    macam = ["derajat Celcius", "derajat Fahrenheit", "derajat Reamur", "Kelvin"]

    os.system('clear')

    print("------------------------------------------------------------------------------------")
    print("Baik. Berarti kamu sekarang dalam satuan suhu " + macam[int(satuan1) - 1])
    print("------------------------------------------------------------------------------------")
    print("Mau kamu konversi ke satuan suhu apa?")
    print("     1. Celcius")
    print("     2. Fahrenheit")
    print("     3. Reamur")
    print("     4. Kelvin")
    print("------------------------------------------------------------------------------------")
    satuan2 = input("Masukkan pilihan kamu sesuai dengan angka yang tertera : ")
    print("------------------------------------------------------------------------------------")
    print("Baik. Berarti kamu akan mengonversi dari " + macam[int(satuan1) - 1] + " ke " + macam[int(satuan2) - 1])
    suhu = input("Sekarang, masukkan nilai suhu yang akan kamu konversi : ")

    print("------------------------------------------------------------------------------------")
    if satuan1 == satuan2 :
        print("Hasil konversinya adalah", suhu, macam[int(satuan2) - 1])

    elif (satuan1 == '1') and (satuan2 == '2') :
        print("Hasil konversinya adalah", "{:.2f}".format(((float(suhu) * 9) / 5) + 32), macam[int(satuan2) - 1])

    elif (satuan1 == '1') and (satuan2 == '3') :
        print("Hasil konversinya adalah", "{:.2f}".format((float(suhu) * 4) / 5), macam[int(satuan2) - 1])

    elif (satuan1 == '1') and (satuan2 == '4') :
        print("Hasil konversinya adalah", "{:.2f}".format(float(suhu) + 273.15), macam[int(satuan2) - 1])

    elif (satuan1 == '2') and (satuan2 == '1') :
        print("Hasil konversinya adalah", "{:.2f}".format(((float(suhu) - 32) * 5) / 9), macam[int(satuan2) - 1])

    elif (satuan1 == '2') and (satuan2 == '3') :
        print("Hasil konversinya adalah", "{:.2f}".format((((float(suhu) - 32) * 4) / 9)), macam[int(satuan2) - 1])

    elif (satuan1 == '2') and (satuan2 == '4') :
        print("Hasil konversinya adalah", "{:.2f}".format((((float(suhu) - 32) * 5) / 9) + 273.15), macam[int(satuan2) - 1])

    elif (satuan1 == '3') and (satuan2 == '1') :
        print("Hasil konversinya adalah", "{:.2f}".format((float(suhu) * 5) / 4), macam[int(satuan2) - 1])

    elif (satuan1 == '3') and (satuan2 == '2') :
        print("Hasil konversinya adalah", "{:.2f}".format(((float(suhu) * 9) / 4) + 32), macam[int(satuan2) - 1])

    elif (satuan1 == '3') and (satuan2 == '4') :
        print("Hasil konversinya adalah", "{:.2f}".format(((float(suhu) * 5) / 9) + 273.15), macam[int(satuan2) - 1])

    elif (satuan1 == '4') and (satuan2 == '1') :
        print("Hasil konversinya adalah", "{:.2f}".format(float(suhu) - 273.15), macam[int(satuan2) - 1])

    elif (satuan1 == '4') and (satuan2 == '2') :
        print("Hasil konversinya adalah", "{:.2f}".format((((float(suhu) - 273.15) * 9) / 5) + 32), macam[int(satuan2) - 1])

    elif (satuan1 == '4') and (satuan2 == '3') :
        print("Hasil konversinya adalah", "{:.2f}".format(((float(suhu) - 273.15) * 4) / 5), macam[int(satuan2) - 1])

    print("------------------------------------------------------------------------------------")
    print("Apakah masih ingin melakukan koversi?")
    yesno = input("Yes (y) or no (n) : ")

    if (yesno == 'n') or (yesno == 'N') :
        break

    os.system('clear')

os.system('clear')

print("Terima kasih telah menggunakan.")
print("This program created by --> Gabriel Cesar Hutagalung <--")
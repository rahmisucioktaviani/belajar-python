print("selamat datang DI dafun")
nama = input("masukkan namamu : ")
umur = input("masukkan umurmu : ")
if(int(umur) > 10):
    print("halo" , nama , "selamat datang di dafun")
else :
    print("maaf anda tidak bisa menikmati wahan di dafun")

daftar_wahana = ["biang lala RP. 13.000" , "istana boneka RP. 10.000" , "rumah kaca RP. 15.000" , "roller coaster RP. 20.000 "]
print(" daftar wahana")
angka = 1
for wahana in daftar_wahana :
    print(str(angka) +" . " + wahana)
    angka = angka + 1

pilihan = input("masukkan pilihanmu")
if pilihan == "1" :
     print(" tiket RP. 13.000 + pajak RP 2.000 Total keseluruhan RP. 15.000")
elif pilihan == "2" :
    print("tiket RP 10.000 + Pajak RP 2.000 Total keseluruhan RP. 12.000")
elif pilihan == "3" :
    print("tiket RP 15.000 + pajak RP 2.000 total keseluruhan RP 17.000")
elif pilihan == "4" :
    if (int(umur) > 16 ) :
        print("tiket RP 20.000 + pajak RP 2.000 total keseluruhan RP 22.000")
    else : 
        print("anda belum cukup umur untuk bermain wahana ini")










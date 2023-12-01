def menyapa(nama , tempat) :
    print("haloooooo" , nama)
    print("selamat datang di" , tempat)

menyapa("salman" , "rpl")
menyapa("siti" , "kandang ayam" )



def hitung(angka1, angka2, operasi):
    if operasi == "+":
        return angka1 + angka2
    elif operasi == "*":
        return angka1 * angka2
    else:
        return "Operasi tidak valid"
                                    
                                    
def perulangan(kata, jumlah):
        for _ in range(jumlah):
           print(kata)

print(hitung(2, 4, "*"))   
print(hitung(4, 5, "+"))   
print(hitung(10, 5, "-"))  

perulangan("haiii salman", 4)
perulangan("selamat datang", 2)
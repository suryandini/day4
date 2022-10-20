#dasar-dasar phyton
#Aturan1: penulisan satu statement di dalam phyton tidak di akhiri dengan tanda titik koma.
print("Hello dunia")
panjang = 200
print ("panjang" , panjang)

#Aturan2: statement pada phyton dinyatakan dalam satu baris. jadi akhir dari sebuah pernyataan adalah baris baru (new line)
panjang = 25
lebar = 30
luas = panjang*lebar
print ("luas =",luas)

#Aturan3 :jika ada pernyataan yang panjangnya terdiri lebih dari 1 baris, maka dapat dilakukan dengan menggunakan tanda backslash("\")
panjang = 300
lebar = 30
tinggi = 20
volume = panjang * lebar *\
         tinggi
print ("volume =",volume)

#Aturan4 : statement yang ada di dalam atau diapit oleh tanda kurung seperti "[].{}.()" tidak memerlukan tanda "\"
panjang = 300
lebar = 30
tinggi = 20
volume = (panjang * lebar * tinggi)
print ("volume =", volume)

#Aturan5 : Phyton menggunakan tanda indentasi (spasi) sebagai penanda blok. panjang spasi
#atau indentasi untuk setiap baris yang ada di dalam satu blok kode harus sama. bila spasi atau indentasi
#dalam satu grup kode tersebut tidak sama. phyton akan menampilkan sintaks eror
usia = 17
if usia >20:
    print("di terima masuk SMP")
    print("dinyatakan lulus")
else:
    print("tidak di terima masuk SMP")
    print("dinyatakan gagal")
print ('teks ini di cetak terus')


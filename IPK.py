algoritma = float(input("Masukan nilai algoritma :"))
perancangan_objek = float(input("masukan nilai perancangan_objek :"))
kalkulus = float(input("masukan nilai B. kalkulus :"))
Etika_Profesi = float(input("masukan nilai Etika_profesi :"))
data_base = float(input("masukan nilai data_base :"))
english = float(input("masukan nilai english :"))

rata2 = (algoritma+perancangan_objek+kalkulus+Etika_Profesi+data_base+english)/6
bobot = rata2/25
if rata2 >= 90 :
    hasil = "A"
elif rata2 >= 85 :
    hasil = "A-"  
elif rata2 >= 80 :
    hasil = "A/B" 
elif rata2 >= 75 :
    hasil = "B+"   
elif rata2 >= 70 :
    hasil = "B" 
elif rata2 >= 65 :
    hasil = "B-" 
elif rata2 >= 60 :
    hasil = "B/C" 
elif rata2 >= 55 :
    hasil = "C+" 
elif rata2 >= 50 :
    hasil = "C" 
elif rata2 >= 45 :
    hasil = "C-" 
elif rata2 >= 40 :
    hasil = "C/D" 
elif rata2 >= 35 :
    hasil = "D+" 
elif rata2 >= 30 :
    hasil = "D"                              
else :
    hasil = "E"  

print("Nilai rata rata anda pada semster ini adalah ", rata2 , "Bobotnya adalah ", bobot , "jika di konversikan menjadi huruf ", hasil)    
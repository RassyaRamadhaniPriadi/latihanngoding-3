kalkulus = int(input("Masukan nilai kalkulus :"))
statistika = int(input("masukan nilai statistika :"))
logika = int(input("masukan nilai B. logika :"))
algoritma = int(input("masukan nilai algoritma :"))
orkom = int(input("masukan nilai orkom :"))

planA = (kalkulus+statistika+logika+algoritma+orkom)/5

if planA <50:
    hasil = "E"
elif planA <60 :
    hasil = "D"  
elif planA < 70 :
    hasil = "C" 
elif planA < 80 :
    hasil = "B"        
else :
    hasil = "A"  

print("rata-rata nilai anda adalah", planA , "dan jika di konversikan maka menjadi", hasil)
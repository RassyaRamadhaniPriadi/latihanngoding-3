english = int(input("Masukan nilai B. inggris :"))
mtk = int(input("masukan nilai mtk :"))
indo = int(input("masukan nilai B. indo :"))
ipa = int(input("masukan nilai IPA :"))
ips = int(input("masukan nilai IPS :"))

planA = (english+mtk+indo+ipa+ips)/5
if planA >= 75:
    hasil = "Selamat anda lulus"
else :
    hasil =  "Mohon maaf anda tidak lulus"

print(hasil)       
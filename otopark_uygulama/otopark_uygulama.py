import tkinter as tk
import random
import json
from tkinter import messagebox

def otopark_durumunu_guncelle():
    secili_otopark = otoparklar_listesi.get(tk.ACTIVE)
    yeni_durum = otopark_durumu_giris.get()
    messagebox.showinfo("Otopark Durum Güncellemesi", "Seçtiğiniz otoparkın durumu güncellenmiştir")



    for i in range(len(otoparklar)):
        if otoparklar[i]["ad"] == secili_otopark:
            otoparklar[i]["durum"] = yeni_durum

    otopark_durumu_goster()

    with open("otoparklar.json", "w") as file:
        json.dump(otoparklar, file)

def otopark_durumu_goster():
    otopark_durumu_frame = tk.Toplevel(root)
    otopark_durumu_frame.title("Otopark Durumu")


    for otopark in otoparklar:
        label = tk.Label(otopark_durumu_frame, text=f"{otopark['ad']}: {otopark['durum']}")
        label.pack(pady=5)

def engelli_rezerve_et():
    secili_otopark = otoparklar_listesi.get(tk.ACTIVE)
    messagebox.showinfo("Engelli Rezervasyon", "Otopark sizin için ayırtıldı. 15 dakika sonra rezerveniz kalkacaktır")

    for i in range(len(otoparklar)):
        if otoparklar[i]["ad"] == secili_otopark:
            if otoparklar[i]["durum"] == "Boş":
                otoparklar[i]["durum"] = "Engelli Rezerve"
                otopark_durumu_goster()
                break

    with open("otoparklar.json", "w") as file:
        json.dump(otoparklar, file)

def kullanici_girisi():
    kullanici_adi = kullanici_adi_giris.get()
    sifre = sifre_giris.get()

    if kullanici_adi == "admin" and sifre == "admin123":
        otopark_durumu_goster_1.pack()
        otopark_guncelleme_frame.pack() 
    else:
        otopark_guncelleme_frame.pack_forget()  

    if kullanici_adi == "engelli" and sifre == "engelli123":
        otopark_durumu_goster_1.pack()
        engelli_rezerve_et_dugmesi.pack()
    else:
        engelli_rezerve_et_dugmesi.pack_forget()
    
    if kullanici_adi == "vatandas" and sifre == "vatandas123":
        otopark_durumu_goster_1.pack()
    

        
otoparklar = [
    {"ad": "Otopark 1", "durum": random.choice(["Boş", "Dolu", "Engelli Rezerve"])},
    {"ad": "Otopark 2", "durum": random.choice(["Boş", "Dolu", "Engelli Rezerve"])},
    {"ad": "Otopark 3", "durum": random.choice(["Boş", "Dolu", "Engelli Rezerve"])},
    {"ad": "Otopark 4", "durum": random.choice(["Boş", "Dolu", "Engelli Rezerve"])},
    {"ad": "Otopark 5", "durum": random.choice(["Boş", "Dolu", "Engelli Rezerve"])},
]

try:
    with open("otoparklar.json", "r") as file:
        otoparklar = json.load(file)
except FileNotFoundError:
    with open("otoparklar.json", "w") as file:
        json.dump(otoparklar, file)

root = tk.Tk()
root.title("Otopark Uygulaması")
root.geometry("400x550")

kullanici_giris_frame = tk.Frame(root)
kullanici_giris_frame.pack(pady=20)

kullanici_adi_etiket = tk.Label(kullanici_giris_frame, text="Kullanıcı Adı:")
kullanici_adi_etiket.pack()

kullanici_adi_giris = tk.Entry(kullanici_giris_frame)
kullanici_adi_giris.pack(pady=5)

sifre_etiket = tk.Label(kullanici_giris_frame, text="Şifre:")
sifre_etiket.pack()

sifre_giris = tk.Entry(kullanici_giris_frame, show="*")
sifre_giris.pack(pady=5)

giris_dugmesi = tk.Button(kullanici_giris_frame, text="Giriş Yap", command=kullanici_girisi)
giris_dugmesi.pack(pady=10)

otoparklar_listesi = tk.Listbox(root)
otoparklar_listesi.pack(pady=10)

for otopark in otoparklar:
    otoparklar_listesi.insert(tk.END, otopark["ad"])

otopark_durumu_giris = tk.Entry(root)
otopark_durumu_giris.pack(pady=5)

otopark_guncelleme_frame = tk.Frame(root)
engelli_rezerve_et_dugmesi = tk.Frame(root)
otopark_durumu_goster_1 = tk.Frame(root)


guncelle_dugmesi = tk.Button(otopark_guncelleme_frame, text="Güncelle", command=otopark_durumunu_guncelle)
guncelle_dugmesi.pack(pady=5)

rezerve_et_dugmesi = tk.Button(engelli_rezerve_et_dugmesi, text="Engelli Rezerve Et", command=engelli_rezerve_et)
rezerve_et_dugmesi.pack(pady=5)

otopark_durumu_goster_dugmesi = tk.Button(otopark_durumu_goster_1, text="Otopark Durumu Göster", command=otopark_durumu_goster)
otopark_durumu_goster_dugmesi.pack(pady=10)

root.mainloop()

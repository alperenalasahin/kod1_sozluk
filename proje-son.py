import tkinter as tk
from tkinter import messagebox
import json
import hashlib
import os

data_file = "country_info.json"
info_file = "country_info_details.json" 
psw_info = {} 

default_country_info = {
    "Türkiye": "Türkiye'nin küresel ısınma ile mücadelede...",
    "ABD": "ABD'nin küresel ısınma ile mücadelede...",
    "Çin": "Çin'in küresel ısınma ile mücadelede...",
}

if not os.path.exists(data_file):
    with open(data_file, "w") as file:
        json.dump(default_country_info, file)

try:
    with open(data_file, "r") as file:
        country_info = json.load(file)
except FileNotFoundError:
    country_info = default_country_info

if not os.path.exists(info_file):
    with open(info_file, "w") as file:
        json.dump({country: "" for country in country_info}, file)

try:
    with open(info_file, "r") as file:
        country_info_details = json.load(file)
except FileNotFoundError:
    country_info_details = {country: "" for country in country_info}

def hashed_psw(psw):
    try:
        with open("psw_info.json", "r") as file:
            psw_info = json.load(file)
            md5_hash = hashlib.md5()
            md5_hash.update(psw.encode('utf-8'))
            hashed_value = md5_hash.hexdigest()
            if psw_info["uye"] == hashed_value:
                return True
            else:
                return False
    except FileNotFoundError:
        psw_info = default_country_info

def save_data():
    with open(data_file, "w") as file:
        json.dump(country_info, file)

def save_info():
    with open(info_file, "w") as file:
        json.dump(country_info_details, file)

def show_info():
    selected_country = country_var.get()
    info = country_info.get(selected_country, "Bu ülke hakkında bilgi bulunamadı.")
    detailed_info = country_info_details.get(selected_country, "Detaylı bilgi bulunamadı.")

    info_window = tk.Toplevel(root)
    info_window.title(selected_country + " - Bilgi")

    formatted_info = '\n'.join([info[i:i+60] for i in range(0, len(info), 60)])
    formatted_detailed_info = '\n'.join([detailed_info[i:i+60] for i in range(0, len(detailed_info), 60)])

    label = tk.Label(info_window, text=f"Genel Bilgi:\n{formatted_info}\n\nDetaylı Bilgi:\n{formatted_detailed_info}", padx=20, pady=20, justify="left")
    label.pack()

def check_password():
    username = username_entry.get()
    password = password_entry.get()
    
    if (username == "admin" and hashed_psw(password)):
        admin_window = tk.Toplevel(root)
        admin_window.title("Yönetici Paneli")
        
        def update_info():
            selected_country = country_var.get()
            new_info = info_entry.get()
            country_info[selected_country] = new_info
            save_data()
            messagebox.showinfo("Başarılı", f"{selected_country} bilgisi güncellendi!")

        edit_frame = tk.Frame(admin_window, padx=20, pady=20)
        edit_frame.pack()

        country_label_admin = tk.Label(edit_frame, text="Ülke Seçin:")
        country_label_admin.grid(row=0, column=0)
        countries = list(country_info.keys())
        country_var.set(countries[0])
        country_dropdown_admin = tk.OptionMenu(edit_frame, country_var, *countries)
        country_dropdown_admin.grid(row=0, column=1)

        info_label_admin = tk.Label(edit_frame, text="Yeni Bilgi:")
        info_label_admin.grid(row=1, column=0)
        info_entry = tk.Entry(edit_frame)
        info_entry.grid(row=1, column=1)

        update_button = tk.Button(edit_frame, text="Bilgiyi Güncelle", command=update_info)
        update_button.grid(row=2, column=0, columnspan=2)

    else:
        messagebox.showerror("Hata", "Yanlış kullanıcı adı veya şifre!")

root = tk.Tk()
root.title("Küresel Isınma ve Ülkeler")
root.geometry("400x300") 

login_frame = tk.Frame(root, padx=20, pady=20)
login_frame.pack()

username_label = tk.Label(login_frame, text="Kullanıcı Adı:")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(login_frame, text="Şifre:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Giriş", command=check_password)
login_button.grid(row=2, column=0, columnspan=2)

country_frame = tk.Frame(root, padx=20, pady=20)
country_frame.pack()

country_label = tk.Label(country_frame, text="Ülke Seçin:")
country_label.grid(row=0, column=0)
countries = list(country_info.keys())
country_var = tk.StringVar(root)
country_var.set(countries[0])
country_dropdown = tk.OptionMenu(country_frame, country_var, *countries)
country_dropdown.grid(row=0, column=1)

info_button = tk.Button(country_frame, text="Bilgi Göster", command=show_info)
info_button.grid(row=1, column=0, columnspan=2)

root.mainloop()

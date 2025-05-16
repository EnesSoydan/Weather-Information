import tkinter as tk
from tkinter import messagebox
import requests
import os

API_KEY = os.getenv("API_KEY")

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Uyarı", "Lütfen bir şehir adı girin.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"]
            weather = data["weather"][0]["description"]

            result_text.set(f"{city.title()} için hava durumu:\n\n🌡️ Sıcaklık: {temperature}°C\n🌤️ Durum: {weather.capitalize()}")
        else:
            result_text.set("")
            messagebox.showerror("Hata", f"{city} şehri bulunamadı veya API anahtarınız geçersiz.")
    except requests.exceptions.RequestException:
        result_text.set("")
        messagebox.showerror("Bağlantı Hatası", "Verilere erişilemedi. Lütfen internet bağlantınızı kontrol edin.")

# Ana pencere
root = tk.Tk()
root.title("Hava Durumu Uygulaması")
root.geometry("500x300")
root.configure(bg="#f0f2f5")
root.resizable(False, False)

# Başlık
title_label = tk.Label(root, text="🌍 Hava Durumu Öğren", font=("Segoe UI", 18, "bold"), bg="#f0f2f5", fg="#333")
title_label.pack(pady=15)

# Giriş alanı
input_frame = tk.Frame(root, bg="#f0f2f5")
input_frame.pack(pady=5)

city_entry = tk.Entry(input_frame, font=("Segoe UI", 12), width=30, bd=1, relief="solid")
city_entry.grid(row=0, column=0, padx=10)

search_button = tk.Button(input_frame, text="Sorgula", font=("Segoe UI", 12, "bold"), bg="#4caf50", fg="white",
                          activebackground="#45a049", cursor="hand2", padx=10, command=get_weather)
search_button.grid(row=0, column=1)

# Sonuç alanı
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Segoe UI", 13), bg="#f0f2f5", fg="#222", justify="left")
result_label.pack(pady=20)

root.mainloop()

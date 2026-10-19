import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  
root.geometry("450x600") 
root.configure(bg="#f0f4f8")

# --- 1. LABEL JUDUL ---
label_judul = tk.Label(
    root, 
    text="Aplikasi Prediksi Prodi Pilihan", 
    font=("Arial", 14, "bold"), 
    bg="#f0f4f8", 
    fg="#333333"
)
label_judul.pack(pady=15)

# --- 2. 10 INPUT NILAI MATA PELAJARAN ---
frame_input = tk.Frame(root, bg="#f0f4f8")
frame_input.pack(pady=5)

entries = []

for i in range(1, 11):
    lbl = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i}:", font=("Arial", 10), bg="#f0f4f8", anchor="w")
    lbl.grid(row=i-1, column=0, sticky="w", padx=10, pady=4)
    
    entry = tk.Entry(frame_input, width=15, font=("Arial", 10))
    entry.grid(row=i-1, column=1, padx=10, pady=4)
    entries.append(entry)

# --- FUNGSI HASIL PREDIKSI ---
def hitung_prediksi():
    label_hasil.config(text="Prediksi Prodi: Teknologi Informasi", fg="green")

# --- 3. BUTTON BERTULISKAN HASIL PREDIKSI ---
btn_prediksi = tk.Button(
    root, 
    text="Hasil Prediksi", 
    font=("Arial", 11, "bold"), 
    bg="#4CAF50", 
    fg="white", 
    padx=10, 
    pady=5,
    command=hitung_prediksi
)
btn_prediksi.pack(pady=15)

# --- 4. LABEL LUARAN HASIL PREDIKSI ---
label_hasil = tk.Label(
    root, 
    text="Prediksi Prodi: -", 
    font=("Arial", 12, "bold"), 
    bg="#f0f4f8", 
    fg="#333333"
)
label_hasil.pack(pady=10)

# Menjalankan aplikasi GUI
root.mainloop()
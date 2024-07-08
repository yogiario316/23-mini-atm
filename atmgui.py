import tkinter as tk
from tkinter import messagebox
import getpass

# Inisialisasi Tkinter
root = tk.Tk()
root.title("Ario ATM")

# Data Dummy PIN dan Saldo
PIN_ATM = None  # Awalnya None, akan diubah setelah login berhasil
saldo = 0

# Fungsi-fungsi yang telah diperbarui
def lihat_saldo():
    messagebox.showinfo("Saldo Anda", f"Sisa saldo anda adalah Rp. {saldo:.2f}")

def deposit():
    global saldo
    try:
        isi = float(entry_deposit.get())
        if isi < 0:
            raise ValueError("Jumlah tidak boleh negatif")
        saldo += isi
        messagebox.showinfo("Deposit Berhasil", f"Deposit sebesar Rp. {isi:.2f} berhasil ditambahkan.")
    except ValueError as e:
        messagebox.showerror("Error", f"Maaf, {e}")

def tarik():
    global saldo
    try:
        isi = float(entry_tarik.get())
        if isi > saldo:
            raise ValueError("Saldo tidak cukup")
        elif isi < 0:
            raise ValueError("Jumlah tidak boleh negatif")
        saldo -= isi
        messagebox.showinfo("Tarik Tunai Berhasil", f"Tarik tunai sebesar Rp. {isi:.2f} berhasil dilakukan.")
    except ValueError as e:
        messagebox.showerror("Error", f"Maaf, {e}")

def process_login(event=None):  # Tambahkan event=None untuk handle event <Return>
    entered_pin = entry_pin.get()
    if len(entered_pin) == 6 and entered_pin.isdigit():
        global PIN_ATM
        PIN_ATM = entered_pin
        # PIN benar, tampilkan elemen-elemen antarmuka ATM
        label_welcome.pack()
        button_lihat_saldo.pack()
        label_deposit.pack()
        entry_deposit.pack()
        button_deposit.pack()
        label_tarik.pack()
        entry_tarik.pack()
        button_tarik.pack()
        button_keluar.pack()  # Tambahkan tombol keluar
        button_login.pack_forget()
        entry_pin.pack_forget()
        label_pin.pack_forget()
    else:
        messagebox.showerror("Login Gagal", "PIN harus berupa 6 digit angka. Silakan coba lagi.")

# Fungsi handler untuk event <Return>
def handle_enter(event):
    process_login()

# Membuat GUI Utama
label_pin = tk.Label(root, text="Masukkan (6 Digit) Pin anda:")
label_pin.pack()
entry_pin = tk.Entry(root, show='*')
entry_pin.pack()

# Mengaitkan event <Return> ke fungsi handle_enter
entry_pin.bind("<Return>", handle_enter)

button_login = tk.Button(root, text="Login", command=process_login)
button_login.pack()

label_welcome = tk.Label(root, text="Selamat datang di Ario ATM", font=("Helvetica", 16, "bold"))
button_lihat_saldo = tk.Button(root, text="Lihat Saldo", command=lihat_saldo)

label_deposit = tk.Label(root, text="Masukkan Jumlah yang akan ditabung:")
entry_deposit = tk.Entry(root)
button_deposit = tk.Button(root, text="Deposit", command=deposit)

label_tarik = tk.Label(root, text="Masukkan Jumlah yang ingin anda tarik:")
entry_tarik = tk.Entry(root)
button_tarik = tk.Button(root, text="Tarik Tunai", command=tarik)

# Tombol Keluar
button_keluar = tk.Button(root, text="Keluar", command=root.quit)

# Loop Tkinter utama
root.mainloop()

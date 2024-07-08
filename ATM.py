import getpass
import time
import sys

nama = ["Yogi Ario", "2313020004", "Projek Mini ATM"]

def type_writer(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # Move to the next line after typing is done

def lihat_saldo(saldo):
    type_writer(" ")
    type_writer("#################################")
    type_writer(f"Sisa saldo anda adalah Rp. {saldo:.2f}")
    type_writer("#################################")
    type_writer(" ")
    

def deposit():
    type_writer(" ")
    type_writer("#################################")
    try:
        isi = float(input("Masukkan Jumlah yang akan ditabung: "))
        if isi < 0:
            raise ValueError("Jumlah tidak boleh negatif")
    except ValueError as e:
        type_writer("#################################")
        type_writer(f"Maaf, {e}")
        type_writer("#################################")
        type_writer(" ")
        return 0
    else:
        type_writer("#################################")
        return isi
    
def tarik(saldo):
    type_writer(" ")
    type_writer("#################################")
    try:
        isi = float(input("Masukkan Jumlah yang ingin anda tarik: "))
        if isi > saldo:
            raise ValueError("Saldo tidak cukup")
        elif isi < 0:
            raise ValueError("Jumlah tidak boleh negatif")
    except ValueError as e:
        type_writer(" ")
        type_writer("#################################")
        type_writer(f"Maaf, {e}")
        type_writer("#################################")
        type_writer(" ")
        return 0
    else:
        type_writer("#################################")
        return isi
    
def login():
    while True:
        input_pin = getpass.getpass("Masukkan (6 Digit) Pin anda: ")
        if len(input_pin) == 6 and input_pin.isdigit():
            return True
        else:
            type_writer("#################################")
            type_writer("PIN Salah")
            type_writer("#################################")
            type_writer(" ")
    
def main():
    if not login():
        return
    saldo = 0
    is_running = True

    while is_running:
        type_writer(" ")
        type_writer("#################################")
        type_writer("     Selamat datang di Ario ATM")
        type_writer("#################################")
        type_writer("1. Lihat Saldo")
        type_writer("2. Deposit")
        type_writer("3. Tarik Tunai")
        type_writer("4. Keluar")
        type_writer("#################################")
        choice = input("Masukkan Pilihan anda (1-4): ")
        type_writer(" ")

        if choice == '1':
            lihat_saldo(saldo)
        elif choice == '2':
            saldo += deposit()
        elif choice == '3':
            saldo -= tarik(saldo)
        elif choice == '4':
            is_running = False
        else:
            type_writer("#################################")
            type_writer("Maaf Nomor yang anda masukkan salah")
            type_writer("#################################")
            type_writer(" ")

        type_writer("#################################")
        type_writer("Terimakasih telah menggunakan Jasa Kami")
        type_writer("#################################")

if __name__ == '__main__':
    main()

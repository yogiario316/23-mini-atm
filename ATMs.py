import getpass

nama = ["Yogi Ario", "2313020004", "Projek Mini ATM"]

def lihat_saldo(saldo):
    print(" ")
    print("#################################")
    print(f"Sisa saldo anda adalah Rp. {saldo:.2f}")
    print("#################################")
    print(" ")
    

def deposit():
    print(" ")
    print("#################################")
    try:
        isi = float(input("Masukkan Jumlah yang akan ditabung: "))
        if isi < 0:
            raise ValueError("Jumlah tidak boleh negatif")
    except ValueError as e:
        print("#################################")
        print(f"Maaf, {e}")
        print("#################################")
        print(" ")
        return 0
    else:
        print("#################################")
        return isi
    
def tarik(saldo):
    print(" ")
    print("#################################")
    try:
        isi = float(input("Masukkan Jumlah yang ingin anda tarik: "))
        if isi > saldo:
            raise ValueError("Saldo tidak cukup")
        elif isi < 0:
            raise ValueError("Jumlah tidak boleh negatif")
    except ValueError as e:
        print(" ")
        print("#################################")
        print(f"Maaf, {e}")
        print("#################################")
        print(" ")
        return 0
    else:
        print("#################################")
        return isi
    
def login():
    while True:
        input_pin = getpass.getpass("Masukkan (6 Digit) Pin anda: ")
        if len(input_pin) == 6 and input_pin.isdigit():
            return True
        else:
            print("#################################")
            print("PIN Salah")
            print("#################################")
            print(" ")
    
def main():
    if not login():
        return
    saldo = 0
    is_running = True

    while is_running:
        print(" ")
        print("#################################")
        print("     Selamat datang di Ario ATM")
        print("#################################")
        print("1. Lihat Saldo")
        print("2. Deposit")
        print("3. Tarik Tunai")
        print("4. Keluar")
        print("#################################")
        choice = input("Masukkan Pilihan anda (1-4): ")
        print(" ")

        if choice == '1':
            lihat_saldo(saldo)
        elif choice == '2':
            saldo += deposit()
        elif choice == '3':
            saldo -= tarik(saldo)
        elif choice == '4':
            is_running = False
        else:
            print("#################################")
            print("Maaf Nomor yang anda masukkan salah")
            print("#################################")
            print(" ")

        print("#################################")
        print("Terimakasih telah menggunakan Jasa Kami")
        print("#################################")

if __name__ == '__main__':
    main()

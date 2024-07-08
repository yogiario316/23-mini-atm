nama = ["Yogi Ario", "2313020004", "Projek Mini ATM"]

def lihat_saldo(saldo):
    print("#################################")
    print(f"Sisa saldo anda adalah Rp. {saldo:.2f}")
    print("#################################")

def deposit():
    print("#################################")
    isi = float(input("Masukkan Jumlah yang akan ditabung: "))
    print("#################################")
    if isi < 0:
        print("#################################")
        print("Maaf Jumlah yang anda masukkan salah")
        print("#################################")
        return 0
    else:
        return isi
    
def tarik(saldo):
    print("#################################")
    isi = float(input("Masukkan Jumlah yang ingin anda tarik: "))
    print("#################################")

    if  isi > saldo:
        print("#################################")
        print("Maaf Saldo anda tidak cukup")
        print("#################################")
        return 0
    elif isi < 0:
        print("#################################")
        print("Maaf Masukkan jumlah yang benar")
        print("#################################")
        return 0
    else:
        return isi
    
def main():
    saldo = 0
    is_running = True

    while is_running:
        print("#################################")
        print("     Selamat datang di Ario ATM")
        print("#################################")
        print("1. Lihat Saldo")
        print("2. Deposit")
        print("3. Tarik Tunai")
        print("4. Keluar")
        print("#################################")
        choice = input("Masukkan Pilihan anda (1-4)")

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

print("#################################")
print("Terimakasih telah menggunakan Jasa Kami")
print("#################################")

if __name__ == '__main__':
    main()
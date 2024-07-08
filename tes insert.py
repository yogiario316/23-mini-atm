def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        b = i - 1
        while b >= 0 and key < arr[b]:
            arr[b + 1] = arr[b]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [24, 9, 29, 14, 19, 27]
print("Array sebelum diurutkan:", arr)  # Menampilkan array sebelum disortir
sortir_arr = insertionSort(arr.copy())  # Menggunakan salinan array untuk diurutkan
print("Array yang telah diurutkan:", sortir_arr)  # Menampilkan array setelah disortir

default_list = [32, 14, 16, 13, 13, 115, 1, 9]

def insertion_sort(input_list):
    # Listenin her elemanını sırayla kontrol et
    for i in range(1, len(input_list)):
        key = input_list[i]  # Sıradaki eleman
        j = i - 1
        
        # Anahtar eleman yerine yerleşene kadar sola kaydır
        while j >= 0 and key < input_list[j]:
            input_list[j + 1] = input_list[j]
            j -= 1
        
        input_list[j + 1] = key

# Fonksiyonu çağır ve listeyi sıralar
insertion_sort(default_list)
print(default_list)

default_list = [32, 14, 16, 13, 13, 115, 1, 9]

def merge_sort(arr):
    if len(arr) > 1:
        # Diziyi ortadan ikiye ayır
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Sol ve sağ yarıları ayrı ayrı sırala
        print(left_half, right_half)
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge işlemi
        i = j = k = 0

        # İki yarıyı birleştir
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Kalan elemanları ekle (sol yarıdan)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Kalan elemanları ekle (sağ yarıdan)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1



# Fonksiyonu çağır ve listeyi sıralar
merge_sort(default_list)
print(default_list)

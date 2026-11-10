def greedy(target, pecahan):
    hasil = {}
    for koin in sorted(pecahan, reverse=True):
        jumlah, target = divmod(target, koin)
        if jumlah:
            hasil[koin] = jumlah
    return hasil, target

pecahan = [20, 10, 5, 2, 1]
hasil, sisa = greedy(18, pecahan)
print(hasil)
print("Total:", sum(hasil.values()), "Sisa:", sisa)
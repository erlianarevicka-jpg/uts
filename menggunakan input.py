def greedy(target, pecahan):
    hasil = {}
    for koin in sorted(pecahan, reverse=True):
        jumlah, target = divmod(target, koin)
        if jumlah:
            hasil[koin] = jumlah
    return hasil, target


def main():
    # Input target
    try:
        target = int(input("Masukkan target nilai: "))
        if target < 0:
            print("Target tidak boleh negatif.")
            return
    except ValueError:
        print("Input target harus berupa angka bulat.")
        return

    # Input pecahan (dipisah spasi), kosongkan untuk memakai default
    teks = input("Masukkan pecahan dipisah spasi (kosongkan untuk default 20 10 5 2 1): ").strip()
    if teks:
        try:
            pecahan = [int(x) for x in teks.split()]
            if any(p <= 0 for p in pecahan):
                print("Pecahan harus bernilai positif.")
                return
        except ValueError:
            print("Pecahan harus berupa angka bulat dipisah spasi.")
            return
    else:
        pecahan = [20, 10, 5, 2, 1]

    hasil, sisa = greedy(target, pecahan)

    print("\nHasil:", hasil)
    print("Total koin:", sum(hasil.values()), "| Sisa:", sisa)


if __name__ == "__main__":
    main()
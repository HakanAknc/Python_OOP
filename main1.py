from kitap import Kitap
from kutuphane import Kutuphane

def main():
    kutuphane = Kutuphane()

    kitap1 = Kitap("1984", "George Orwell", 1949, "1234567890")
    kitap2 = Kitap("To Kill a Mockingbird", "Harper Lee", 1960, "0987654321")

    kutuphane.kitap_ekle(kitap1)
    kutuphane.kitap_ekle(kitap2)

    print("\nKütüphanedeki kitaplar:")
    kutuphane.kitaplari_listele()

    aranan_kitap = kutuphane.kitap_bul("1984")
    if aranan_kitap:
        print(f"\nAranan kitap bulundu: {aranan_kitap.kitap_bilgisi()}")
    else:
        print("\nAranan kitap bulunamadı.")

if __name__ == "__main__":
    main()
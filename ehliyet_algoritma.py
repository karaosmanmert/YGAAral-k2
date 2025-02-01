import os  #gerekli modulu import et

def ehliyet_kontrol(yas):
    """
    Bu fonksiyon, kullanicinin yasina gore ehliyet alip alamayacagini belirler.

    Args:
        yas (int): Kullanicinin yasi.

    Returns:
        str: Kullanicinin ehliyet durumu hakkinda bir mesaj.
    """
    if yas >= 18:
        return "Ehliyet alabilir."
    else:
        return "Ehliyet alamaz."

def dosyaya_yaz(yas, metin):
    """
    Bu fonksiyon, verilen metni belirtilen dosyaya yazar.

    Args:
        yas (str): Yazilacak dosyanin adi.
        metin (str): Dosyaya yazilacak metin.
    """
    try:
        with open(yas, "w") as dosya:  # Dosyayi yazma modunda aç
            dosya.write(metin)  # Metni dosyaya yaz
        print(f"{yas} dosyasina yazma islemi basarili.")
    except Exception as e:
        print(f"Dosyaya yazma sirasinda bir hata olustu: {e}")

def dosyadan_oku(yas):
    """
    Bu fonksiyon, belirtilen dosyadan metni okur.

    Args:
        yas (str): Okunacak dosyanin adi.

    Returns:
        str: Dosyadan okunan metin.
    """
    try:
        with open(yas, "r") as dosya:  # Dosyayi okuma modunda aç
            metin = dosya.read()  # Dosyadaki metni oku
            return metin
    except FileNotFoundError:
        print(f"{yas} dosyasi bulunamadi.")
        return None
    except Exception as e:
        print(f"Dosyadan okuma sirasinda bir hata olustu: {e}")
        return None

if __name__ == "__main__":
    dosya_adi = "C:/Users/mertk/OneDrive/Desktop/YGAAralik2/yas.txt"  # absolute path

    try:
        kullanici_yasi = int(input("Lütfen yasinizi giriniz: "))
        sonuc = ehliyet_kontrol(kullanici_yasi)

        dosyaya_yaz(dosya_adi, f"Kullanicinin yaşi: {kullanici_yasi}, Ehliyet durumu: {sonuc}")

        okunan_metin = dosyadan_oku(dosya_adi)
        if okunan_metin:
            print("Dosyadan okunan metin:")
            print(okunan_metin)

    except ValueError:
        print("Lütfen geçerli bir sayi giriniz.")
        
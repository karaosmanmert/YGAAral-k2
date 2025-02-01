def ehliyet_kontrol(yas):
    if yas >= 18:
        return "Ehliyet alabilir."
    else:
        return "Ehliyet alamaz."

if __name__ == "__main__":
    try:
        kullanici_yasi = int(input("Lütfen yasinizi giriniz: "))
        sonuc = ehliyet_kontrol(kullanici_yasi)
        print(sonuc)
    except ValueError:
        print("Lütfen geçerli bir sayi giriniz.")
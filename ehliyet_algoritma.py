def ehliyet_kontrol(yas):
    """
    Bu fonksiyon, kullanicinin yasina gore ehliyet alip alamayacagini belirler.

    Args:
        yas (int): Kullanicinin yasi.

    Returns:
        str: Kullanicinin ehliyet durumu hakkinda bir mesaj.
    """
    if yas >= 18:   # Yas 18 veya daha buyukse
        return "Ehliyet alabilir."  # Ehliyet alabilir mesajini dondur
    else:
        return "Ehliyet alamaz."    # Ehliyet alamaz mesajini dondur

if __name__ == "__main__":
    try:
        kullanici_yasi = int(input("Lutfen yasinizi giriniz: "))    # Kullanicidan yas bilgisini al
        sonuc = ehliyet_kontrol(kullanici_yasi)     # Kullanicinin yasini fonksiyona gonder ve sonucu al
        print(sonuc)
    except ValueError:      # Kullanici gecerli bir sayi girmemisse
        print("Lutfen gecerli bir sayi giriniz.")
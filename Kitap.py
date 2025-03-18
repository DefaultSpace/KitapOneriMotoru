# Gerekli Kütüphaneler:
# Bu kütüphaneleri kurmak için terminalde şu komutları çalıştırın:
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import random

# Simüle Edilmiş Veri Seti (Project Gutenberg'den alınan örnek kitaplar)
kitaplar = {
    'Bilim Kurgu': [
        {'title': 'The Time Machine', 'author': 'H.G. Wells', 'link': 'https://www.gutenberg.org/ebooks/35'},
        {'title': 'The War of the Worlds', 'author': 'H.G. Wells', 'link': 'https://www.gutenberg.org/ebooks/36'},
        {'title': 'A Journey to the Centre of the Earth', 'author': 'Jules Verne', 'link': 'https://www.gutenberg.org/ebooks/18857'},
        {'title': 'Twenty Thousand Leagues Under the Sea', 'author': 'Jules Verne', 'link': 'https://www.gutenberg.org/ebooks/164'},
        {'title': 'The Invisible Man', 'author': 'H. G. Wells', 'link': 'https://www.gutenberg.org/ebooks/5230'}
    ],
    'Klasik': [
        {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'link': 'https://www.gutenberg.org/ebooks/1342'},
        {'title': 'Moby Dick; Or, The Whale', 'author': 'Herman Melville', 'link': 'https://www.gutenberg.org/ebooks/2701'},
        {'title': 'The Adventures of Sherlock Holmes', 'author': 'Sir Arthur Conan Doyle', 'link': 'https://www.gutenberg.org/ebooks/1661'},
        {'title': 'Jane Eyre', 'author': 'Charlotte Brontë', 'link': 'https://www.gutenberg.org/ebooks/1260'},
        {'title': 'Wuthering Heights', 'author': 'Emily Brontë', 'link': 'https://www.gutenberg.org/ebooks/768'}
    ],
    'Jane Austen': [
        {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'link': 'https://www.gutenberg.org/ebooks/1342'},
        {'title': 'Emma', 'author': 'Jane Austen', 'link': 'https://www.gutenberg.org/ebooks/158'},
        {'title': 'Sense and Sensibility', 'author': 'Jane Austen', 'link': 'https://www.gutenberg.org/ebooks/161'},
        {'title': 'Mansfield Park', 'author': 'Jane Austen', 'link': 'https://www.gutenberg.org/ebooks/141'},
        {'title': 'Northanger Abbey', 'author': 'Jane Austen', 'link': 'https://www.gutenberg.org/ebooks/121'}
    ],
    'H.G. Wells': [
        {'title': 'The Time Machine', 'author': 'H.G. Wells', 'link': 'https://www.gutenberg.org/ebooks/35'},
        {'title': 'The War of the Worlds', 'author': 'H.G. Wells', 'link': 'https://www.gutenberg.org/ebooks/36'},
        {'title': 'The Invisible Man', 'author': 'H. G. Wells', 'link': 'https://www.gutenberg.org/ebooks/5230'},
        {'title': 'The Island of Doctor Moreau', 'author': 'H. G. Wells', 'link': 'https://www.gutenberg.org/ebooks/159'},
        {'title': 'The First Men in the Moon', 'author': 'H. G. Wells', 'link': 'https://www.gutenberg.org/ebooks/1013'}
    ],
    'Science Fiction': [
        {'title': 'The Time Machine', 'author': 'H.G. Wells', 'link': 'https://www.gutenberg.org/ebooks/35'},
        {'title': 'The War of the Worlds', 'author': 'H.G. Wells', 'link': 'https://www.gutenberg.org/ebooks/36'},
        {'title': 'A Journey to the Centre of the Earth', 'author': 'Jules Verne', 'link': 'https://www.gutenberg.org/ebooks/18857'},
        {'title': 'Twenty Thousand Leagues Under the Sea', 'author': 'Jules Verne', 'link': 'https://www.gutenberg.org/ebooks/164'},
        {'title': 'The Invisible Man', 'author': 'H. G. Wells', 'link': 'https://www.gutenberg.org/ebooks/5230'}
    ],
    'Classics': [
        {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'link': 'https://www.gutenberg.org/ebooks/1342'},
        {'title': 'Moby Dick; Or, The Whale', 'author': 'Herman Melville', 'link': 'https://www.gutenberg.org/ebooks/2701'},
        {'title': 'The Adventures of Sherlock Holmes', 'author': 'Sir Arthur Conan Doyle', 'link': 'https://www.gutenberg.org/ebooks/1661'},
        {'title': 'Jane Eyre', 'author': 'Charlotte Brontë', 'link': 'https://www.gutenberg.org/ebooks/1260'},
        {'title': 'Wuthering Heights', 'author': 'Emily Brontë', 'link': 'https://www.gutenberg.org/ebooks/768'}
    ]
}


def veri_cek(kriter):
    """
    Project Gutenberg'den veri çeken fonksiyon (tür veya yazar bazlı).
    Bu versiyonda simüle edilmiş veri seti kullanılmaktadır.
    Args:
        kriter (str): Kitap türü veya yazar adı.
    Returns:
        list: Kitap bilgilerini içeren bir liste.
              Hata durumunda, boş bir liste döndürür.
    """
    print(f"'{kriter}' kriterine göre kitaplar aranıyor...")
    try:
        # İngilizce girdileri de desteklemek için lowercase'e çevir
        if kriter.lower() == "bilim kurgu" or kriter.lower() == "science fiction":
          kriter = 'Bilim Kurgu'
        elif kriter.lower() == "klasik" or kriter.lower() == "classics":
          kriter = 'Klasik'
        if kriter in kitaplar:
            return kitaplar[kriter]
        else:
            print(f"'{kriter}' için veri bulunamadı.")
            return []
    except Exception as e:
        print(f"Veri alınırken bir hata oluştu: {e}")
        return []


def oneriler_olustur(veriler):
    """
    Çekilen verilerden 3 öneri seçen fonksiyon.
    Args:
        veriler (list): Kitap bilgilerini içeren bir liste.
    Returns:
        list: Seçilen 3 kitap önerisini içeren bir liste.
    """
    if not veriler:
        return []
    return random.sample(veriler, min(3, len(veriler)))


def sonuc_goster(kriter, oneriler):
    """
    Sonuçları formatlı bir şekilde gösteren fonksiyon.
    Args:
        kriter (str): Kullanıcının seçtiği kriter (tür veya yazar).
        oneriler (list): Kitap önerilerini içeren bir liste.
    """
    print(f"\n{kriter} için Öneriler:")
    if not oneriler:
        print("Öneri bulunamadı.")
        return
    for i, kitap in enumerate(oneriler):
        print(f"{i + 1}. Kitap: '{kitap['title']}' - {kitap['author']}")
        print(f"   İndir: {kitap['link']}")


def main():
    """
    Programın ana akışını yöneten fonksiyon.
    """
    while True:
        # Kullanıcıya tür mü yoksa yazar mı seçmek istediğini Türkçe olarak sor.
        secim_tipi = input("Kitapları türe göre mi yoksa yazara göre mi aramak istersiniz? (tür/yazar): ").lower()

        # Geçersiz bir seçim yapılmışsa uyarı gönder.
        while secim_tipi not in ["tür", "yazar"]:
            print("Geçersiz seçim. Lütfen 'tür' veya 'yazar' seçiniz.")
            secim_tipi = input("Kitapları türe göre mi yoksa yazara göre mi aramak istersiniz? (tür/yazar): ").lower()

        if secim_tipi == "tür":
            kriter = input("Bir kitap türü giriniz (örn., Bilim Kurgu, Klasik): ")
        else:
            kriter = input("Bir yazar adı giriniz (örn., Jane Austen, H.G. Wells): ")

        # Kriter boşsa veya sayısal değer içeriyorsa hata mesajı gönder.
        if not kriter.strip() or any(char.isdigit() for char in kriter):
            print("Geçersiz giriş. Lütfen geçerli bir ad veya tür giriniz (yalnızca alfabetik karakterler).")
            continue

        veriler = veri_cek(kriter)
        oneriler = oneriler_olustur(veriler)
        sonuc_goster(kriter, oneriler)

        devam = input("Başka bir öneri almak ister misiniz? (e/h): ")
        if devam.lower() != 'e':
            break


if __name__ == "__main__":
    main()

import random
import string

# Şifre oluşturma fonksiyonu
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    # string.ascii_letters: Küçük ve büyük harfler (a-z, A-Z).
    # string.digits: Sayılar (0-9).
    # string.punctuation: Semboller (!@#$%^&* gibi).
    
    # Rastgele bir şifre oluştur.
    password = ''.join(random.choice(characters) for _ in range(length))
    # random.choice(characters): Karakter havuzundan rastgele bir seçim yapar.
    # for _ in range(length): Belirtilen uzunluk kadar bu işlemi tekrarlar.
    # ''.join(...): Seçilen karakterleri birleştirerek şifreyi oluşturur.
    return password

# Kullanıcıdan şifre uzunluğunu al
try:
    length = int(input("Şifre uzunluğunu girin: "))
    if length < 6:
        print("Şifre en az 6 karakter uzunluğunda olmalı.")
    else:
        print("Oluşturulan şifre:", generate_password(length))
except ValueError:
    print("Lütfen geçerli bir sayı girin.")

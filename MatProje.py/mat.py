import math  # Karekök işlemi için matematik kütüphanesini ekliyoruz

def kok_bul():
    print("--- İkinci Dereceden Denklem Kök Bulucu ---")
    print("Lütfen ax^2 + bx + c = 0 denklemi için katsayıları giriniz.")

    # 1. Adım: Kullanıcıdan a, b, c değerlerini al
    try:
        a = float(input("a değerini giriniz: "))
        b = float(input("b değerini giriniz: "))
        c = float(input("c değerini giriniz: "))
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")
        return

    # a 0 olursa denklem 2. dereceden olmaz, basit bir kontrol ekleyelim
    if a == 0:
        print("a değeri 0 olamaz. Bu durumda denklem 1. dereceden olur.")
        return

    # 2. Adım: Diskriminantı hesapla
    delta = (b ** 2) - (4 * a * c)
    print(f"\nDiskriminant (Delta) Değeri: {delta}")

    # 3. Adım: Koşulları kontrol et ve kökleri bul
    if delta > 0:
        # İki farklı gerçek kök var
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Sonuç: Denklemin iki farklı gerçek kökü vardır.")
        print(f"Kök 1 (x1): {x1}")
        print(f"Kök 2 (x2): {x2}")

    elif delta == 0:
        # Tek bir gerçek kök var (Çakışık kök)
        x = -b / (2 * a)
        print("Sonuç: Denklemin çakışık tek bir gerçek kökü vardır.")
        print(f"Kök (x): {x}")

    else:
        # Delta < 0 durumu
        print("Sonuç: Delta 0'dan küçüktür. Denklemin gerçek kökü yoktur.")
        print("(Karmaşık/Sanal kökler mevcuttur ancak bu program kapsamında hesaplanmamıştır.)")

# Programı çalıştır
kok_bul()
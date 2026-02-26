import math

def bisection_method(f_str, a, b, tol, max_iter=100):
    # Kullanıcının girdiği metni matematiksel bir fonksiyona çeviriyoruz
    def f(x):
        # Güvenli bir şekilde string ifadeyi çalıştırıp 'x' yerine değer koyar
        return eval(f_str, {"math": math}, {"x": x})
    
    # 1. Adım: Ara Değer Teoremi kontrolü (Bölüm 3.1)
    if f(a) * f(b) >= 0:
        print("\nHATA: f(a) ve f(b) zıt işaretli değil. Kök bu aralıkta olmayabilir veya aralık yanlış seçilmiş.")
        return None

    print("\n--- İterasyon Adımları ---")
    # İterasyon süreci
    for i in range(1, max_iter + 1):
        # 2. Adım: Aralığın orta noktasını hesapla
        c = (a + b) / 2.0
        
        print(f"Adım {i}: Aralığımız [{a:.4f}, {b:.4f}], Orta Nokta (c) = {c:.4f}")
        
        # 3. Adım: Durma Kriterlerini Kontrol Et (Bölüm 3.7)
        if abs(b - a) < tol or f(c) == 0:
            print(f"\nKök başarıyla bulundu! ({i}. adımda sonlandı)")
            return c
        
        # 4. Adım: Yeni aralığı belirle ve daralt (Bölüm 3.2)
        if f(a) * f(c) < 0:
            b = c  # Kök sol yarıda
        else:
            a = c  # Kök sağ yarıda
            
    print("\nMaksimum iterasyona ulaşıldı ancak hedeflenen toleransa inilemedi.")
    return (a + b) / 2.0

# --- KULLANICIDAN GİRDİ ALMA KISMI ---
print("=== Bisection (İkiye Bölme) Yöntemi Hesaplayıcı ===")
print("Lütfen fonksiyonu 'x' değişkenine bağlı olarak yazın.")
print("Önemli Not: Üs alma işlemi için '^' yerine '**' kullanmalısınız (Örn: x**3 - x - 2)")

# Kullanıcıdan değerleri istiyoruz
fonksiyon_girdisi = input("f(x) denklemini girin: ")
baslangic_a = float(input("Arama aralığının alt sınırını (a) girin: "))
baslangic_b = float(input("Arama aralığının üst sınırını (b) girin: "))
tolerans = float(input("Hedeflenen hata toleransını girin (Örn: 0.001): "))

# Fonksiyonu çalıştırıyoruz
kok = bisection_method(fonksiyon_girdisi, baslangic_a, baslangic_b, tolerans)

if kok is not None:
    print(f"==> Hesaplanan Yaklaşık Kök: {kok:.5f}")

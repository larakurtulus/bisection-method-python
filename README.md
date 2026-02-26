# Bisection Method Calculator 🧮

Mühendislikte karşılaşılan doğrusal olmayan (nonlinear) denklemlerin köklerini bulmak için geliştirilmiş, etkileşimli bir Python uygulaması. Kök bulma işlemlerinde en güvenilir yöntemlerden biri olan **İkiye Bölme (Bisection)** algoritmasını kullanır.

## Özellikler (Features)
* **Etkileşimli Kullanım:** Kullanıcıdan fonksiyonu, aralığı ve toleransı çalışma anında dinamik olarak alır.
* **Adım Adım İzleme:** Her iterasyonda aralığın nasıl daraldığını adım adım konsola yazdırır.
* **Güvenlik Kontrolü:** Ara Değer Teoremi'ni (Intermediate Value Theorem) test ederek başlangıç aralığının doğruluğunu en başta denetler.

## Nasıl Kullanılır? (Usage)
Kod çalıştırıldığında konsol sizden sırasıyla şu değerleri isteyecektir:
1. `f(x)` denklemi (Örn: `x**3 - x - 2` *Not: Üs alma işlemi için `**` kullanılmalıdır.*)
2. Alt ve üst aralık sınırları (Örn: `a = 1`, `b = 2`)
3. Hata toleransı (Örn: `0.001`)

## Örnek Çıktı (Example Output)
```text
=== Bisection (İkiye Bölme) Yöntemi Hesaplayıcı ===
Lütfen fonksiyonu 'x' değişkenine bağlı olarak yazın.
f(x) denklemini girin: x**3 - x - 2
Arama aralığının alt sınırını (a) girin: 1
Arama aralığının üst sınırını (b) girin: 2
Hedeflenen hata toleransını girin (Örn: 0.001): 0.001

--- İterasyon Adımları ---
Adım 1: Aralığımız [1.0000, 2.0000], Orta Nokta (c) = 1.5000
Adım 2: Aralığımız [1.5000, 2.0000], Orta Nokta (c) = 1.7500
...
Kök başarıyla bulundu! (10. adımda sonlandı)
==> Hesaplanan Yaklaşık Kök: 1.52148

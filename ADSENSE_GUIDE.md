# Google AdSense Entegrasyon Rehberi

## 🎯 Tamamlanan Hazırlıklar

Bu proje Google AdSense için hazır hale getirilmiştir. Aşağıdaki özellikler eklenmiştir:

### ✅ 1. Gizlilik Politikası (Privacy Policy)
- **URL**: `/gizlilik-politikasi`
- **Dosya**: `templates/privacy.html`
- Kapsamlı KVKK ve GDPR uyumlu gizlilik politikası
- Google AdSense, Analytics ve çerez kullanımı açıklamaları
- Footer'da link mevcut

### ✅ 2. ads.txt Dosyası
- **URL**: `/ads.txt`
- **Dosya**: `static/ads.txt`
- Reklam dolandırıcılığını önlemek için IAB standardı
- Publisher ID'nizi eklemeniz gerekiyor

### ✅ 3. robots.txt
- **URL**: `/robots.txt`
- **Dosya**: `static/robots.txt`
- Arama motorları için optimize edilmiş
- Sitemap referansı dahil

### ✅ 4. Dinamik Sitemap
- **URL**: `/sitemap.xml`
- Otomatik olarak tüm sayfaları içerir
- Güncel haber listesi
- Kategoriler ve statik sayfalar

### ✅ 5. Meta Tags & SEO
- Open Graph tags (Facebook)
- Twitter Card tags
- Canonical URLs
- Schema.org structured data hazır

### ✅ 6. Cookie Consent Banner
- GDPR/KVKK uyumlu çerez bildirimi
- Kabul/Reddet seçenekleri
- Gizlilik politikasına link

### ✅ 7. Reklam Alanları
- Ana sayfa: Top ve bottom banner (728x90)
- Makale sayfası: In-article ve sidebar reklamlar
- Hazır placeholder'lar mevcut

## 📋 AdSense Başvuru Adımları

### 1. Ön Gereksinimler
Başvuru yapmadan önce kontrol edin:

- ✅ Site en az 6 aydır yayında (tavsiye edilen)
- ✅ En az 20-30 özgün makale var
- ✅ Düzenli içerik güncellemesi yapılıyor
- ✅ Kaliteli, özgün içerik (AI ile yeniden yazıldı ✓)
- ✅ Kullanıcı dostu navigasyon
- ✅ Gizlilik politikası mevcut
- ✅ İletişim bilgileri açık
- ✅ Mobil uyumlu tasarım

### 2. Google AdSense Hesabı Oluşturma

1. **AdSense'e Kaydolun**
   - https://www.google.com/adsense/ adresine gidin
   - "Başlayın" butonuna tıklayın
   - Google hesabınızla giriş yapın

2. **Site Bilgilerini Girin**
   ```
   Web sitesi URL: https://your-domain.com
   Dil: Türkçe
   Ülke: Türkiye
   ```

3. **İletişim Bilgileri**
   - Ad, soyad
   - Adres bilgileri
   - Telefon numarası

4. **Ödeme Bilgileri**
   - Banka hesap bilgileri
   - Vergi kimlik numarası

### 3. Site Doğrulama

AdSense size bir doğrulama kodu verecek:

```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX"
     crossorigin="anonymous"></script>
```

Bu kodu `templates/base.html` dosyasına ekleyin:

```html
<!-- Google AdSense -->
<meta name="google-adsense-account" content="ca-pub-XXXXXXXXXXXXXXXX">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX"
     crossorigin="anonymous"></script>
```

### 4. ads.txt Güncelleme

AdSense hesabınızdan Publisher ID'nizi alın ve `static/ads.txt` dosyasını güncelleyin:

```
google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0
```

### 5. Onay Süreci

- **Süre**: 1-4 hafta (genellikle 1-2 hafta)
- **Durum Kontrolü**: AdSense hesabınızdan takip edebilirsiniz
- **İnceleme**: Google otomatik ve manuel inceleme yapar

### 6. Onaylandıktan Sonra

Onay aldıktan sonra reklam yerleşimi:

#### Ana Sayfa (index.html)
```html
<!-- Top Banner - 728x90 veya Responsive -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
     data-ad-slot="YYYYYYYYYY"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
```

#### Makale Sayfası (article.html)
```html
<!-- In-Article Ad -->
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
     data-ad-slot="YYYYYYYYYY"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
```

## 🚨 Önemli Notlar

### AdSense Politikaları

**Yapılması Gerekenler:**
- ✅ Özgün, kaliteli içerik üretin
- ✅ Düzenli güncellemeler yapın
- ✅ Kullanıcı deneyimini önceliklendirin
- ✅ Telif haklarına saygı gösterin
- ✅ Gizlilik politikasını güncel tutun

**Yapılmaması Gerekenler:**
- ❌ Kendi reklamlarınıza tıklamayın
- ❌ Başkalarını tıklamaya teşvik etmeyin
- ❌ Tıklama botu kullanmayın
- ❌ Kopyala-yapıştır içerik kullanmayın
- ❌ Yasadışı içerik paylaşmayın
- ❌ Yetişkin içerik (18+) eklemeyın
- ❌ Aşırı reklam yerleştirmeyin

### Optimizasyon İpuçları

1. **Reklam Yerleşimi**
   - Her sayfada 3-4 reklam yeterli
   - İçeriğin üstünde ve ortasında en etkili
   - Sidebar'da çok fazla reklam koymayın

2. **Reklam Boyutları**
   - Responsive reklamlar mobil için ideal
   - 336x280 (Large Rectangle) - Yüksek performans
   - 728x90 (Leaderboard) - Header/Footer için
   - 300x600 (Half Page) - Sidebar için

3. **İçerik Stratejisi**
   - Günde 2-3 yeni haber
   - SEO odaklı başlıklar
   - En az 500 kelimelik içerikler
   - Görseller mutlaka ekleyin

4. **Trafik Artırma**
   - Sosyal medya paylaşımları
   - Google Search Console kullanın
   - Backlink stratejisi
   - E-posta bülteni

## 📊 Beklenen Gelir

Gelir faktörleri:
- **Trafik**: Günlük ziyaretçi sayısı
- **Niche**: Haber siteleri orta gelir kategorisinde
- **Coğrafya**: Türkiye CPC'si düşük (ancak Avrupa ziyaretçileri yüksek)
- **Sezon**: Ocak-Şubat, Ekim-Aralık daha yüksek

Tahmini kazanç (Türkiye):
- 1.000 görüntüleme = $0.5-2 (RPM: $0.5-2)
- 10.000 görüntüleme = $5-20
- 100.000 görüntüleme = $50-200

**Not**: Bunlar tahminlerdir. Gerçek kazançlar niche, içerik kalitesi ve trafik kaynağına göre değişir.

## 🔗 Yararlı Linkler

- [Google AdSense Yardım](https://support.google.com/adsense)
- [AdSense Program Politikaları](https://support.google.com/adsense/answer/48182)
- [ads.txt Kılavuzu](https://support.google.com/adsense/answer/7532444)
- [KVKK Resmi Sitesi](https://kvkk.gov.tr/)
- [Google Search Console](https://search.google.com/search-console)

## 💡 Ekstra Öneriler

### 1. Google Analytics Ekleyin
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### 2. Google Search Console
- Site ownership doğrulayın
- Sitemap gönderin (`/sitemap.xml`)
- Index durumunu takip edin

### 3. Sayfa Hızı Optimizasyonu
- Görselleri optimize edin
- CDN kullanın
- Lazy loading ekleyin
- Caching stratejisi

### 4. Mobil Optimizasyon
- Responsive tasarım ✓ (zaten var)
- AMP sayfaları (opsiyonel)
- Mobil öncelikli yaklaşım

## 📝 Checklist

Son kontrol listesi:

- [ ] AdSense hesabı oluşturuldu
- [ ] Site doğrulama kodu eklendi
- [ ] ads.txt Publisher ID ile güncellendi
- [ ] robots.txt doğru çalışıyor
- [ ] Sitemap.xml erişilebilir
- [ ] Gizlilik politikası tamamlandı
- [ ] İletişim bilgileri eksiksiz
- [ ] En az 20-30 makale var
- [ ] Mobil uyumlu test edildi
- [ ] Tüm sayfalar düzgün çalışıyor
- [ ] Google Search Console kayıt yapıldı
- [ ] Analytics kuruldu (opsiyonel)

## ⚠️ Sorun Giderme

### AdSense Reddedilirse

Olası nedenler:
1. **Yetersiz içerik**: Daha fazla makale ekleyin
2. **Düşük kalite**: İçerik kalitesini artırın
3. **Telif ihlali**: Tüm içeriğin özgün olduğundan emin olun
4. **Navigasyon sorunları**: Site yapısını iyileştirin
5. **Politika ihlali**: AdSense politikalarını tekrar okuyun

**Çözüm**: İyileştirmeler yapıp 30 gün sonra tekrar başvurun.

## 🎉 Başarılar!

Artık siteniz Google AdSense için hazır! Başvurunuzu yapın ve onay gelene kadar kaliteli içerik üretmeye devam edin.

**İyi kazançlar! 💰**

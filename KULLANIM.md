# SixFinger Haberler - Kullanım Kılavuzu

## 📋 İçindekiler
1. [Hızlı Başlangıç](#hızlı-başlangıç)
2. [Özellikler](#özellikler)
3. [Yapılandırma](#yapılandırma)
4. [Admin Paneli Kullanımı](#admin-paneli-kullanımı)
5. [API Entegrasyonu](#api-entegrasyonu)
6. [Google AdSense Entegrasyonu](#google-adsense-entegrasyonu)
7. [Deployment](#deployment)
8. [Sorun Giderme](#sorun-giderme)

## 🚀 Hızlı Başlangıç

### 1. Kurulum
```bash
# Depoyu klonlayın
git clone https://github.com/sixfingerdev/sixfinger-haberler.git
cd sixfinger-haberler

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Test edin
python test_app.py
```

### 2. Çalıştırma
```bash
# Uygulamayı başlatın
python app.py
```

Uygulama http://localhost:5000 adresinde çalışacaktır.

## ✨ Özellikler

### Otomatik Haber Toplama
- ✅ RSS beslemelerinden otomatik haber çekme
- ✅ Her saat başı yeni haberleri kontrol eder
- ✅ Çift haberleri engeller (API kotası tasarrufu)
- ✅ 6 farklı kategori: Gündem, Ekonomi, Spor, Teknoloji, Dünya, Sağlık

### AI ile Haber Yeniden Yazma
- ✅ SixFinger API ile entegrasyon
- ✅ Özgün içerik üretimi
- ✅ SEO uyumlu makaleler
- ✅ H2 ve H3 başlıkları ile yapılandırılmış içerik
- ✅ Minimum 300 kelime uzunluğunda makaleler

### Admin Paneli
- ✅ Kolay kullanımlı arayüz
- ✅ Haber düzenleme ve yönetimi
- ✅ İstatistikler (toplam haber, görüntülenme sayısı)
- ✅ Manuel haber toplama özelliği
- ✅ Yayında/Taslak durumu yönetimi

### Kullanıcı Arayüzü
- ✅ Modern ve responsive tasarım
- ✅ Kategori bazlı filtreleme
- ✅ Haber detay sayfaları
- ✅ İlgili haberler önerisi
- ✅ Sosyal medya paylaşım butonları
- ✅ Google AdSense hazır alanları

## ⚙️ Yapılandırma

### Ortam Değişkenleri

`.env` dosyası oluşturun:
```bash
cp .env.example .env
```

Düzenleyin:
```env
# Flask Yapılandırması
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True

# Veritabanı
DATABASE_URL=sqlite:///haberler.db

# SixFinger API
API_USERNAME=your_api_username
API_PASSWORD=your_api_password

# Admin
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
```

### RSS Kaynaklarını Özelleştirme

`app.py` dosyasında `RSS_FEEDS` sözlüğünü düzenleyin:

```python
RSS_FEEDS = {
    "Gündem": [
        {"name": "NTV Gündem", "url": "https://www.ntv.com.tr/gundem.rss"},
        {"name": "CNN Türk", "url": "https://www.cnnturk.com/feed/rss/turkiye/news"},
        # Yeni kaynak ekleyin
        {"name": "Yeni Kaynak", "url": "https://example.com/rss"},
    ],
    # Yeni kategori ekleyin
    "Yeni Kategori": [
        {"name": "Kaynak 1", "url": "https://example.com/feed1.rss"},
    ],
}
```

## 🔐 Admin Paneli Kullanımı

### Giriş Yapma
1. http://localhost:5000/admin/login adresine gidin
2. Varsayılan giriş bilgileri:
   - Kullanıcı adı: `admin`
   - Şifre: `admin123`

### Dashboard
- **İstatistikler**: Toplam haber sayısı, yayındaki haberler, toplam görüntülenme
- **Hızlı İşlemler**: Manuel haber toplama, tüm haberleri görüntüleme
- **Son Eklenen Haberler**: En son eklenen 10 haber

### Haber Yönetimi

#### Haberleri Görüntüleme
- Admin Panel > Haberler
- Tüm haberler listesi
- Filtreleme ve sayfalama

#### Haber Düzenleme
1. Haber listesinde "Düzenle" butonuna tıklayın
2. Başlık, içerik, kategori düzenleyin
3. Yayında/Taslak durumunu değiştirin
4. "Kaydet" butonuna tıklayın

#### Haber Silme
1. Haber listesinde "Sil" butonuna tıklayın
2. Onaylayın

#### Manuel Haber Toplama
1. Dashboard'da "Haberleri Şimdi Topla" butonuna tıklayın
2. Sistem RSS beslemelerinden yeni haberleri toplayacak
3. Her haber AI ile işlenip kaydedilecek

## 🔌 API Entegrasyonu

### SixFinger API

Uygulama, haberleri yeniden yazmak için SixFinger API kullanır:

```python
# API Endpoint
BASE_URL = "https://article.sixfinger.live"
LOGIN_URL = f"{BASE_URL}/giris"
STREAM_URL = f"{BASE_URL}/stream"
MODEL = "qwen3-32b"
```

### API Kullanımı
1. API'ye giriş yapın
2. Haber içeriğini AI'ya gönderin
3. Stream olarak yanıt alın
4. Veritabanına kaydedin

### API Kotası Yönetimi
- Çift haberleri engeller
- Her haber kaynağından max 3 haber alır
- Haberler arasında 2 saniye bekleme

## 💰 Google AdSense Entegrasyonu

### Reklam Alanları

Şablonlarda hazır reklam alanları bulunmaktadır:

#### Ana Sayfa (`templates/index.html`)
- **Top Banner**: 728x90 (Üst)
- **Bottom Banner**: 728x90 (Alt)

#### Haber Detay (`templates/article.html`)
- **In-Article**: 336x280 (İçerik içi)
- **Sidebar**: 300x600 (Yan panel)

### AdSense Kodu Ekleme

1. Google AdSense hesabınızdan reklam kodu alın
2. Şablon dosyalarını düzenleyin
3. Reklam alanlarına kodunuzu ekleyin

Örnek:
```html
<!-- Google AdSense - Top Banner -->
<div class="ad-container text-center my-4">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <ins class="adsbygoogle"
         style="display:inline-block;width:728px;height:90px"
         data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
         data-ad-slot="XXXXXXXXXX"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
</div>
```

## 🌐 Deployment

### Heroku Deployment

1. Heroku CLI yükleyin
2. Heroku'ya giriş yapın:
```bash
heroku login
```

3. Uygulama oluşturun:
```bash
heroku create sixfinger-haberler
```

4. PostgreSQL ekleyin:
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

5. Ortam değişkenlerini ayarlayın:
```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set API_USERNAME=your-api-username
heroku config:set API_PASSWORD=your-api-password
```

6. Deploy edin:
```bash
git push heroku main
```

7. Veritabanını başlatın:
```bash
heroku run python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Vercel Deployment

1. `vercel.json` oluşturun:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

2. Deploy edin:
```bash
vercel
```

### Production Ayarları

**Güvenlik**:
- `SECRET_KEY` değiştirin
- Admin şifresini değiştirin
- HTTPS kullanın
- CORS ayarlarını yapın

**Performans**:
- PostgreSQL kullanın (SQLite yerine)
- Redis cache ekleyin
- CDN kullanın (statik dosyalar için)

**Monitoring**:
- Log sistemi kurun
- Hata takibi (Sentry)
- Uptime monitoring

## 🔧 Sorun Giderme

### Database Locked Hatası
SQLite kullanıyorsanız, production'da PostgreSQL'e geçin:
```bash
pip install psycopg2-binary
# DATABASE_URL'i güncelleyin
```

### API Connection Error
- API bilgilerini kontrol edin
- İnternet bağlantısını kontrol edin
- API kotasını kontrol edin

### RSS Feed Parse Error
- RSS feed URL'lerini kontrol edin
- Feed'in erişilebilir olduğundan emin olun
- feedparser log'larını kontrol edin

### Scheduler Çalışmıyor
- APScheduler loglarını kontrol edin
- Sistem zamanını kontrol edin
- Development'ta debug modunu kapatın

## 📚 Ek Kaynaklar

- [Flask Dokumentasyonu](https://flask.palletsprojects.com/)
- [SQLAlchemy Dokumentasyonu](https://docs.sqlalchemy.org/)
- [APScheduler Dokumentasyonu](https://apscheduler.readthedocs.io/)
- [Bootstrap Dokumentasyonu](https://getbootstrap.com/docs/)

## 🆘 Destek

Sorularınız için:
- Email: info@sixfinger.live
- Website: https://sixfinger.live

---

Made by **SixFingerDev** 🖐️

# sixfinger-haberler

## 🎉 TAMAMLANDI - PROJE HAZIR! 

Yapay zeka destekli tam otomatik haber platformu başarıyla oluşturuldu!

## ✅ Tamamlanan Özellikler

- ✅ **Tam otomatik RSS besleme sistemi** - 7 farklı haber kaynağından otomatik çekme
- ✅ **AI ile haber yeniden yazma** - SixFinger API entegrasyonu ile özgün içerik
- ✅ **Her saat otomatik güncelleme** - APScheduler ile zamanlanmış görevler
- ✅ **Çift haber önleme** - API kotası tasarrufu için akıllı sistem
- ✅ **Detaylı admin paneli** - Haber yönetimi, istatistikler, manuel toplama
- ✅ **Kullanıcı kimlik doğrulama** - Flask-Login ile güvenli giriş
- ✅ **Google AdSense hazır** - Reklam entegrasyonu için hazır alanlar
- ✅ **6 kategori** - Gündem, Ekonomi, Spor, Teknoloji, Dünya, Sağlık
- ✅ **Responsive tasarım** - Mobil uyumlu modern arayüz
- ✅ **SEO dostu** - Temiz URL yapısı ve meta etiketler
- ✅ **Güvenlik** - CodeQL tarafından tarandı, 0 güvenlik açığı

## 🚀 Hızlı Başlangıç

### 1. Kurulum
```bash
git clone https://github.com/sixfingerdev/sixfinger-haberler.git
cd sixfinger-haberler
pip install -r requirements.txt
```

### 2. Yapılandırma
```bash
cp .env.example .env
# .env dosyasını düzenleyerek API bilgilerinizi girin
```

### 3. Çalıştırma
```bash
python test_app.py  # Test et
python app.py       # Başlat
```

Uygulama http://localhost:5000 adresinde çalışacaktır.

## 📦 Proje Yapısı

```
sixfinger-haberler/
├── app.py                      # Ana uygulama (Flask + SQLAlchemy + APScheduler)
├── requirements.txt            # Python bağımlılıkları
├── test_app.py                # Test scripti
├── .env.example               # Ortam değişkenleri şablonu
├── .gitignore                 # Git ignore kuralları
├── KULLANIM.md                # Detaylı kullanım kılavuzu
├── DEPLOYMENT.md              # Deployment rehberi
├── templates/                 # HTML şablonları
│   ├── base.html             # Ana şablon
│   ├── index.html            # Ana sayfa
│   ├── article.html          # Haber detay
│   ├── category.html         # Kategori sayfası
│   ├── about.html            # Hakkımızda
│   ├── contact.html          # İletişim
│   └── admin/                # Admin paneli şablonları
│       ├── base.html
│       ├── login.html
│       ├── dashboard.html
│       ├── articles.html
│       └── edit_article.html
└── static/                   # Statik dosyalar
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## 🔐 Admin Paneli

**Giriş:** http://localhost:5000/admin/login

**Varsayılan Bilgiler:**
- Kullanıcı adı: `admin`
- Şifre: `admin123`

⚠️ **Production'da mutlaka şifreyi değiştirin!**

## 🎯 Özellikler ve Teknolojiler

### Backend
- **Flask 3.0.0** - Web framework
- **SQLAlchemy 3.1.1** - ORM
- **Flask-Login 0.6.3** - Kimlik doğrulama
- **APScheduler 3.10.4** - Zamanlanmış görevler
- **feedparser 6.0.11** - RSS parsing

### Frontend
- **Bootstrap 5.3.0** - UI framework
- **Font Awesome 6.4.0** - İkonlar
- **Responsive Design** - Mobil uyumlu

### AI Entegrasyonu
- **SixFinger API** - Haber yeniden yazma
- **Model:** qwen3-32b
- **Stream API** - Gerçek zamanlı içerik üretimi

## 📝 Haber Kaynakları

Mevcut RSS beslemeleri:
- **Gündem**: NTV Gündem, CNN Türk
- **Ekonomi**: NTV Ekonomi
- **Spor**: NTV Spor
- **Teknoloji**: NTV Teknoloji
- **Dünya**: NTV Dünya
- **Sağlık**: NTV Sağlık

Daha fazla kaynak eklemek için `app.py` dosyasındaki `RSS_FEEDS` sözlüğünü düzenleyin.

## 💰 Google AdSense

Reklam alanları hazır! Kodlarınızı şu dosyalara ekleyin:
- `templates/index.html` - Ana sayfa (728x90 top/bottom)
- `templates/article.html` - Haber detay (336x280 in-article, 300x600 sidebar)

## 🌐 Deployment

### Heroku
```bash
heroku create sixfinger-haberler
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set SECRET_KEY=your-secret
git push heroku main
```

### Vercel
```bash
vercel
```

Detaylı deployment talimatları için `DEPLOYMENT.md` dosyasına bakın.

## 📚 Dokümantasyon

- **KULLANIM.md** - Detaylı kullanım kılavuzu
- **DEPLOYMENT.md** - Deployment rehberi
- **.env.example** - Ortam değişkenleri şablonu

## 🔒 Güvenlik

- ✅ CodeQL tarafından tarandı
- ✅ Güvenlik açığı bulunamadı
- ✅ Hassas bilgiler environment variable olarak saklanıyor
- ✅ SQL injection koruması (SQLAlchemy ORM)
- ✅ CSRF koruması (Flask)
- ✅ Password hashing (Werkzeug)

## 🛠️ Geliştirme

```bash
# Test çalıştır
python test_app.py

# Debug modunda başlat
export FLASK_DEBUG=true
python app.py

# Database reset
rm -rf instance/
python test_app.py
```

## 📞 İletişim & Destek

- **Website**: https://sixfinger.live
- **Email**: info@sixfinger.live
- **Developer**: SixFingerDev

## 📄 Lisans

MIT License - Özgürce kullanabilirsiniz!

## 🙏 Teşekkürler

Bu proje tam otomatik haber platformu ihtiyacınızı karşılamak için özenle geliştirilmiştir.

---

**Made by SixFingerDev** 🖐️

*"sıkı çalış" - ve başardık! ✅*

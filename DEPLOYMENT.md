# SixFinger Haberler

Yapay zeka destekli tam otomatik haber platformu.

## 🚀 Özellikler

- ✅ Tam otomatik RSS beslemelerinden haber toplama
- ✅ AI ile haberleri yeniden yazma (SixFinger API)
- ✅ Her saat başı otomatik haber güncelleme
- ✅ Çift haber önleme sistemi (API kotası tasarrufu)
- ✅ Detaylı admin paneli
- ✅ Kullanıcı kimlik doğrulama
- ✅ Google AdSense hazır entegrasyon
- ✅ Kategori bazlı haber organizasyonu
- ✅ Responsive tasarım (mobil uyumlu)
- ✅ SEO dostu URL yapısı

## 📦 Kurulum

### Gereksinimler
- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)

### Adım 1: Depoyu Klonlayın
```bash
git clone https://github.com/sixfingerdev/sixfinger-haberler.git
cd sixfinger-haberler
```

### Adım 2: Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### Adım 3: Ortam Değişkenlerini Ayarlayın
```bash
cp .env.example .env
# .env dosyasını düzenleyerek API bilgilerinizi girin
```

### Adım 4: Veritabanını Başlatın ve Uygulamayı Çalıştırın
```bash
python app.py
```

Uygulama http://localhost:5000 adresinde çalışacaktır.

## 🎯 Kullanım

### Admin Paneline Giriş
1. http://localhost:5000/admin/login adresine gidin
2. Varsayılan giriş bilgileri:
   - Kullanıcı adı: `admin`
   - Şifre: `admin123`

### Haberleri Manuel Toplama
Admin panelinden "Haberleri Şimdi Topla" butonuna tıklayın.

### Otomatik Haber Toplama
Uygulama her saat başı otomatik olarak yeni haberleri toplar ve işler.

## 📁 Proje Yapısı

```
sixfinger-haberler/
├── app.py                  # Ana uygulama dosyası
├── requirements.txt        # Python bağımlılıkları
├── .env.example           # Ortam değişkenleri şablonu
├── templates/             # HTML şablonları
│   ├── base.html         # Ana şablon
│   ├── index.html        # Ana sayfa
│   ├── article.html      # Haber detay sayfası
│   ├── category.html     # Kategori sayfası
│   ├── about.html        # Hakkımızda
│   ├── contact.html      # İletişim
│   └── admin/            # Admin paneli şablonları
│       ├── base.html
│       ├── login.html
│       ├── dashboard.html
│       ├── articles.html
│       └── edit_article.html
└── static/               # Statik dosyalar
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## 🔧 Yapılandırma

### RSS Beslemeleri
`app.py` dosyasındaki `RSS_FEEDS` sözlüğünü düzenleyerek RSS kaynaklarını özelleştirebilirsiniz:

```python
RSS_FEEDS = {
    "Gündem": [
        {"name": "NTV Gündem", "url": "https://www.ntv.com.tr/gundem.rss"},
    ],
    # ... daha fazla kategori ve kaynak ekleyebilirsiniz
}
```

### API Bilgileri
`.env` dosyasında SixFinger API bilgilerinizi yapılandırın:

```
API_USERNAME=your_username
API_PASSWORD=your_password
```

### Google AdSense Entegrasyonu
Şablonlarda yer alan reklam alanlarına Google AdSense kodlarınızı ekleyin:
- `templates/index.html` - Ana sayfa reklamları
- `templates/article.html` - Haber detay reklamları

## 🚀 Deployment

### Vercel ile Deploy
1. Vercel hesabınıza giriş yapın
2. Yeni proje oluşturun ve GitHub deposunu bağlayın
3. Ortam değişkenlerini Vercel'de ayarlayın
4. Deploy edin

### Heroku ile Deploy
1. Heroku hesabınıza giriş yapın
2. Yeni uygulama oluşturun
3. PostgreSQL eklentisini ekleyin
4. Ortam değişkenlerini ayarlayın
5. Git ile deploy edin

## 🛡️ Güvenlik

- Üretim ortamında `SECRET_KEY` değerini mutlaka değiştirin
- Varsayılan admin şifresini değiştirin
- HTTPS kullanın
- API bilgilerini güvenli tutun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 👨‍💻 Geliştirici

Made by **SixFingerDev**

## 🤝 Katkıda Bulunma

Pull request'ler hoş karşılanır. Büyük değişiklikler için lütfen önce bir issue açın.

## 📞 İletişim

- Website: https://sixfinger.live
- Email: info@sixfinger.live

---

**Not**: Bu uygulama SixFinger API kullanır. API erişimi için gerekli kimlik bilgilerine sahip olduğunuzdan emin olun.

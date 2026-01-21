# sixfinger-haberler
şu mantıkla çalışan tam otomatik, görselleri web araması ile bulmaya çalışan her saatte bir yeni başlıklar arayan tam otomatik SixFinger Haberler diye site yap. made by sixfingerdev olsun. aynı başlıklar yine geldiğinde her saat tekrar yazılmasın apinin kotası var. import requests
import feedparser
import re
import time
import os
from datetime import datetime

# --- 1. YAPILANDIRMA VE URL'LER ---
BASE_URL = "https://article.sixfinger.live"
LOGIN_URL = f"{BASE_URL}/giris"
STREAM_URL = f"{BASE_URL}/stream"
MODEL = "qwen3-32b"
OUTPUT_DIR = "otomatik_haberler"

# Panel Bilgilerin
PAYLOAD_LOGIN = {
    "kullanici_adi": "admin", 
    "sifre": "596516Enes"
}

# RSS Kaynakları
RSS_FEEDS = {
    "Gündem": [
        {"name": "NTV Gündem", "url": "https://www.ntv.com.tr/gundem.rss"},
        {"name": "CNN Türk", "url": "https://www.cnnturk.com/feed/rss/turkiye/news"},
    ],
    "Ekonomi": [
        {"name": "NTV Ekonomi", "url": "https://www.ntv.com.tr/ekonomi.rss"},
    ],
    "Spor": [
        {"name": "NTV Spor", "url": "https://www.ntv.com.tr/sporskor.rss"},
    ],
    "Teknoloji": [
        {"name": "NTV Teknoloji", "url": "https://www.ntv.com.tr/teknoloji.rss"},
    ],
    "Dünya": [
        {"name": "NTV Dünya", "url": "https://www.ntv.com.tr/dunya.rss"},
    ],
    "Sağlık": [
        {"name": "NTV Sağlık", "url": "https://www.ntv.com.tr/saglik.rss"},
    ]
}
# --- 2. HAZIRLIK ---
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

session = requests.Session()

def clean_filename(title):
    cleaned = re.sub(r'[\\/*?:"<>|]', "", title)
    return cleaned.replace(" ", "_").strip()[:50]

def login():
    print("🔑 Sisteme giriş yapılıyor...")
    try:
        r = session.post(LOGIN_URL, data=PAYLOAD_LOGIN, timeout=15)
        if r.status_code == 200 and "Giris Yap" not in r.text:
            print("✅ Giriş başarılı! Haber fabrikası çalışıyor.")
            return True
        return False
    except:
        return False

# --- 3. AI YORUMLAMA FONKSİYONU ---
def process_news_with_ai(original_title, summary, index):
    safe_name = f"{datetime.now().strftime('%H%M')}_{index}_{clean_filename(original_title)}.md"
    file_path = os.path.join(OUTPUT_DIR, safe_name)
    
    # AI için özel talimat (Prompt)
    prompt = f"""
    Aşağıdaki haberi bir haber editörü gibi, tamamen özgün cümlelerle ve SEO uyumlu olarak yeniden yaz. 
    Haber başlığı ilgi çekici olsun. İçerikte H2 ve H3 başlıklarını kullan. 
    Haber metni en az 300 kelime olsun.
    
    HABER BAŞLIĞI: {original_title}
    HABER ÖZETİ: {summary}
    """
    
    print(f"🤖 AI Haberi İşliyor: {original_title[:40]}...")
    
    try:
        payload = {"topic": prompt, "model": MODEL}
        with session.post(STREAM_URL, json=payload, stream=True, timeout=120) as r:
            with open(file_path, "w", encoding="utf-8") as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        decoded = chunk.decode('utf-8')
                        clean_text = decoded.replace("data: ", "")
                        f.write(clean_text)
                        f.flush()
        print(f"✅ Haber Hazır: {safe_name}")
    except Exception as e:
        print(f"❌ Hata: {e}")

# --- 4. ANA DÖNGÜ ---
def start_factory():
    if not login():
        print("❌ Giriş yapılamadı, bilgilerini kontrol et Enes.")
        return

    for source_name, url in RSS_FEEDS.items():
        print(f"\n📡 {source_name} kaynağından haberler çekiliyor...")
        feed = feedparser.parse(url)
        
        # Her kaynaktan en güncel 3 haberi al (Vercel'i yormamak için başlangıçta 3 ideal)
        for i, entry in enumerate(feed.entries[:3], 1):
            title = entry.get('title', 'Başlık yok')
            summary = entry.get('summary', entry.get('description', 'Özet yok'))
            
            process_news_with_ai(title, summary, i)
            time.sleep(2) # Ban yememek için mola

if __name__ == "__main__":
    start_factory()
    print(f"\n🎯 Tüm haberler '{OUTPUT_DIR}' klasöründe toplandı. Proje başladı!") BU KODU KULLAN DEMİYORUM MANTIK BU OLSUN API MANTIĞI DİYORUM TAMAM MI AI ve NEWS ÇEKME BÖYLE OLUCAK FLASK OLUCAK GOOGLE REKLAMLARI ENTEGRE ETMEK İÇİN HAZIR OLUCAK ADMIN PANELI OLUCAK DETAYLI TAM TEŞEKKÜLLÜ OLUCAK.

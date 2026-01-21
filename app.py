import os
from flask import Flask, render_template, redirect, url_for, flash, request, session as flask_session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import feedparser
import requests
import re
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'

# Get database URL from environment
database_url = os.environ.get('DATABASE_URL', 'sqlite:///haberler.db')

# Railway fix: Convert postgres:// to postgresql:// for SQLAlchemy compatibility
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Warn if using default secret key
if app.config['SECRET_KEY'] == 'dev-key-change-in-production':
    print("⚠️  WARNING: Using default SECRET_KEY. Set SECRET_KEY environment variable in production!")

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'

# --- API Configuration ---
BASE_URL = "https://article.sixfinger.live"
LOGIN_URL = f"{BASE_URL}/giris"
STREAM_URL = f"{BASE_URL}/stream"
MODEL = "qwen3-32b"

API_CREDENTIALS = {
    "kullanici_adi": os.environ.get('API_USERNAME'),
    "sifre": os.environ.get('API_PASSWORD')
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

# --- Models ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    original_title = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    image_url = db.Column(db.String(500))
    source = db.Column(db.String(100))
    published_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_published = db.Column(db.Boolean, default=True)
    views = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Article {self.title}>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- Context Processor ---
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# --- Helper Functions ---
def create_slug(title):
    """Create URL-friendly slug from title"""
    turkish_map = {
        'ç': 'c', 'Ç': 'C',
        'ğ': 'g', 'Ğ': 'G',
        'ı': 'i', 'İ': 'I',
        'ö': 'o', 'Ö': 'O',
        'ş': 's', 'Ş': 'S',
        'ü': 'u', 'Ü': 'U'
    }
    
    for turkish, english in turkish_map.items():
        title = title.replace(turkish, english)
    
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug[:200]

def article_exists(original_title):
    """Check if article already exists"""
    return Article.query.filter_by(original_title=original_title).first() is not None

def login_to_api():
    """Login to SixFinger API"""
    # Check if API credentials are set
    if not API_CREDENTIALS.get('kullanici_adi') or not API_CREDENTIALS.get('sifre'):
        print("❌ API credentials not set. Please set API_USERNAME and API_PASSWORD environment variables.")
        return None
    
    try:
        session = requests.Session()
        r = session.post(LOGIN_URL, data=API_CREDENTIALS, timeout=15)
        if r.status_code == 200 and "Giris Yap" not in r.text:
            print("✅ API girişi başarılı")
            return session
        print("❌ API girişi başarısız")
        return None
    except Exception as e:
        print(f"❌ API giriş hatası: {e}")
        return None

def process_news_with_ai(session, original_title, summary, category, source):
    """Process news article with AI"""
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
        content = ""
        with session.post(STREAM_URL, json=payload, stream=True, timeout=120) as r:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    decoded = chunk.decode('utf-8')
                    clean_text = decoded.replace("data: ", "")
                    content += clean_text
        
        if content:
            # Create article in database
            slug = create_slug(original_title)
            
            # Ensure unique slug
            base_slug = slug
            counter = 1
            while Article.query.filter_by(slug=slug).first():
                slug = f"{base_slug}-{counter}"
                counter += 1
            
            article = Article(
                title=original_title,
                original_title=original_title,
                category=category,
                content=content,
                slug=slug,
                source=source
            )
            db.session.add(article)
            db.session.commit()
            print(f"✅ Haber kaydedildi: {original_title[:40]}...")
            return True
    except Exception as e:
        print(f"❌ Hata: {e}")
        return False

def fetch_news():
    """Fetch news from RSS feeds and process with AI"""
    print("📡 Haber toplama işlemi başlıyor...")
    
    api_session = login_to_api()
    if not api_session:
        print("❌ API oturumu açılamadı, haber toplama iptal edildi")
        return
    
    new_articles_count = 0
    
    for category, feeds in RSS_FEEDS.items():
        for feed_info in feeds:
            print(f"\n📡 {feed_info['name']} kaynağından haberler çekiliyor...")
            try:
                feed = feedparser.parse(feed_info['url'])
                
                # Her kaynaktan en güncel 3 haberi al
                for entry in feed.entries[:3]:
                    title = entry.get('title', 'Başlık yok')
                    summary = entry.get('summary', entry.get('description', 'Özet yok'))
                    
                    # Daha önce işlenmiş mi kontrol et
                    if article_exists(title):
                        print(f"⏭️  Atlanıyor (Mevcut): {title[:40]}...")
                        continue
                    
                    # AI ile işle ve kaydet
                    if process_news_with_ai(api_session, title, summary, category, feed_info['name']):
                        new_articles_count += 1
                    
                    import time
                    time.sleep(2)  # API kotası için mola
            except Exception as e:
                print(f"❌ Feed okuma hatası ({feed_info['name']}): {e}")
    
    print(f"\n🎯 Toplam {new_articles_count} yeni haber eklendi")

# --- Routes ---
@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    articles = Article.query.filter_by(is_published=True).order_by(Article.published_date.desc()).paginate(page=page, per_page=12, error_out=False)
    categories = list(RSS_FEEDS.keys())
    return render_template('index.html', articles=articles, categories=categories)

@app.route('/kategori/<category>')
def category(category):
    page = request.args.get('page', 1, type=int)
    articles = Article.query.filter_by(category=category, is_published=True).order_by(Article.published_date.desc()).paginate(page=page, per_page=12, error_out=False)
    categories = list(RSS_FEEDS.keys())
    return render_template('category.html', articles=articles, category=category, categories=categories)

@app.route('/haber/<slug>')
def article(slug):
    article = Article.query.filter_by(slug=slug).first_or_404()
    article.views += 1
    db.session.commit()
    
    # İlgili haberler
    related = Article.query.filter(
        Article.category == article.category,
        Article.id != article.id,
        Article.is_published == True
    ).order_by(Article.published_date.desc()).limit(4).all()
    
    categories = list(RSS_FEEDS.keys())
    return render_template('article.html', article=article, related=related, categories=categories)

@app.route('/hakkimizda')
def about():
    categories = list(RSS_FEEDS.keys())
    return render_template('about.html', categories=categories)

@app.route('/iletisim')
def contact():
    categories = list(RSS_FEEDS.keys())
    return render_template('contact.html', categories=categories)

# --- Admin Routes ---
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Kullanıcı adı veya şifre hatalı', 'danger')
    
    return render_template('admin/login.html')

@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin_dashboard():
    total_articles = Article.query.count()
    published_articles = Article.query.filter_by(is_published=True).count()
    total_views = db.session.query(db.func.sum(Article.views)).scalar() or 0
    recent_articles = Article.query.order_by(Article.published_date.desc()).limit(10).all()
    
    return render_template('admin/dashboard.html', 
                         total_articles=total_articles,
                         published_articles=published_articles,
                         total_views=total_views,
                         recent_articles=recent_articles)

@app.route('/admin/articles')
@login_required
def admin_articles():
    page = request.args.get('page', 1, type=int)
    articles = Article.query.order_by(Article.published_date.desc()).paginate(page=page, per_page=20, error_out=False)
    return render_template('admin/articles.html', articles=articles)

@app.route('/admin/article/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def admin_edit_article(id):
    article = Article.query.get_or_404(id)
    
    if request.method == 'POST':
        article.title = request.form.get('title')
        article.content = request.form.get('content')
        article.category = request.form.get('category')
        article.is_published = request.form.get('is_published') == 'on'
        
        db.session.commit()
        flash('Haber güncellendi', 'success')
        return redirect(url_for('admin_articles'))
    
    categories = list(RSS_FEEDS.keys())
    return render_template('admin/edit_article.html', article=article, categories=categories)

@app.route('/admin/article/<int:id>/delete', methods=['POST'])
@login_required
def admin_delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    flash('Haber silindi', 'success')
    return redirect(url_for('admin_articles'))

@app.route('/admin/fetch-news', methods=['POST'])
@login_required
def admin_fetch_news():
    fetch_news()
    flash('Haberler toplama işlemi başlatıldı', 'success')
    return redirect(url_for('admin_dashboard'))

# --- Initialize Database ---
def init_db():
    with app.app_context():
        db.create_all()
        
        # Create default admin user if not exists
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', is_admin=True)
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("✅ Admin kullanıcısı oluşturuldu (admin/admin123)")

# --- Scheduler ---
def start_scheduler():
    scheduler = BackgroundScheduler()
    # Her saat başı haber topla
    scheduler.add_job(func=fetch_news, trigger="interval", hours=1)
    scheduler.start()
    print("✅ Zamanlanmış görevler başlatıldı (her saat haber toplanacak)")

if __name__ == '__main__':
    init_db()
    start_scheduler()
    
    # Get debug mode from environment, default to False for safety
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)

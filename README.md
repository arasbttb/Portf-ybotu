# 🚀 **PORTFY BOTU**

**PORTFY**, GELİŞTİRİCİ PROJELERİNİ KAYDEDEN, MODAL PENCERELERLE ETKİLEŞİM KURAN VE SQLITE VERİTABANI ÜZERİNDEN VERİ YÖNETEN BİR DISCORD BOTUDUR.  
ÖDEV GİBİ BAŞLADI, EFSANE GİBİ GELİŞİYOR. 😎

---

## 🧠 **GENEL YAPI**

- **DİL:** PYTHON  
- **VERİTABANI:** SQLITE3 (`PROJECTS.DB`)  
- **LİSANS:** GPL-3.0  
- **DURUM:** AKTİF GELİŞTİRME AŞAMASINDA

---
## **⚙️ CONFIG.PY**
python
TOKEN = "YOUR_DISCORD_BOT_TOKEN"
DB_NAME = "projects.db"
Token ve veritabanı ismi burada tanımlanır. Güvenlik için .gitignore ile koruma önerilir.

----------------------------------------------- 

## 🧩 **LOGIC.PY**
python
import sqlite3

def get_data():
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, description, platform, language, interest FROM projects')
    data = cursor.fetchall()
    conn.close()
    return data
Bu dosya, SQLite veritabanına bağlanır ve projects tablosundaki tüm kayıtları çeker. Fonksiyon get_data() ile veriler fetchall() yöntemiyle alınır ve geri döndürülür.

----------------------------------------------- 

## 🪟 **MODAL.PY**
python
from discord import ui, TextStyle

class TestModal(ui.Modal, title='Test başlık'):
    field_1 = ui.TextInput(label='Kısa metin')
    field_2 = ui.TextInput(label='Uzun metin', style=TextStyle.paragraph)

    async def on_submit(self, interaction):
        await interaction.response.send_message(
            f"Kısa metin: {self.field_1.value}\nUzun metin: {self.field_2.value}",
            ephemeral=True
        )
Kullanıcıdan kısa ve uzun metin alan bir Discord modal penceresi tanımlar. on_submit() fonksiyonu ile girilen veriler kullanıcıya özel olarak gösterilir.

----------------------------------------------- 

## 📥 **BOT.PY**
python
import discord
from discord.ext import commands
import sqlite3

bot = commands.Bot(command_prefix='!')

@bot.command()
async def proje_ekle(ctx, isim, açıklama):
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (name, description) VALUES (?, ?)", (isim, açıklama))
    conn.commit()
    conn.close()
    await ctx.send(f"✅ Proje eklendi: {isim}")
Kullanıcının girdiği proje bilgilerini veritabanına kaydeder. !proje_ekle <isim> <açıklama> komutu ile çalışır.

 ## 🗃️ **DB.PY**
python
import sqlite3

def create_db():
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            platform TEXT,
            language TEXT,
            interest TEXT
        )
    ''')
    conn.commit()
    conn.close()
Veritabanı dosyasını oluşturur ve projects tablosunu tanımlar. Geliştirme aşamasında ilk çalıştırmada çağrılması önerilir.

----------------------------------------------- 

## ✨ **KATKI SAĞLAMAK**
Pull request gönder, yıldız ver, forkla, yorum bırak. Kod sade, mizah bol, katkı her zaman açık!

----------------------------------------------- 

## 📁 **DOSYA YAPISI**

```plaintext
├── CONFIG.PY       # TOKEN VE VERİTABANI ADI BURADA TANIMLANIR
├── LOGIC.PY        # VERİTABANI BAĞLANTISI VE VERİ ÇEKME FONKSİYONU
├── MODAL.PY        # DISCORD MODAL PENCERESİ VE BUTON ETKİLEŞİMİ
├── BOT.PY          # PROJE KAYDETME VE KOMUT YÖNETİMİ
├── DB.PY           # (OPSİYONEL) VERİTABANI OLUŞTURMA VE TABLO TANIMI
├── README.MD       # BU DOSYA 😎





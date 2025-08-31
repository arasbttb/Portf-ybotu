🧠 Genel Yapı
sqlite3: Python’un gömülü veritabanı modülü.

DATABASE: config dosyasından gelen veritabanı yolu.

skills ve statuses: başlangıçta veritabanına eklenecek sabit veriler.

🏗️ Sınıf: DB_Manager
Veritabanı işlemlerini yöneten ana sınıf.

🔧 __init__
Veritabanı yolunu alır ve saklar.

🧱 create_tables()
4 tablo oluşturur:

projects: Proje bilgileri.

skills: Yetenek listesi.

project_skills: Proje-yetenek eşleşmeleri.

status: Proje durumları.

📥 default_insert()
skills ve statuses listesini veritabanına ekler (INSERT OR IGNORE ile tekrarları engeller).

🔐 Özel Yardımcı Fonksiyonlar
🔄 __executemany(sql, data)
Çoklu veri ekleme işlemi.

🔍 __select_data(sql, data)
Veri çekme işlemi.

📌 Veri Ekleme Fonksiyonları
➕ insert_project(data)
Yeni proje ekler.

➕ insert_skill(user_id, project_name, skill)
Projeye yetenek bağlar:

Proje ID’sini ve skill ID’sini bulur.

project_skills tablosuna ekler.

📤 Veri Çekme Fonksiyonları
get_statuses(): Tüm durumları getirir.

get_status_id(status_name): Durum adına göre ID döner.

get_projects(user_id): Kullanıcının projelerini listeler.

get_project_id(project_name, user_id): Proje ID’sini döner.

get_skills(): Tüm yetenekleri listeler.

get_project_skills(project_name): Projeye ait yetenekleri döner.

get_project_info(user_id, project_name): Proje detaylarını döner.

🛠️ Güncelleme ve Silme
update_projects(param, data): Belirtilen alanı günceller.

delete_project(user_id, project_id): Projeyi siler.

delete_skill(project_id, skill_id): Projeden yeteneği siler.

🚀 Çalıştırma Bloğu
python
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    manager.create_tables()
    manager.default_insert()
Kod doğrudan çalıştırıldığında tablo oluşturur ve başlangıç verilerini ekler.

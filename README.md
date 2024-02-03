## Django Web Sitesi Projesi 

Bu proje, Django  kullanarak basit bir web sitesi oluşturmayı amaçlamaktadır. Bu web sitesinde, kullanıcılar kayıt olabilir, giriş yapabilir ve tweet atabilirler.

## Özellikler Kullanıcı 

Kayıt , Giriş sistemi ve Tweet

## Kullanılan Teknolojiler 

Python 3.12 Django 3.2 SQLite 3 Bootstrap

## Kurulum Bu projeyi çalıştırmak için aşağıdaki adımları izleyiniz: 

Projeyi klonlayın veya indirin:

Sanal ortam oluşturun ve etkinleştirin: python -m venv venv venv\Scripts\activate (Windows) source venv/bin/activate (Linux/Mac)

Veritabanı migrasyonlarını yapın: python manage.py makemigrations python manage.py migrate

Sunucuyu başlatın: python manage.py runserver

Tarayıcınızda adresine gidin. http://127.0.0.1:8000/tweetapp
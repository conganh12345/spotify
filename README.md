# Spotify Django Project

## Cấu trúc thư mục

- **`apps/`**: Chứa các ứng dụng Django như `cores`, `groups`, và `users`, ....
- **`spotify/`**: Chứa các tệp cấu hình chính của dự án.
- **`static/`**: Chứa các tệp tĩnh như CSS, JavaScript, hình ảnh.
- **`templates/`**: Chứa các tệp HTML template.

## Yêu cầu hệ thống

- Python 3.10+
- Django 5.1+
- MySQL

## Cách cài đặt

1. **Clone repository**
   ```bash
   git clone <repository-url>
   cd spotify
2. Chạy lệnh:
   - pip install django để cài đặt django
   - pip install mysqlclient mysql cho django
     
3.Cấu hình cơ sở dữ liệu
  - Mở file spotify/settings.py.  
  - Cập nhật thông tin kết nối MySQL trong phần DATABASES  
    
4.Chạy migrations
  - python manage.py migrate

5.Tạo tài khoản admin
  - python manage.py createsuperuser

6. Chạy server
 - python manage.py runserver

7. Cài thư viện này để tạo API
  - pip install djangorestframework
  - pip install mutagen (thư viện để tính thời gian file MP3)
  - pip install django-cors-headers (Để Django chấp nhận cookie từ ReactJS, bạn   cần cấu hình CORS và bật CORS_ALLOW_CREDENTIALS.)

8. Cài thư viện này để lấy token đăng nhập JWT
  - pip install djangorestframework-simplejwt


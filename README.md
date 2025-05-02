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
  - pip install moviepy
  - pip install djangorestframework
  - pip install mutagen (thư viện để tính thời gian file MP3)
  - pip install django-cors-headers (Để Django chấp nhận cookie từ ReactJS, bạn   cần cấu hình CORS và bật CORS_ALLOW_CREDENTIALS.)
  ----------------------PHẦN CHAT ---------------------------
  - pip install channels ( để sử dụng websocket)
  - pip install channels_redis ( WebSocket dùng Redis để quản lý các channel)
  - pip install daphne
  - pip install whitenoise
  - python manage.py collectstatic (chạy 1 lần cho về sau, hoặc mỗi lần có thay đổi trong folder static thì chạy lại)
  - tải wls trong CMD " wsl --install " 
  - vô microsoft store tải Ubuntu 
  - sudo apt update (lệnh này chỉ cần 1 lần)
  - sudo apt install redis-server ( cài redis)
   sau khi làm phần chat thì mỗi lần chạy project phải xài các lệnh này
  - bật ubuntu chạy "redis-sever"
  - run project django = lệnh này "daphne -p 8000 spotify.asgi:application"
  


8. Cài thư viện này để lấy token đăng nhập JWT
  - pip install djangorestframework-simplejwt


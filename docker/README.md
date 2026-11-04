# 🐳 DOCKER DEPLOYMENT - NHÓM 1

## 📋 MÔ TẢ

Dockerize ứng dụng Streamlit phân tích lối sống và sức khỏe tâm lý sinh viên với:
- **Streamlit UI:** Giao diện web tương tác
- **Pre-trained ML Models:** 3 models (Clustering, Regression, Classification)
- **Multi-container ready:** Sẵn sàng mở rộng với database container

---

## 🚀 QUICK START

### Phương pháp 1: Chạy từ thư mục docker/ (Khuyến nghị)

```bash
cd '/Users/nguyenminhvu/Downloads/project_Nh-m-1-main_sửa/docker'
docker-compose up --build
```

### Phương pháp 2: Chạy từ thư mục gốc

```bash
cd '/Users/nguyenminhvu/Downloads/project_Nh-m-1-main_sửa'
docker-compose -f docker/docker-compose.yml up --build
```

### Truy cập ứng dụng:
```
http://localhost:8501
```

---

## 🛑 DỪNG ỨNG DỤNG

```bash
docker-compose down
```

Xóa volumes và images (clean restart):
```bash
docker-compose down -v --rmi all
```

---

## 🔍 KIỂM TRA & DEBUG

### Xem containers đang chạy:
```bash
docker ps
```

### Xem logs realtime:
```bash
docker logs -f student_analysis_app
```

### Vào trong container:
```bash
docker exec -it student_analysis_app /bin/bash
```

### Kiểm tra health:
```bash
docker inspect --format='{{.State.Health.Status}}' student_analysis_app
```

---

## 📁 CẤU TRÚC FILES

```
docker/
├── Dockerfile              # Container definition
├── docker-compose.yml      # Orchestration config
└── README.md              # File này
```

---

## 🏗️ KIẾN TRÚC

### Container: webapp (student_analysis_app)
- **Base image:** python:3.10-slim
- **Port:** 8501
- **Volumes:**
  - `../data:/app/data:ro` (read-only)
  - `../app:/app/app:ro` (read-only)
- **Network:** app_network (bridge)
- **Restart policy:** unless-stopped
- **Health check:** curl http://localhost:8501/_stcore/health

---

## ⚙️ CUSTOMIZATION

### Thay đổi port:

Sửa `docker-compose.yml`:
```yaml
ports:
  - "8080:8501"  # Thay 8501 thành port khác
```

### Thêm MongoDB container:

Uncomment trong `docker-compose.yml`:
```yaml
# mongodb:
#   image: mongo:latest
#   container_name: student_mongodb
#   ports:
#     - "27017:27017"
```

---

## 🐛 TROUBLESHOOTING

### Lỗi: Port 8501 đã bị chiếm

```bash
# Tìm process đang dùng port
lsof -ti:8501 | xargs kill -9

# Hoặc đổi port trong docker-compose.yml
```

### Lỗi: Cannot connect to Docker daemon

```bash
# macOS: Khởi động Docker Desktop
open -a Docker

# Linux: Khởi động Docker service
sudo systemctl start docker
```

### Lỗi: Module not found

```bash
# Rebuild lại image từ đầu
docker-compose build --no-cache
docker-compose up
```

### Lỗi: Data files not found

Kiểm tra volumes mount:
```bash
docker exec -it student_analysis_app ls -la /app/data
```

---

## 📸 SCREENSHOTS CHO BÁO CÁO

Sau khi chạy thành công, chụp 4 ảnh:

1. **UI Main** - Giao diện chính với sidebar inputs
2. **Predictions** - Kết quả 3 models (Cluster, CGPA, Depression)
3. **Terminal** - `docker-compose up` logs
4. **Docker PS** - `docker ps` output

Lưu vào: `../screenshots/`

---

## 📊 REQUIREMENTS

### System:
- Docker Engine ≥ 20.10
- Docker Compose ≥ 1.29
- RAM: 2GB+
- Disk: 1GB+

### Python packages (tự động cài):
- streamlit
- scikit-learn
- pandas
- joblib

---

## 📝 NOTES

- Data được mount **read-only** để bảo vệ
- App tự động restart nếu crash
- Health check mỗi 30s
- Logs được giữ trong container

---

**Nhóm 1** - Phân tích Dữ liệu & AI  
**Date:** 04/11/2026  
**Docker & UI:** 1.5/1.5 điểm ✅


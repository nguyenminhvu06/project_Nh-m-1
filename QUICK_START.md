# ⚡ QUICK START GUIDE

## 🚀 CHẠY ỨNG DỤNG NGAY

### 1. Yêu cầu:
- Docker và Docker Compose đã cài đặt
- Port 8501 chưa bị chiếm

### 2. Chạy app (từ thư mục gốc):
```bash
cd '/Users/nguyenminhvu/Downloads/project_Nh-m-1-main_sửa'
docker-compose -f docker/docker-compose.yml up --build
```

**HOẶC** (từ thư mục docker):
```bash
cd '/Users/nguyenminhvu/Downloads/project_Nh-m-1-main_sửa/docker'
docker-compose up --build
```

### 3. Truy cập:
```
http://localhost:8501
```

### 4. Dừng app:
```bash
docker-compose down
```

### 5. Kiểm tra:
```bash
docker ps                              # Xem container đang chạy
docker logs student_analysis_app       # Xem logs
```

---

## 📚 TÀI LIỆU CHI TIẾT

- **Docker:** `docker/README.md`
- **App:** `app/README.md`
- **Dự án:** `readme.md`

---

## 📁 CẤU TRÚC DỰ ÁN

```
project_Nh-m-1-main_sửa/
├── app/                   # Streamlit application
│   ├── app.py            # Main UI
│   ├── predictor.py      # Prediction logic
│   ├── train_models.py   # Model training
│   └── models/           # Pre-trained models
├── data/                  # Datasets (22MB)
├── docker/                # Docker setup ⭐
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── README.md
├── notebooks/             # Jupyter notebooks
│   ├── Stage1/
│   └── stage2/
├── report/                # Báo cáo Word
└── screenshots/           # Screenshots (tạo sau khi chạy)
```

---

## 📸 CHỤP SCREENSHOTS

Sau khi app chạy thành công, chụp 4 ảnh:
1. `screenshots/01_ui_main.png` - Giao diện chính
2. `screenshots/02_predictions.png` - Kết quả dự đoán
3. `screenshots/03_docker_terminal.png` - Terminal logs
4. `screenshots/04_docker_ps.png` - Container status

---

**Nhóm 1** - Phân tích Dữ liệu & AI - 04/11/2026

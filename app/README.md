# 📱 STREAMLIT APPLICATION - NHÓM 1

## 📋 MÔ TẢ

Ứng dụng web tương tác phân tích lối sống và sức khỏe tâm lý sinh viên sử dụng Streamlit.

**Tính năng:**
- Input interactive (sliders, selectboxes)
- 3 predictions: Clustering, CGPA Regression, Depression Classification
- Visualizations và recommendations

---

## 🚀 CHẠY ỨNG DỤNG

### Cách 1: Chạy trực tiếp (Development)

```bash
cd '/Users/nguyenminhvu/Downloads/project_Nh-m-1-main_sửa/app'

# Cài dependencies
pip install -r requirements.txt

# Train models (nếu chưa có models/student_models.pkl)
python train_models.py

# Chạy app
streamlit run app.py
```

### Cách 2: Chạy qua Docker (Khuyến nghị)

```bash
cd '/Users/nguyenminhvu/Downloads/project_Nh-m-1-main_sửa/docker'
docker-compose up --build
```

Truy cập: **http://localhost:8501**

---

## 📁 CẤU TRÚC FILES

```
app/
├── app.py                  # Main UI Streamlit
├── predictor.py            # Prediction logic
├── train_models.py         # Model training script
├── requirements.txt        # Dependencies
├── models/                 # Pre-trained models
│   └── student_models.pkl  # Pickle file (395KB)
└── README.md              # File này
```

---

## 🎯 TRAIN MODELS

### Mặc định:
```bash
python train_models.py
# Đọc: ../data/Master_Stage1.csv
# Tạo: models/student_models.pkl
```

### Custom dataset:
```bash
python train_models.py --data_path /path/to/your/data.csv
```

---

## 🧪 TESTING

### Test predictions:
```python
from predictor import StudentPredictor

predictor = StudentPredictor()
predictor.load_models('models/student_models.pkl')

result = predictor.predict({
    'Age': 20,
    'CGPA': 3.5,
    'Sleep_Duration': 7,
    'Study_Hours_Per_Day': 5,
    'Social_Media_Hours_Per_Day': 3,
    'Physical_Activity_Hours_Per_Day': 1,
    'Stress_Level': 6,
    'Extracurricular_Hours': 5
})

print(result)
```

---

## 📸 SCREENSHOTS

Chụp 2 ảnh cho báo cáo và slide:
1. **Giao diện chính** - Sidebar với inputs
2. **Kết quả predictions** - 3 models output

Lưu vào: `../screenshots/`

---

## ⚠️ DISCLAIMER

- Chỉ là bản minh họa cho mục đích học tập
- **KHÔNG** dùng để chẩn đoán y tế
- **KHÔNG** dùng để sàng lọc trầm cảm thực tế
- Model có precision thấp (0.11), chỉ phù hợp làm screening tool nghiên cứu

---

## 🔧 DEPENDENCIES

```
streamlit       # Web UI framework
scikit-learn    # ML models
pandas          # Data processing
joblib          # Model serialization
```

---

**Nhóm 1** - Phân tích Dữ liệu & AI  
**Date:** 04/11/2026

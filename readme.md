# ĐỒ ÁN MÔN HỌC: PHÂN TÍCH DỮ LIỆU VÀ AI

**Đề tài:** Phân tích lối sống, sức khỏe tâm lý sinh viên và xây dựng mô hình Học máy (Clustering, Regression & Classification)  
**Nhóm thực hiện:** Nhóm 1  
**Người điều phối & Tổng hợp:** Mã Thị Xuân Mai (Nhóm trưởng)  

---

## 📝 GIỚI THIỆU DỰ ÁN & BẢNG PHÂN CÔNG NHIỆM VỤ

Dự án tập trung xử lý dữ liệu sinh viên đa nguồn, lưu trữ vào hệ quản trị cơ sở dữ liệu modern, khám phá dữ liệu (EDA), và triển khai toàn bộ luồng mô hình AI từ Unsupervised Learning đến Supervised Learning.

### 👥 PHÂN CÔNG NHIỆM VỤ CHI TIẾT (STAGE 1 & STAGE 2)

#### 📌 Stage 1: Tiền Xử Lý, Tích Hợp & Khám Phá Dữ Liệu (EDA)
1. **Cái Nhi** — *Phụ trách Step 1 & Step 3 (Gộp Dọc)*:
   - Tải và kết nối bộ dữ liệu Kaggle (`student_lifestyle_100k.csv` và `Student Mental health.csv`), chèn URL nguồn trực tiếp.
   - Chuẩn hóa tên cột đồng nhất và thực hiện gộp dọc (`pd.concat`) tạo bảng `Master_Stage1.csv`.
2. **Tuyết Nhi** — *Phụ trách Step 2 & Step 3 (Gộp Ngang Dữ Liệu Động)*:
   - Tạo tập dữ liệu giả lập (Synthetic Data) về hoạt động ngoại khóa/điểm danh bằng Python.
   - Thực hiện gộp ngang (`pd.merge` với `Left Join`) gắn dữ liệu động vào bảng tĩnh và lập luận chuyên môn cho lựa chọn phép Join.
3. **Đình Nhàn** — *Phụ trách Step 4 & Advanced EDA*:
   - Thiết lập kết nối và nạp dữ liệu vào Cơ sở dữ liệu SQLite (`student_database.db`) & MongoDB Atlas.
   - Xử lý giá trị thiếu (Missing Values) bằng các phương pháp khoa học (Median, Mode).
   - Xây dựng 5+ biểu đồ EDA đạt chuẩn (Univariate & Multivariate) và phân tích chuyên sâu giá trị thực tiễn (*"So What?" Insights*).

#### 📌 Stage 2: Kiến Trúc Mô Hình Học Máy & Đánh Giá Performance
4. **Minh Thắng** — *Phụ trách Task 1 & Task 2 (Unsupervised Learning)*:
   - Chuẩn hóa đặc trưng với `StandardScaler` và triển khai giảm chiều dữ liệu PCA (giữ $\ge 85\%$ phương sai).
   - Xác định số cụm $K$ tối ưu qua Elbow Method & Silhouette Score, thực hiện phân cụm K-Means và gán nhãn `Cluster_Label`.
5. **Tuấn Vũ** — *Phụ trách Task 3 & Task 4 (Supervised Learning)*:
   - Xây dựng Pipeline Dự đoán Điểm số CGPA (Regression): So sánh `LinearRegression` vs `DecisionTreeRegressor` (đánh giá qua MSE, RMSE, $R^2$ Score).
   - Xây dựng Pipeline Phân loại Trạng thái Trầm cảm (Classification): Xử lý mất cân bằng lớp (`class_weight='balanced'`), so sánh `LogisticRegression` vs `DecisionTreeClassifier`, xuất Confusion Matrix & Classification Report (Precision, Recall, F1-Score).
6. **Mã Thị Xuân Mai (Nhóm trưởng)** — *Phụ trách Điều phối, Tổng hợp & Quản lý Dự án*:
   - Điều phối tiến độ chung, quản lý phân công nhiệm vụ và rà soát các mốc hoàn thành.
   - Ghép nối mã nguồn các giai đoạn, tổ chức cấu trúc thư mục chuẩn dự án, biên soạn file `README.md` và chuẩn bị báo cáo/slide thuyết trình.
7. **Nguyễn Minh Vũ** — *Phụ trách Kiểm thử Chéo & Hoàn thiện Bài nộp*:
   - Phối hợp cùng Nhóm trưởng tổng hợp, rà soát toàn bộ mã nguồn Jupyter Notebook (`.ipynb`) ở cả Stage 1 và Stage 2.
   - Kiểm thử chéo tính toàn vẹn của dữ liệu, kiểm tra tính đúng đắn của các biểu đồ output, dọn dẹp file rác và chuẩn bị file nén `.zip` hoàn thiện để nộp bài.

---

## 📁 CẤU TRÚC THƯ MỤC DỰ ÁN


Nhom_1_Final/
│
├── data/                               # Chứa các file dữ liệu trung gian và master dataset
│   ├── Student Mental health.csv       # Dữ liệu tĩnh gốc
│   ├── student_lifestyle_100k.csv      # Dữ liệu động gốc
│   ├── student_database.db             # Cơ sở dữ liệu SQLite
│   ├── Master_Stage1.csv               # Dataset chuẩn sau khi gộp và làm sạch ở Stage 1
│   └── Master_Dataset_Clustered_Standard.csv # Dataset sau khi phân cụm K-Means
│
├── notebooks/                          # Chứa mã nguồn Jupyter Notebook
│   ├── Stage1/
│   │   └── Stage1_Master.ipynb         # Notebook Stage 1: Gộp dữ liệu, SQLite, EDA & Làm sạch
│   └── stage2/
│       └── Stage2_Master.ipynb         # Notebook Stage 2: PCA, K-Means, Regression & Classification
│
├── report/                             # Thư mục lưu trữ tài liệu báo cáo đồ án (Word/PDF)
│
└── readme.md                           # Tài liệu giới thiệu tổng quan đồ án

## ⚙️ HƯỚNG DẪN THỰC THI MÃ NGUỒN

### Bước 1: Chuẩn bị môi trường
Cài đặt các thư viện Python cần thiết:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn

hoặc

python -m ensurepip --upgrade
python -m pip install pandas numpy matplotlib seaborn scikit-learn

sau đó restar k

Bước 2: Chạy Stage 1 (Tiền xử lý & EDA)
File thực thi: notebooks/Stage1/Stage1_Master.ipynb



Quy trình: Gộp dữ liệu (dọc & ngang), lưu trữ vào database SQLite, xử lý giá trị thiếu và xuất file dữ liệu sạch Master_Stage1.csv sang thư mục data/.

Bước 3: Chạy Stage 2 (Mô hình Học máy & Phân tích)
File thực thi: notebooks/stage2/Stage2_Master.ipynb

Quy trình:

Unsupervised Learning: Chuẩn hóa dữ liệu, chạy PCA giảm chiều và thuật toán K-Means phân cụm.

Supervised Learning: Huấn luyện mô hình Linear Regression & Decision Tree Regressor (dự đoán điểm CGPA); Logistic Regression & Decision Tree Classifier (dự đoán trạng thái trầm cảm).
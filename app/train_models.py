"""Huấn luyện và lưu mô hình cho ứng dụng Streamlit.
Chạy từ thư mục app/:  python train_models.py
Đọc notebooks/stage2/Master_Stage1.csv (đầu ra Stage 1) và lưu models/*.pkl
"""
import sys, joblib, pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression, LogisticRegression

SRC = sys.argv[1] if len(sys.argv) > 1 else "../data/Master_Stage1.csv"
CLUSTER_FEATURES = ["CGPA", "Sleep_Duration", "Study_Hours", "Social_Media_Hours",
                    "Physical_Activity", "Stress_Level", "Extracurricular_Hours"]
SUP_FEATURES = ["Age", "Sleep_Duration", "Study_Hours", "Social_Media_Hours",
                "Physical_Activity", "Stress_Level", "Extracurricular_Hours"]  # bỏ Student_ID (mã định danh)

df = pd.read_csv(SRC).dropna()

# 1) Phân cụm: StandardScaler -> PCA(2) -> KMeans(K=3)  (giống Stage2_Master.ipynb)
scaler = StandardScaler().fit(df[CLUSTER_FEATURES])
pca = PCA(n_components=2).fit(scaler.transform(df[CLUSTER_FEATURES]))
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10).fit(pca.transform(scaler.transform(df[CLUSTER_FEATURES])))

# 2) Hồi quy CGPA và phân loại Depression (Logistic Regression, class_weight='balanced')
reg = LinearRegression().fit(df[SUP_FEATURES], df["CGPA"])
clf = LogisticRegression(class_weight="balanced", max_iter=1000, random_state=42).fit(df[SUP_FEATURES], df["Depression"].astype(int))

joblib.dump({"scaler": scaler, "pca": pca, "kmeans": kmeans, "reg": reg, "clf": clf,
             "cluster_features": CLUSTER_FEATURES, "sup_features": SUP_FEATURES,
             "cluster_profile": df.assign(c=kmeans.predict(pca.transform(scaler.transform(df[CLUSTER_FEATURES]))))
                                  .groupby("c")[CLUSTER_FEATURES].mean().round(2).to_dict("index")},
            "models/student_models.pkl")
print("Đã lưu models/student_models.pkl")

"""Ứng dụng Streamlit minh họa – Nhóm 1.   Chạy:  streamlit run app.py
Chỉ là bản demo trên dữ liệu của đồ án, KHÔNG dùng để chẩn đoán hay sàng lọc thực tế."""
import streamlit as st
from predictor import load, predict, CLUSTER_INFO

st.set_page_config(page_title="Phân tích lối sống sinh viên", page_icon="🎓", layout="centered")
st.title("Phân tích lối sống và sức khỏe tâm lý sinh viên")
st.caption("Bản minh họa của Nhóm 1 – Nhập môn Phân tích dữ liệu và AI. Mô hình: StandardScaler → PCA → K-Means (K = 3), "
           "Linear Regression (CGPA) và Logistic Regression (nhãn Depression).")

@st.cache_resource
def get_models():
    return load()
m = get_models()

st.subheader("Nhập thông tin sinh viên")
c1, c2 = st.columns(2)
with c1:
    age = st.number_input("Tuổi", 18, 24, 21)
    cgpa = st.slider("CGPA hiện tại", 1.0, 4.0, 3.0, 0.01)
    sleep = st.slider("Thời lượng ngủ (giờ/ngày)", 3.0, 12.0, 7.0, 0.1)
    study = st.slider("Thời gian học (giờ/ngày)", 0.0, 13.0, 4.5, 0.1)
with c2:
    social = st.slider("Mạng xã hội (giờ/ngày)", 0.0, 10.0, 3.5, 0.1)
    physical = st.slider("Hoạt động thể chất (thang số của bộ dữ liệu)", 0, 150, 75)
    stress = st.slider("Mức stress (2–10)", 1, 10, 4)
    extra = st.slider("Ngoại khóa (giờ/tuần, mô phỏng)", 1, 14, 8)

if st.button("Phân tích", type="primary"):
    r = predict(m, age, sleep, study, social, physical, stress, extra, cgpa)
    title, desc = CLUSTER_INFO[r["cluster"]]
    st.divider(); st.subheader("Kết quả")
    st.success(f"**Nhóm hồ sơ:** {title}"); st.caption(desc + ". Nhãn cụm do thuật toán tạo ra, không phải chẩn đoán.")
    a, b = st.columns(2)
    a.metric("CGPA dự đoán (Linear Regression)", f"{r['cgpa_pred']:.2f}", f"{r['cgpa_pred']-cgpa:+.2f} so với CGPA nhập")
    b.metric("Xác suất nhãn Depression = 1 (Logistic)", f"{r['depr_proba']*100:.1f}%")
    if r["depr_label"] == 1:
        st.warning("Mô hình gán nhãn 1 (cần quan tâm thêm). Precision của mô hình chỉ khoảng 11%, nên đây không phải kết luận.")
    else:
        st.info("Mô hình gán nhãn 0.")
    if stress >= 8:
        st.warning("Stress ≥ 8: trong dữ liệu, nhóm này có tỷ lệ nhãn Depression = 1 khoảng 42% (so với ~10% chung) – nên ưu tiên hỗ trợ.")
    st.caption("Mô hình huấn luyện với class_weight='balanced' nên xác suất cao hơn tỷ lệ thực (~10%). Mô hình yếu (AUC ≈ 0,55). Kết quả chỉ để minh họa quy trình đưa mô hình vào ứng dụng.")

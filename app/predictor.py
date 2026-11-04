"""Logic dự đoán tách khỏi giao diện để dễ kiểm thử."""
import joblib, pandas as pd
import os

CLUSTER_INFO = {
    0: ("Cụm 0 – Học tập tốt, lối sống cân bằng", "CGPA cao, học nhiều, dùng mạng xã hội ít, stress thấp"),
    1: ("Cụm 1 – Căng thẳng, ngủ ít, ít vận động", "Stress cao nhất, ngủ ít nhất, vận động thấp nhất"),
    2: ("Cụm 2 – Học ít, dùng mạng xã hội nhiều", "CGPA thấp nhất, học ít, mạng xã hội nhiều nhất"),
}

def load(path="models/student_models.pkl"):
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Build absolute path to the model file
    model_path = os.path.join(script_dir, path)
    return joblib.load(model_path)

def predict(m, age, sleep, study, social, physical, stress, extra, cgpa):
    sup = pd.DataFrame([[age, sleep, study, social, physical, stress, extra]], columns=m["sup_features"])
    clu = pd.DataFrame([[cgpa, sleep, study, social, physical, stress, extra]], columns=m["cluster_features"])
    cluster = int(m["kmeans"].predict(m["pca"].transform(m["scaler"].transform(clu)))[0])
    return {"cluster": cluster,
            "cgpa_pred": float(m["reg"].predict(sup)[0]),
            "depr_label": int(m["clf"].predict(sup)[0]),
            "depr_proba": float(m["clf"].predict_proba(sup)[0, 1])}

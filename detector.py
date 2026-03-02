import pickle

# Load trained model
with open("model/threat_model.pkl", "rb") as f:
    model = pickle.load(f)

def detect_threat(features):
    prediction = model.predict([features])
    return prediction[0]  # 1 = Threat, 0 = Safe

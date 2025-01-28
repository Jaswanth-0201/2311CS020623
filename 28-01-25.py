import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "customer_id": [1, 2, 3, 4, 5],
    "gender": ["male", "female", "male", "female", "male"],
    "subscription_status": ["active", "inactive", "active", "inactive", "active"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

label_encoder = LabelEncoder()
df["gender_encoded"] = label_encoder.fit_transform(df["gender"])

df["subscription_status_encoded"] = label_encoder.fit_transform(df["subscription_status"])

print("\nDataFrame after Label Encoding:")
print(df)
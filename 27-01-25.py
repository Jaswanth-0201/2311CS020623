import pandas as pd 
from sklearn.preprocessing import MinMaxScaler
data = {
    "age": [25,30,35,40,45],
    "height": [150,160,170,180,190],
    "weight": [50,60,70,80,90],
}

df = pd.DataFrame(data)

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
print(scaled_df)
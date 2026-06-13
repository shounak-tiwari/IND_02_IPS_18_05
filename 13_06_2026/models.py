# imports all library 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
from scipy import stats 
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,RobustScaler
from sklearn.model_selection import train_test_split

from parsefun import parse_sqft


# load datasets 
df = pd.read_csv(r"C:\Users\Akash\Desktop\02_IPS\13_06_2026\Bangalore  house data.csv")


# cleaning of string cols 
for x in ['society','location','area_type']:
    df[x] = df[x].str.replace(r"[^\w\s]","",regex=True).str.strip()

# total sqft 
df['total_sqft'] = df['total_sqft'].apply(parse_sqft)
df = df.drop(columns=['size'])
df['society'] = df.groupby("location")["society"].transform(
    lambda x : x.fillna(x.mode().iloc[0] if not x.mode().empty else np.nan)
)
df = df.dropna()
df = df.reset_index(drop=True)
print(df.shape)

number_for_outlier = ['total_sqft','price']

for x in number_for_outlier:
    z = np.abs(stats.zscore(df[x]))
    df = df[z <= 3]

le = LabelEncoder()
df['area_type'] = le.fit_transform(df['area_type'])

# low cardinality columns only  add more if 
# nunique < ~20

low_cardinality = ['availability']

ohe = OneHotEncoder(sparse_output=False,handle_unknown='ignore')

for cols in low_cardinality:
    if df[cols].nunique()<=20:
        encoded = ohe.fit_transform(df[[cols]])

        encoded_df = pd.DataFrame(
            encoded,columns=ohe.get_feature_names_out([cols]),
            index =df.index
        )

        df = pd.concat([df,encoded_df],axis=1)
        df = df.drop(columns=[cols])
    else:
        print("Skipped")
    

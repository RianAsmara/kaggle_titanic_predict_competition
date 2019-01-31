import pandas as pd

# Load Training Data [891]  & Testing Data [417]

train_data = pd.read_csv('Data/train.csv')
test_data = pd.read_csv('Data/test.csv')
all_data = (train_data, test_data)

# Feature 1 : Pclass

print(train_data[["Pclass", "Survived"]].groupby(["Pclass"], as_index=False).mean())
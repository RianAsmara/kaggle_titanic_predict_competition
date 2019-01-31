import pandas as pd

# Load Training Data [891]  & Testing Data [417]

train_data = pd.read_csv('Data/train.csv')
test_data = pd.read_csv('Data/test.csv')
all_data = (train_data, test_data)

# Feature 2 : Sex

print(train_data[["Sex", "Survived"]].groupby(["Sex"], as_index=False).mean())
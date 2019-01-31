import pandas as pd

# Load Training Data [891]  & Testing Data [417]

train_data = pd.read_csv('Data/train.csv')
test_data = pd.read_csv('Data/test.csv')
all_data = (train_data, test_data)

# Feature 3 : Family Size

for data in all_data:
    data['family_size'] = data['SibSp'] + data['Parch'] + 1
print(train_data[["family_size", "Survived"]].groupby(["family_size"], as_index=False).mean())

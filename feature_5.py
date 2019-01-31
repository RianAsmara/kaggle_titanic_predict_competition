import pandas as pd

# Load Training Data [891]  & Testing Data [417]

train_data = pd.read_csv('Data/train.csv')
test_data = pd.read_csv('Data/test.csv')
all_data = (train_data, test_data)

# Feature 5 : Fare

for data in all_data:
    data['Fare'] = data['Fare'].fillna(data['Fare'].median())
train_data['category_fare'] = pd.cut(train_data['Fare'], 4)
print(train_data[["category_fare", "Survived"]].groupby(["category_fare"], as_index=False).mean())



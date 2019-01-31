import pandas as pd

# Load Training Data [891]  & Testing Data [417]

train_data = pd.read_csv('Data/train.csv')
test_data = pd.read_csv('Data/test.csv')
all_data = (train_data, test_data)

# Feature 4 : Embarked

for data in all_data:
    data['Embarked'] = data['Embarked'].fillna('S')
print(train_data[["Embarked", "Survived"]].groupby(["Embarked"], as_index=False).mean())



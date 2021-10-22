print('Tesla offers four car models: Model S, Model X, Model 3, and Model Y')
print('I would always go for Model Y because of uniqueness')
import pandas as pd
url = "https://raw.githubusercontent.com/isu-abe/516x/master/data/surveys1977.csv"
data = pd.read_csv(url, sep =',', index_col=0)
data.head()
data.describe()
print(data.describe())

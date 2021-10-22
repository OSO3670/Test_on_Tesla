import pandas as pd
import sys

file_to_open = open(sys.argv[1], 'r')
#url = "https://raw.githubusercontent.com/isu-abe/516x/master/data/surveys1977.csv"
data = pd.read_csv(url, sep =',', index_col=0)
print(data.describe())

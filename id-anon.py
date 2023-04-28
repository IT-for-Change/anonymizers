import random
import pandas as pd

#The file is not really a CSV, it is a list of codes, one per row. No header
df = pd.read_csv('id.csv',header=None)

#We only need non n/a rows
rows = len(df.index) 

digits = len(str(rows))
range_lower = pow(10,digits)
range_upper = range_lower + rows

codes = list(range(range_lower, range_upper))
random.shuffle(codes)

df.columns = ['ORIGINAL_ID']
df['ANONYMIZED_ID'] = codes
df.to_csv('id-anon.csv',index=False)

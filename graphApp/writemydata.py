import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/ss/Desktop/GraphQL/graphProj/db.sqlite3')
df = pd.read_csv('/Users/ss/Desktop/GraphQL/sam.csv')
df['id']=df.index
df=df[['id', 'Segment', 'Country', 'Product', 'Units', 'Sales', 'Datesold']]
df.to_sql('graphApp_productmodel', conn, if_exists='replace', index=False)

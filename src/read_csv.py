import pandas as pd
import numpy as np
import json
import requests


class MergeData():
    def __init__(self):

        url = "https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/python-software-developer/products.json"
        response = requests.get(url)
        json_string = json.loads(response.text)
        df1 = pd.DataFrame(json_string)

        df2 = pd.read_csv('products.csv', index_col=None, header=0, low_memory=False, keep_default_na=False)
        df2.columns = ['id', 'name', 'brand', 'retailer', 'price', 'in_stock']
        df = pd.concat([df1, df2], ignore_index=True)
        df['id'] = df.id.astype('str')
        self.df = df

    def get_id(self, id):
        row = self.df.loc[self.df['id'] == id]
        if row.empty:
            return 'Error 404 ID not found'
        else:
            row = row.replace('"', '', regex=True)
            row = row.replace(' ', '', regex=True)
            if row.iloc[0]['in_stock'].startswith("y"):
                row['in_stock'] = True
            elif row.iloc[0]['in_stock'].startswith("n"):
                row['in_stock'] = False
            row = row.replace("", np.nan, regex=True)
            if row.iloc[0]['price'] != None:
                row['price'] = row ['price'].astype(float)
            json_output = json.loads(row.to_json(orient='records'))
            return json.dumps(json_output, indent=2, sort_keys=True)









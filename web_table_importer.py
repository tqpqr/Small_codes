import requests
import re
import pandas as pd

url='http://web_page_with_tables.com'

dfs = pd.read_html(url)

#print(dfs)
g=1
for tabl in dfs:

    tabl.to_csv("C:/Tables/" + str(g) + ".csv")
    g=g+1

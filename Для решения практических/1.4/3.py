import pandas as pd
dfs = pd.read_html('https://stepik.org/media/attachments/lesson/209723/3.html')
print(dfs[0])

# print(dfs[0].values.sum())
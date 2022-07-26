import pandas as pd

data = [["Chet", 33],["Teju", 32],["Lucy",5]]

df = pd.DataFrame(data, columns=['Name', 'Age'])

print(df)
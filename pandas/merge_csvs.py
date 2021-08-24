from datetime import datetime

import pandas as pd

start = datetime.now()

# reading two csv files
data1 = pd.read_csv('ARQUIVO_AQUI.csv')
data2 = pd.read_csv('ARQUIVO_AQUI.csv')
data3 = pd.read_csv('ARQUIVO_AQUI.csv')
data4 = pd.read_csv('ARQUIVO_AQUI.csv')

output1 = pd.merge(data1, data2,
                   on='i_databases',
                   how='inner') \
    .merge(data3) \
    .merge(data4)

output1.to_csv('OUTPUT_PANDAS.csv', index=False)

end = datetime.now()
time_elapsed = end - start
print(f'Time Elapsed: {time_elapsed}')

import pandas as pd

df = pd.read_csv('real-time.csv')
df_pivot = df.pivot(index=['station','state','city','last_update'], columns='pollutant_id', values='pollutant_avg')
df_pivot = df_pivot.reset_index()
df_pivot = df_pivot.rename_axis(None, axis=1)
df_pivot = df_pivot.rename(columns={'last_update':'From Date', 'OZONE':'Ozone'})
df_pivot = df_pivot[df_pivot.columns[3:]]
df_pivot['From Date'][0] = df_pivot['From Date'][0][:-3]

Thist = pd.read_csv('historic_data.csv')
Thist = pd.concat([Thist,df_pivot])

Thist.to_csv('historic_data.csv',index=False)

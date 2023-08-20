import pandas as pd

def clean_df(filename, savename):
    try:
        history = pd.read_excel(filename)
    except:
        history = pd.read_csv(filename)
    Thist = history.iloc[16:].T.set_index(history[15:16].values[0])
    Thist = Thist.T
    Thist.to_csv(savename, index=False)

filename = 'site_15720230820215101.xlsx'
savename = 'historic_data.csv'

df = clean_df(filename, savename)


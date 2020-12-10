from pathlib import Path
import pandas as pd


RAWDATA_PATH = Path('data/raw')
CLEANDATA_PATH = Path('data/clean')
df = pd.read_csv(RAWDATA_PATH / "T_Bouhafs_mentions.csv")

df['reply_to'] = [list(eval(el)) if el != '[]' else '' for el in df['reply_to']]
df['reply_to'] = ['|'.join([el[i]['screen_name'] if el != '' else ''
                   for i in range(len(el))])
                  for el in df['reply_to']]

df['mentions'] = [list(eval(el)) if el != '[]' else '' for el in df['mentions']]
print(df['mentions'])
df['mentions'] = ['|'.join([el[i]['screen_name'] if el != '' else ''
                   for i in range(len(el))])
                  for el in df['mentions']]
# dict1 = ast.literal_eval(strip_results[0]+'}')
df = df.drop(columns=['id', 'conversation_id', 'user_id', 'photos', 'urls', 'video',
                      'thumbnail', 'near', 'geo', 'source', 'user_rt_id', 'user_rt',
                      'retweet_date', 'translate', 'trans_src', 'trans_dest'])
df.to_csv(CLEANDATA_PATH / "clean.csv", index=False)

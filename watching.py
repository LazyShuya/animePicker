import pandas as pd 


def new_watching(link_reference, episode_no):
    d = {'ref_link':link_reference, 'episode':episode_no}
    df = pd.DataFrame(data=d, index = [0])
    print(df)
    df.to_csv('watching_list.csv', index=False)



def update_episode(episode_no):
    df = pd.read_csv('watching_list.csv')
    df.at[0,'episode'] = episode_no
    df.to_csv('watching_list.csv',encoding='utf-8', index=False)


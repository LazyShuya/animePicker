import pandas as pd 

def coninue_left():
    df = pd.read_csv('watching_list.csv')
    ref = df.ref_link[0] + str(df.episode[0])
    
    return ref



def new_watching(link_reference, episode_no):
    d = {'ref_link':link_reference, 'episode':episode_no}
    df = pd.DataFrame(data=d, index = [0])
    df.to_csv('watching_list.csv', index=False)



def update_episode(episode_no):
    df = pd.read_csv('watching_list.csv')
    df.at[0,'episode'] = episode_no
    df.to_csv('watching_list.csv',encoding='utf-8', index=False)

# coninue_left()
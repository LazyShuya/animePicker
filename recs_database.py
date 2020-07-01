import pandas as pd
def add_recs(anime_name, anime_list = []):
    #opening file
    df_recs = pd.read_csv('test.csv')
    df_anime = pd.read_csv('watchedA.csv')
    if anime_name not in list(df_anime.anime):
        for anime in anime_list:
            if anime not in list(df_recs.recs):
                if anime not in list(df_anime.anime):
                    df = df.append({'anime':anime_name, 'recs':anime},ignore_index=True)
            else:
                df_recs.loc[df_recs.anime_recs==anime, 'counter'] += 1
        
    df_recs.to_csv('test.csv', sep=',',encoding='utf-8', index=False)
    df_anime.to_csv('watchedA.csv', sep=',',encoding='utf-8', index=False)


def update():
    df_recs = pd.read_csv('test.csv')
    df_anime = pd.read_csv('watchedA.csv')
    df_recs = df_recs.set_index('anime')
    for anime in df_anime.anime:
        if anime in df_recs.index:
            df_recs = df_recs.drop([anime])
    df_recs.to_csv('test.csv', sep=',',encoding='utf-8', index=False)
    df_anime.to_csv('watchedA.csv', sep=',',encoding='utf-8', index=False)



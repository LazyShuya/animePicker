import pandas as pd


# # df = pd.read_csv('test.csv')

# def check_anime(anime_name):
#     for Anime in df.anime.unique():
#         if Anime == anime_name:
#             return True
#     return False


#Adding data into database:
def add_recs(anime_name, anime_list = []):
    df_recs = pd.read_csv('test.csv')
    df_anime = pd.read_csv('watchedA.csv')
    if anime_name not in list(df_anime.anime):
        df_anime = df_anime.append({'anime':anime_name}, ignore_index= True)
        for anime in anime_list:
            if anime not in list(df_recs.anime_recs):
                df_recs = df_recs.append({'anime_recs':anime, 'counter' : 0},ignore_index=True)
            else:
                df_recs.loc[df_recs.anime_recs==anime, 'counter'] += 1
        df_recs.drop(df_recs.filter(regex="Unname"),axis=1, inplace=True)
        df_anime.drop(df_anime.filter(regex="Unname"),axis=1, inplace=True)

        df_recs.to_csv('test.csv', sep=',',encoding='utf-8', index=False)
        df_anime.to_csv('watchedA.csv', sep=',',encoding='utf-8', index=False)
        print('record added')
    else:
        print('already exists')


def update():
   df_recs = pd.read_csv('test.csv')
   df_anime = pd.read_csv('watchedA.csv')
   for anime in list(df_anime.anime):
       if anime in list(df_recs.anime_recs):
           df_recs.drop(df_recs[df_recs.anime_recs == anime].index, inplace = True)
   df_recs.drop(df_recs.filter(regex="Unname"),axis=1, inplace=True)
   df_recs.to_csv('test.csv', sep=',',encoding='utf-8', index=False)
   df_anime.drop(df_anime.filter(regex="Unname"),axis=1, inplace=True)
   df_anime.to_csv('watchedA.csv', sep=',',encoding='utf-8', index=False)



#     return
# class Recommend:
#     def __init__(self, web_link, anime_name):
#         self.recs = []
#         self.anime = anime_name
#         self.d_main = pd.read_csv('test.csv')

#     def D_Base(self, list_names):
#         for name in list_names:
#             df2 = {"anime":self.anime, "recs":name}
#             frame = pd.DataFrame([df2])
#             self.d_main = self.d_main.append(frame, ignore_index=True)
        
#         self.d_main.drop(self.d_main.filter(regex="Unname"),axis=1, inplace=True)
#         self.d_main.to_csv('test.csv')

#     def Find_Recs(self):
#         self.stuff = self.soup.find_all(style="margin-bottom: 2px;")
#         for text in self.stuff:
#             self.recs.append(text.find('strong').get_text())
#         self.D_Base(self.recs)

# con = Recommend('https://myanimelist.net/anime/11843/Danshi_Koukousei_no_Nichijou/userrecs', 'Danshi Koukousei no Nichijou')
# df = con.cbase()
# print(df.anime.unique())

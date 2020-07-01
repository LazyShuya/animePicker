import pandas as pd
def add_recs(anime_name, anime_list = []):
    #opening file
    df = pd.read_csv('test.csv')
    if anime_name not in list(df.anime):
        for anime in anime_list:
            if anime not in list(df.recs):
                df = df.append({'anime':anime_name, 'recs':anime},ignore_index=True)
        
    df.to_csv('test.csv', sep=',',encoding='utf-8', index=False)



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

import regex
import pandas as pd


df = pd.read_csv('test.csv')

def check_anime(anime_name):
    for Anime in df.anime.unique():
        if Anime == anime_name:
            return True
    return False


#Adding data into database:
def add_recs(anime_name, anime_list = []):
    global df
    if check_anime(anime_name) == False:
        for anime in anime_list:
            df2 = {"anime":anime_name, "recs":anime}
            frame = pd.DataFrame([df2])
            df = df.append(frame, ignore_index= True)  
        df.drop(df.filter(regex="Unname"),axis=1, inplace=True)
        df.to_csv('test.csv')
        print('record added')
    else:
        print('already exists')

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

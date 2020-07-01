import pandas as pd
import random
import regex
import numpy as np


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


list_for_cache = []

def update():
   df_recs = pd.read_csv('test.csv')
   df_anime = pd.read_csv('watchedA.csv')
   for anime in list(df_anime.anime):
       if anime in list(df_recs.anime_recs):
           df_recs.drop(df_recs[df_recs.anime_recs == anime].index, inplace = True)
   
   df_recs = df_recs.sort_values(by= 'counter', ascending = False)        
   df_recs.drop(df_recs.filter(regex="Unname"),axis=1, inplace=True)
   df_recs.to_csv('test.csv', sep=',',encoding='utf-8', index=False)
   df_anime.drop(df_anime.filter(regex="Unname"),axis=1, inplace=True)
   df_anime.to_csv('watchedA.csv', sep=',',encoding='utf-8', index=False)


def picker(anim_list):
    display = {
        1: anim_list[0],
        2: anim_list[1],
        3: anim_list[2],
        4: anim_list[3],
        5: anim_list[4],
        6: anim_list[5],
        7: anim_list[6],
        8: anim_list[7],
        9: anim_list[8],
        10: anim_list[9],
        11: "Shuffle again",
    }
    for i in range(1,12):
        print(f'{i}) {display[i]}')
    x = int(input("enter your choice: "))
    print("")
    if x<=10 and x>=1 :
        return display[x]
    elif x==11:
        return False
    else:
        print("pleas choose again!!!!")
        picker(anim_list)

def random_function():
    df_recs = pd.read_csv('test.csv')
    df = (df_recs.head(200))
    
    while True:
        for prev_choices in list_for_cache:
            if prev_choices in list(df.anime_recs):
                df = df.drop(df[df.anime_recs==prev])
        anime_list = list(df.anime_recs)
        anime_to_display = random.sample(anime_list, 10)
        choice = picker(anime_to_display)
        if choice is not False:
            return choice
        else:
            list_for_cache.append(anime_to_display)



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

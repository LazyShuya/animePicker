from recs_database import add_recs, update, random_function, update_episode_last,check_completion
import scraper
from watching import new_watching, update_episode, coninue_left 
from mainstuff import MyAnimeList as MAL
from time import sleep


#initialize :
page = MAL()


#redirect to the episode you last watched
def continue_leftoff():
    link = coninue_left()
    page.continue_where_left(link)
    


#get recommendations
def Get_NewAnime():
    search = page.Search(random_function())
    anime_list = scraper.get_recs(search[0])
    first_episode = page.redirect()
    add_recs(first_episode[0], search[1], anime_list)
    new_watching(first_episode[1],first_episode[2])


#exit current session
def exit_app():
    episode = page.exit_program()
    update_episode(episode)
    update_episode_last(episode)


def main():
    print("Your Anime Helper")
    
    print("would you like to :")
    print('1) Continue where you left off?')
    print('2) get a new recommendation')
    print('3) exit')
    x = input("choose your option: ")
    print('')
    while True:
        if x == '1':
            continue_leftoff()
            break
        elif x == '2' :
            if check_completion(0) == True:
                Get_NewAnime()
            else:
                print('complete your previous anime!')
                continue_leftoff()
            break
        elif x=='3':
            print("Sayonara...")
            page.simple_exit()
            break
        else:
            print('wrong option please choose again\n')
    sleep(80)
    print('what do you want to do now?')
    while True:
        if x=='3':
            break
        
        print('1) want a new anime')
        print('2) exit')
        y = input("choose your option: ")
        if y=='1':
            print('')
            print('did you complete your previous anime?')
            print('if not, I will find you and then slap you!')
            print('')
            sleep(2)
            ep = page.current_episode()
            update_episode(ep)
            if check_completion(ep) != True:
                print('complete what you were watching first and then come here!')
                
            else:
                print('you have completed watching the previous one, GOOD!\n')
                Get_NewAnime()
                sleep(60)
        elif y=='2':
            print('sayonara...')
            exit_app()
            break
        else:
            print ('please choose the correct option, or are you blind!\n')


main()
        
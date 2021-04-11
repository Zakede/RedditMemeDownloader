from praw.models.listing.mixins import subreddit
from praw.reddit import Submission
import requests, wget, os
import praw

#Your Reddit APP Credentials, You can create/get them from here https://www.reddit.com/prefs/apps.
reddit = praw.Reddit(client_id = "Your Client ID", client_secret = "Your Client's Secret", user_agent = "Put Anything Here It Really Doesn't Matter")

def main():
    subs_final = []
    items = []
    #Gets all subreddits in the text file and append them in list.
    try:
        with open("subs.txt", "r") as file:
            subs = file.readlines() #Reads all the lines from the subs.txt which contains all the subreddits you'll add.
            subs_final = [x[:-1] for x in subs] #Removes \n string from all the results.
    except FileNotFoundError:
        print("Subs File Not Found, Please make sure you have made 'subs.txt' file with all subreddit names you need.")

    #Gets all the posts from the subreddit provided in the text file and appends them in a list.
    for i in range(len(subs_final)):
        subreddit = reddit.subreddit(f"{subs_final[i]}")
        for submissions in subreddit.hot(limit=40):
            items.append(submissions.url)

    # Using Requests To Download Files. (I Prefer To Use Requests Over Wget.)
    for i in range(len(items)):
        links = requests.get(items[i])
        try:
            with open(("Image"+str(i)+".jpg"), "wb") as f: #Most Images of Reddit are saved in .jpg
                f.write(links.content)
        except requests.ConnectionError:
            continue
    
    #Using Wget To Download All The Files. (You can use Wget if you're trying to make a quick downloading program.)
    # for i in list(items):
    #     try:
    #         wget.download(i, os.getcwd())
    #     except Exception as e:
    #         continue

    print(items)

if __name__ == "__main__":
    main()
import instaloader
import time
import csv
import pandas as pd
from datetime import datetime, timedelta

# create an instance of Instaloader class
loader = instaloader.Instaloader()

# specify the username of the user whose posts you want to scrape
username = "colorstv"

# specify the start date for the time period you want to scrape
current_time = datetime.utcnow()
# current_time = datetime(2022,6,15,0,0,0,0)
# specify the starting time and current time difference
start_time = current_time - timedelta(hours=3, minutes=5)
# print(start_time)
# get the user's profile
profile = instaloader.Profile.from_username(loader.context, username)

# hashtag = "hindi"
hashtags_set = set(["colors", "hindi", "Colors"])

cnt = 0
req_links = []

for post in profile.get_posts():
    cnt += 1
    # print(hashtags_set.intersection(set(post.caption_hashtags)))
    # print(post.caption_hashtags)
    # print(post.caption)
    if post.date_utc >= start_time and len(hashtags_set.intersection(set(post.caption_hashtags))) > 0:
        # print(post.caption)
        link = "https://www.instagram.com/p/" + str(post.shortcode) + "/"
        print("Post URL: ", link)
        req_links.append(link)

    if cnt % 10 == 0:
        # time.sleep(15)
        break
    # print(cnt)
print(req_links)

filename = "links"
with open(filename+".csv", 'a') as filedata:
    csv_writer = csv.writer(filedata)
    csv_writer.writerow(['links'])
    for link in req_links:
        # print(link)
        csv_writer.writerow([link])

import requests
from bs4 import BeautifulSoup
import pandas as pd

def getFollowers(username):
    followers_url = f"https://github.com/{username}?tab=followers"

    followers_page = requests.get(followers_url)

    followers_source = BeautifulSoup(followers_page.content,"html.parser")

    followers_list = [i.text for i in followers_source.find_all("span",attrs={"class":"Link--secondary pl-1"})]

    return followers_list


def getFollowing(username):
    following_url = f"https://github.com/{username}?tab=following"

    following_page = requests.get(following_url)

    following_source = BeautifulSoup(following_page.content,"html.parser")

    following_list = [i.text for i in following_source.find_all("span",attrs={"class":"Link--secondary pl-1"})]
    
    return following_list
    
def main(followers_list, following_list):
    ff = set(followers_list).difference(set(following_list))
    fl = set(following_list).difference(set(followers_list))
    
    return ff, fl
    
username = input("Enter Username: ")

followers = getFollowers(username)
following = getFollowing(username)

print("Takip Etmediklerin", main(followers, following)[0])
print("Seni Takip Etmeyenler",main(followers, following)[1])
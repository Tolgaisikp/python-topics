#1. cli olarak çalıştırılıcak o yüzden param almaya bakıcam.
#2. fonksiyon yapısı veya class yapısı oluştur.
import argparse
import numpy as np
from functions import get_manga_chapters, get_manga_pages, download_data, get_manga_pdf

parser = argparse.ArgumentParser()
parser.add_argument("-an", "--anime_name")
parser.add_argument("-e", "--episode", default=False, type=int)
parser.add_argument("-fe", "--final_episode", default=False, type=int)

args = parser.parse_args()

anime_name = args.anime_name.lower()
episode = args.episode
final_episode = args.final_episode

if not final_episode:
    final_episode = episode

berserk_chapters = list(reversed(get_manga_chapters(anime_name)))

if episode:
    for episode in berserk_chapters[episode-1:final_episode]:
        manga_pages_list = get_manga_pages(episode)
        download_data(manga_pages_list)
        get_manga_pdf(episode.split('/')[-2])
else:
    for episode in berserk_chapters:
        manga_pages_list = get_manga_pages(episode)
        download_data(manga_pages_list)
        get_manga_pdf(episode.split('/')[-2])
        print(episode.split('/')[-2], "Download")

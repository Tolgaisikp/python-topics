import requests
import cssutils
from bs4 import BeautifulSoup
import os
from glob import glob
from PIL import Image

#tortuga, mangaşehri gibi seçenekler sunulucak

def get_manga_chapters(name):
    url = f"https://tortuga-ceviri.com/manga/{name}/ajax/chapters/"
    
    req = requests.post(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    
    listing_chapters = soup.find('ul', {'class':'main version-chap no-volumn'})
    
    chapters = [i.find('a')['href'] for i in listing_chapters.find_all('li',{"class":"wp-manga-chapter"})]
    return chapters

def get_manga_pages(chapter):
    url = chapter
    
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    
    reading_content = soup.find('div', {'class':'reading-content'})
    pages = reading_content.find_all('div', {'class':'page-break no-gaps'})
    
    manga = [page.find('img')['src'].strip() for page in pages]
    return manga

def resize_by_percentage(image, percentage = 1.1789600967351874):
    width, height = image.size
    resized_dimensions = (int(width * percentage), int(height * percentage))
    resized = image.resize((827,1200))
    return resized

def remove_dir_file(dir_path):
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            os.rmdir(file_path)
            
def download_data(manga):
    for i, url in enumerate(manga):
        response = requests.get(url)
        file_name = f"image{i}.jpg"  # her resim için benzersiz bir dosya adı oluştur
        folder_path = "images"  # resimleri indireceğiniz klasörün yolu
        os.makedirs(folder_path, exist_ok=True)  # klasörü oluştur (eğer yoksa)
        file_path = os.path.join(folder_path, file_name)  # resmin dosya yolu
        with open(file_path, "wb") as f:
            f.write(response.content)
            
def get_manga_pdf(manga_chapter):
    page_list = glob('./images/*.jpg')
    folder_path = "images"  # resimleri indireceğiniz klasörün yolu
    os.makedirs("pdf", exist_ok=True)

    rgb_images = []
    for page in page_list:
        image = Image.open(page)    
        im_rgb = image.convert('RGB')
        
        width, height = im_rgb.size
        if width > height:
            left_half = im_rgb.crop((0, 0, width // 2, height))
            right_half = im_rgb.crop((width // 2, 0, width, height))
            rgb_images.extend([resize_by_percentage(left_half), resize_by_percentage(right_half)])
        else:
            rgb_images.append(resize_by_percentage(im_rgb))
            
    rgb_images[0].save(f'./pdf/{manga_chapter}.pdf', save_all=True, append_images=rgb_images[1:])

    remove_dir_file("images")
    os.rmdir("images")
import requests
import BeautifulSoup
import urlparse



def image_dem(url):
    images = []
    result = requests.get(url)
    soup = BeautifulSoup.BeautifulSoup(result.text)
    og_image = (soup.find('meta', property='og:image') or
                        soup.find('meta', attrs={'name': 'og:image'}))
    if og_image and og_image['content']:
        images.append(og_image['content'])
    
    thumbnail_spec = soup.find('link', rel='image_src')
    if thumbnail_spec and thumbnail_spec['href']:
        images.append(thumbnail_spec['href'])
        
    for img in soup.findAll("img", src=True):
       if "sprite" not in img["src"]:
           images.append(img["src"])
    return images
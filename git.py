import requests
from bs4 import BeautifulSoup
import json

users = ['gimnakatugampala','AmirhoseinHesami','MOCO-MAKO','aryashah2k','webpointdev','morrisbmm','kroitor','josuakrick']


for user in users:
    response = requests.get(f'https://github.com/{user}')
    soup = BeautifulSoup(response.text,'html.parser')

    # Images
    images = soup.find(class_='avatar avatar-user width-full border color-bg-primary')['src']

    # Name
    name = soup.find(attrs={"itemprop":"name"}).get_text()

    # # Username
    username = soup.find(attrs={"itemprop":"additionalName"}).get_text()

    # Bio
    bio = soup.find(class_='p-note user-profile-bio mb-3 js-user-profile-bio f4').get_text()

    # # Followers
    followers = soup.find(class_='octicon octicon-people').find_next_sibling().get_text()

    # # Following
    followering = soup.find(attrs={"href":f"https://github.com/{user}?tab=following"}).get_text().replace('following','')

    # Stars
    stars = soup.find(attrs={"href":f"https://github.com/{user}?tab=stars"}).get_text()

    # Repo Number
    reponumber = soup.find(attrs={"href":f"/{user}?tab=repositories"}).get_text().replace('Repositories','')


    # Contibutions
    contributions = soup.find(class_='f4 text-normal mb-2').get_text()

    details ={
        'image':images.replace('\n','').strip(),
        'name':name.replace('\n','').strip(),
        'username':username.replace('\n','').strip(),
        'bio':bio.replace('\n','').strip(),
        'followers':followers.replace('\n','').strip(),
        'followering':followering.replace('\n','').strip(),
        'stars':stars.replace('\n','').strip(),
        'reponumber':reponumber.replace('\n','').strip(),
        'contributions':contributions.replace('\n','').strip()
    }

    print(details)


    with open('data.json', 'a') as outfile:
        json.dump(details, outfile)
    
    # # Location
    # print(soup.find(attrs={"itemprop":"homeLocation"}).find('span').get_text())

    # # Twitter
    # print(soup.find(attrs={"rel":"nofollow me"}).get_text())







# soup.select('a[href]')
    


# print(soup.body)
# print(soup.find('span').get_text())

# for item in soup('span'):
#     print(item.get_text())
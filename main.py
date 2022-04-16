import textwrap
from time import sleep
from random import randint
import tweepy
from PIL import Image, ImageFont, ImageDraw
import requests
import json
print('*-' * 12)
print("Starting")
print('*-' * 12)
all_keys = open('TwitterKeys.txt', 'r').read().splitlines()
apikey = all_keys[0]
api_key_secret = all_keys[1]
acess_token = all_keys[2]
acess_token_secret = all_keys[3]
print(apikey)
print(api_key_secret)
print(acess_token)
print(acess_token_secret)

authent = tweepy.OAuthHandler(apikey, api_key_secret)

authent.set_access_token(acess_token, acess_token_secret)
api = tweepy.API(authent, wait_on_rate_limit=True)







def allofit():
    imgresp = requests.get("https://source.unsplash.com/random/landscape/?nature")

    file = open("bgimage.png", "wb")
    file.write(imgresp.content)
    file.close()

    response = requests.get('https://programming-quotes-api.herokuapp.com/quotes/random')
    image = Image.open("bgimage.png")

    print("Getting Image and Quote")
    idk = response.json()

    print(f'Quote is “{idk["en"]}”')
    fontsize = 80
    img_fraction = 0.50

    title = f'"{idk["en"]}"'
    font = ImageFont.FreeTypeFont('lmfont.otf', fontsize)
    editImage = ImageDraw.Draw(image)

    while font.getsize(title)[0] < img_fraction*image.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.FreeTypeFont('lmfont.otf', fontsize)

    fontsize -= 1
    font = ImageFont.FreeTypeFont('lmfont.otf', fontsize)

    title = textwrap.fill(text=title, width=20)

    fillcolor = "black"

    randomnumber = randint(0, 1)

    if randomnumber == 0:
        fillcolor = "black"
        print("Its going black")
    else:
        fillcolor = "white"
        print("Its going white")
    print(title)
    editImage.text((20, 55), title, fill=fillcolor, font=font)

    image.save("result.jpg")

    result = open('result.jpg')

    api.update_status_with_media('A wild quote appeared!', "result.jpg")


while True:
    allofit()
    sleep(4680)


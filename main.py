import requests
from PIL import Image
import imageio
import glob
import shutil
import os
from time import sleep
clearConsole = lambda: print('\n' * 150)
clearConsole()
ammount = int(input("How many frames do you want? 100 is a good number: "))
collection = input("What is the link of the opensea collection: ").split("/")[4]
print("Starting")
sleep(1)
clearConsole = lambda: print('\n' * 150)
clearConsole()
dirname = os.path.dirname(__file__)
if not os.path.exists(os.path.join(dirname, 'data')):
    os.makedirs(os.path.join(dirname, 'data'))
if os.path.exists(os.path.join(dirname, 'final.gif')):
    os.remove(os.path.join(dirname, 'final.gif'))
if os.path.exists(os.path.join(dirname, 'almostdone.gif')):
    os.remove(os.path.join(dirname, 'almostdone.gif'))
if os.path.exists(os.path.join(dirname, 'data')):
    shutil.rmtree(os.path.join(dirname, 'data'))
os.mkdir(os.path.join(dirname, 'data'))
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36', 
    'Accept-Language': 'en-US,en;q=0.8'
}
x = 1
with requests.session() as s:
    for i in range(0, int(ammount / 50)):
        querystring = {"order_direction":"asc",
                    "offset":i*50,
                    "order_by":"pk",
                    "collection":collection,
                    "limit":"50"}
        r = s.get("https://api.opensea.io/api/v1/assets", params=querystring, headers=headers)
        rjson = r.json()
        for j in range(0, len(rjson["assets"])):
            img_data = s.get(rjson["assets"][j]["image_url"]).content
            with open(f'data/{x}.png', 'wb') as handler:
                handler.write(img_data)
            x = x + 1
            print(f"{x - 1}/{ammount}")
frames = []
imgs = glob.glob("data/*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
frames[0].save('almostdone.gif',
               save_all=True,
               append_images=frames[1:],
               duration=ammount,
               loop=0,)

gif_original = 'almostdone.gif'
gif_speed_up = 'final.gif'

gif = imageio.mimread(gif_original)

imageio.mimsave(gif_speed_up, gif, fps=60)
os.remove(os.path.join(dirname, 'almostdone.gif'))
print("Done!")
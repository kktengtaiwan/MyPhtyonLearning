import requests, os

from urllib.request import urlretrieve

from bs4 import BeautifulSoup

frameurl = 'http://www.ghibli.jp/info/013344/'
html = requests.get(frameurl)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text, 'lxml')

html = requests.get(frameurl)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text, 'lxml')

frame_list=sp.find_all('a',class_="panelarea")
  
for frame in frame_list:
    frame_pos=str.find(frame["href"],"frame")
    frame_dir="d:\\python\\imgdownload\\"+frame["href"][27:frame_pos-2]
    if not os.path.exists(frame_dir):
        os.mkdir(frame_dir)

    jpg_path=frame_dir+"\\"

    html = requests.get(frame["href"])
    html.encoding = 'UTF-8'
    sp = BeautifulSoup(html.text, 'lxml')
    jpg_list=sp.find_all('a',class_="panelarea")

    file_index=1
    for jpg in jpg_list:
        jpg_filename=jpg_path+str(file_index)+".jpg"
        print(jpg_filename)
        urlretrieve(jpg["href"],jpg_filename)
        print('第',file_index,'張下載完成!')
        file_index+=1   

    print("===================================")
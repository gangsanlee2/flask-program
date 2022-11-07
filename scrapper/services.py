from urllib.request import urlopen

from bs4 import BeautifulSoup

from scrapper import MusicRanking


def BugsMusic(arg):
    arg = MusicRanking()
    soup = BeautifulSoup(urlopen(arg.domain+arg.query_string), 'lxml')
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    # 디버깅
    _ = 0
    for i, j in zip(titles, artists):
        _ += 1
        print(f"{_}위 {i.find('a').text} - {j.find('a').text}")

    #dictionary 로 변환
    for i in range(0, len(titles)):    # len = length
        arg.dic[arg.titles[i]] = arg.artists[i] # keys=titles, values=artists

    # csv 파일로 저장
    arg.dict_to_dataframe()
    arg.dataframe_to_csv()
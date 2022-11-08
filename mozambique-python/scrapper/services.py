from urllib.request import urlopen
from bs4 import BeautifulSoup

def BugsMusic(arg):
    soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), 'lxml')
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i}위 {j} : {k}") # 디버깅
     for i, j, k in zip(range(1, len(titles)), titles, artists)]
    ####################아래쪽은 어떤 크롤링에서도 똑같음
    diction = {} # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]

    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv() # csv파일로 저장
if __name__ == '__main__':
    a =BugsMusic(arg)
    print(titles)
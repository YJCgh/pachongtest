from urllib import request
from bs4 import BeautifulSoup

#获取html,它可以接收一个url的参数
def get_html(url):
    header = {
        #"Host": 'www.douban.com',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}

    req = request.Request(url,headers=header)
    response=request.urlopen(req)

    if response.getcode() == 200:
        html = response.read().decode()
        return html




#分析html
def parser_html(html):
    soup=BeautifulSoup(html,'lxml')
    title=soup.select('title')[0].text
    div=soup.select('li div.hd')
    inq = soup.select('p.quote span.inq')
    info=soup.select('.info div.bd')
    imgs=soup.select('div.pic a img')
    #print(len(inq))
    data=[]
    for i in range(len(div)):
        data.append(div[i].select('span.title')[0].text+
              inq[i].text+
              ' '.join(str(info[i].text).split())+
              #split 用空格隔开
              imgs[i].get('src')
        )
    # for i in div:
    #     name=i.select('span.title')[0].text
        #print(name)
    return data

#保存数据
def save_data(data):
    #链接到数据库在这个部分进行
    f=open('豆瓣.txt','a',encoding='utf-8')
    for i in data:
        f.write(i+'\n')
    f.close()


def main(url):
    # url='https://movie.douban.com/top250?start=0&filter='
    html=get_html(url)
    #print(html)
    data=parser_html(html)
    save_data(data)
    #print(data)

#在每个模块中都有一个这样的属性，直接运行这个模块
if __name__ == '__main__':
    for i in range(10):
        print(f'开始爬取第{i+1}页')
        start = i * 25
        url = f'https://movie.douban.com/top250?start={start}&filter='
    main(url)
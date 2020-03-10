____________

关于url的参数

是在你想下载的漫画页面中 F12->NETWORK
中随便找一张漫画中的图的URL里截取部分。
例如 http://mhua.zerobyw4.com/manhua/S9na9im6o/23/93.jpg
    截取http://mhua.zerobyw4.com/manhua/S9na9im6o/
————————————
from lxml import etree
import requests
from selenium import webdriver
from threading import Thread


def request_url(hua):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    p = 1
    while p: 
        
        if p < 10: 
            pag = '0'+str(p)
        elif p == 200:
            break
        else :
            pag = str(p)
        purl = url+str(hua)+'/'+pag+'.jpg'
        print('正在下载'+purl)
        # driver.get(purl)
        # html = driver.page_source
        # dom = etree.HTML(html)
        # content = dom.xpath("//img[contains(@src,'jpg')]/@src")
        # if not content:
        #     return
    
        content.append(purl)
        p = p+1
    return content

def download(content,address,hua):
    p = 1
    for page in content:
        r = requests.get(page,headers=headers)

        if r.status_code ==200:
            with open(address+'\%d-%d.jpg'%(hua,p),'wb') as f:
                f.write(r.content)
                f.close()
                p = p+1
        else:
            print("下载失败")
            


if __name__ == "__main__":
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
,'Host': 'mhua.zerobyw4.com'}
    url  =input("链接 例如 http://mhua.zerobyw4.com/manhua/S9na9im6o/ ：")
    huashu = input("下载话数：")
    address = input("下载路径 如 D:\zuoye\zero：")
    url_list = []
    content = []
    h = 1
    p  = 1
    t_list = []
    for hua in range(1,int(huashu+1)):
        content = request_url(hua)
        t = Thread(target=download,args=(content,address,hua))
        t_list.append(t)
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()


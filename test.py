import requests, csv
from bs4 import BeautifulSoup
import time
from multiprocessing.dummy import Pool as ThreadPool

def downloader(url):

    res = []
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f'{url} is failed!')
        return len(res)

    print(f'{url} is parsing')

    html = BeautifulSoup(response.text,'html.parser')
    for instance in html.select('.instance_t'):
        print(instance.text)
        with open('test1.txt','a') as file_test:
            file_test.write(instance.text + '\n')

    for translate in html.select('.translation'):
        print(translate.text)

    for voice in html.select('.voiceLinkBox'):
        print(voice.a.get('href'))

            
              
    

   

if __name__ == '__main__':
    start_time = time.time()

    pool = ThreadPool(100)
    urls = []
    for i in range(10, 100):   
        urls.append(f'http://www.coelang.tufs.ac.jp/ja/zt/gmod/contents/instances/0{i}.html')
    responses = pool.map(downloader, urls)
    pool.close()
    pool.join()
     
    end_time = time.time()
    
    print(f'总共耗时 {end_time - start_time}, 抓取了 {sum(responses)} 条数据')
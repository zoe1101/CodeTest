'''
任务描述：
https://movie.douban.com/cinema/later/beijing/ 这个
页面描述了北京最近上映的电影，你能否通过 Python 得到这些电影的名称、上映时间和海报呢？这个页面的海报是缩小版的，我希望你能从具体的电影描述页面中抓取到海报。
'''


header={'user-agent':'Mozilla/5.0'}

'''
普通 同步版本
'''
# import requests
# from bs4 import BeautifulSoup
#

# def main():
#     url = "https://movie.douban.com/cinema/later/beijing/"
#     init_page = requests.get(url,headers=header).content
#     init_soup = BeautifulSoup(init_page, 'lxml')
#     all_movies = init_soup.find('div', id="showing-soon")
#     for each_movie in all_movies.find_all('div', class_="item"):
#         all_a_tag = each_movie.find_all('a')
#         all_li_tag = each_movie.find_all('li')
#         movie_name = all_a_tag[1].text
#         url_to_fetch = all_a_tag[1]['href']
#         movie_date = all_li_tag[0].text
#         response_item = requests.get(url_to_fetch,headers=header).content
#         soup_item = BeautifulSoup(response_item, 'lxml')
#         img_tag = soup_item.find('img')
#         print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))
#
# main()

'''
协程版本
'''

import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch_content(url):
    async with aiohttp.ClientSession(headers=header, connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = await fetch_content(url)
    init_soup = BeautifulSoup(init_page, 'lxml')
    movie_names, urls_to_fetch, movie_dates = [], [], []
    all_movies = init_soup.find('div', id="showing-soon")

    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')
        movie_names.append(all_a_tag[1].text)
        urls_to_fetch.append(all_a_tag[1]['href'])
        movie_dates.append(all_li_tag[0].text)
        tasks = [fetch_content(url) for url in urls_to_fetch]
        pages = await asyncio.gather(*tasks)

    for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
        soup_item = BeautifulSoup(page, 'lxml')
        img_tag = soup_item.find('img')
        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))


asyncio.run(main())
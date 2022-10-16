import json
import time
import requests as req
import tqdm as tqdm
from bs4 import BeautifulSoup
import lxml

data = { "data":
        []}
headers = {'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://hh.ru/?hhtmFrom=vacancy_search_list',
        'Referer': 'https://hh.ru/?hhtmFrom=vacancy_search_list',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.53',
        'sec-ch-ua': '"Chromium";v="102", "Opera";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',}

for page in range(1, 5):
        if page != 1:
                url = f'https://hh.ru/search/vacancy?text=python+разработчик&from=suggest_post&area=&page={page}&hhtmFrom=vacancy_search_list'
        else:
                url = 'https://hh.ru/search/vacancy?text=python+разработчик&from=suggest_post&area='
        resp = req.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, "lxml")
        tags = soup.find_all(attrs={'class':'serp-item__title'})
        for item in tqdm.tqdm(tags):
                time.sleep(2)
                url_job = item.attrs['href']
                resp_job = req.get(url_job, headers=headers)
                soup_job = soup = BeautifulSoup(resp_job.text, "lxml")
                tag_salary = soup.find(attrs={'class':'bloko-header-section-2 bloko-header-section-2_lite'})
                if tag_salary:
                        tag_salary = tag_salary.text
                else:
                        tag_salary = ''
                tag_region = soup.find(attrs={'data-qa':'vacancy-view-raw-address'})
                if tag_region:
                        tag_region = tag_region.text
                else:
                        tag_region = soup.find(attrs={'data-qa':'vacancy-view-location'}).text
                tag_workExperience = soup.find(attrs={'data-qa':'vacancy-experience'}).text

                data["data"].append({"title":item.text,
                                     "work experience:": tag_workExperience,
                                     "salary": tag_salary.replace(' ', '').strip(),
                                     "region": tag_region})
                with open("data.json", 'w') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import date


def abmission_crawler(link, university_list):
    requ = requests.get(link)
    soup = BeautifulSoup(requ.text, 'html.parser')

    info_block = soup.find_all('span', style='margin-top: 3px')
    title_block = soup.find_all('a', class_='s xst')
    university = []
    field = []
    upload_date = []
    full_title = []

    for i in info_block:
        if requ.status_code == 200:
            university.append(i.find('font', color='#00B2E8').text.lower())
            field.append(i.find('font', color='#F60').text)
            upload_date.append(i.find('font', color='brown').text)

    for t in title_block:
        if requ.status_code == 200:
            full_title.append(t.text)

    df = pd.DataFrame({'university':university, 'field':field, 'date':upload_date, 'full_title':full_title})
    df = df[(df['university'].isin(university_list)) & (df['field'] == 'DataScience/Analytics')]
    # (df['date']== date.today()) & 
    return df


def main():
    university_list = ['upenn', 'university of pennsylvania', 'nw', 'nwu', 'northwestern','northwestern university', 'nyu', 'new york university', 'columbia university', 'columbia', 'umich', 'university of michigan--annarbor', 'ubc', 'university of british columbia']
    df_list = []

    for n in range(1,5):
        url = f'https://www.1point3acres.com/bbs/forum.php?mod=forumdisplay&fid=82&orderby=dateline&filter=author&orderby=dateline&page={n}'
        df_list.append(abmission_crawler(url, university_list))

    return pd.concat(df_list).to_string(index=False)


if __name__ == "__main__":
   final_df = main()
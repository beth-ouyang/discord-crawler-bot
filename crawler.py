import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import date
import zipfile

def abmission_crawler(link, university_list):
    requ = requests.get(link)
    soup = BeautifulSoup(requ.text, 'html.parser')

    info_block = soup.find_all('th', class_='new')
    university = []
    field = []
    upload_date = []
    full_title = []

    for i in info_block:
      if requ.status_code == 200:
        span = i.find_all('span', style='margin-top: 3px')
        if len(span) >= 1:
          for j in span:
            university.append(j.find('font', color='#00B2E8').text.lower())
            field.append(j.find('font', color='#F60').text)
            upload_date.append(j.find('font', color='brown').text)
          
          full_title.append(i.find('a', class_='s xst').text)
        
    df = pd.DataFrame({'university':university, 'field':field, 'date':upload_date, 'full_title':full_title})
    df = df[(df['university'].isin(university_list)) & (df['field'] == 'DataScience/Analytics')]
    # (df['date']== date.today()) & 
    return df


def admission_main():
    university_list = ['upenn', 'university of pennsylvania', 'nw', 'nwu', 'northwestern','northwestern university', 'nyu', 'new york university', 'columbia university', 'columbia', 'umich', 'university of michigan--annarbor', 'ubc', 'university of british columbia']
    df_list = []

    for n in range(1, 5):
        url = f'https://www.1point3acres.com/bbs/forum.php?mod=forumdisplay&fid=82&orderby=dateline&filter=author&orderby=dateline&page={n}'
        df_list.append(abmission_crawler(url, university_list))

    return pd.concat(df_list)[['date', 'full_title']].to_string(index=False)

#######################################################

def line_emoji_download(link):
  requ = requests.get(link)
  soup = BeautifulSoup(requ.text, 'html.parser')
  
  emoji_list = soup.find_all('span', class_='mdCMN09Image FnPreview')
  emoji_url_list = []
  
  for e in emoji_list:
    if requ.status_code == 200:
      e = str(e)
      emoji_url_list.append(e.split('(')[-1].split(')')[0])

  zip_file = zipfile.ZipFile("line_emoji.zip", "w")
  for i in range(len(emoji_url_list)):
    url = emoji_url_list[i]
    response = requests.get(url)
    file_name = str(i) + "_" + url.split('?')[0].split('/')[-1]
    # write the content of each file to the zip file
    zip_file.writestr(file_name, response.content)
  
  # close the zip file
  zip_file.close()

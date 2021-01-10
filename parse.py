import telebot
import requests
import bs4

def covid():
    r = requests.get("https://irkobl.ru/coronavirus/").text
    data = bs4.BeautifulSoup(r, 'html.parser')
    url_last_news = data.find_all('div', class_="news-item")[0].find_all('a', href=True)[0]['href']
    r = requests.get("https://irkobl.ru"+url_last_news).text
    data = bs4.BeautifulSoup(r, 'html.parser')
    img_url = data.find_all('a', class_='fancybox', href=True)[0]['href']
    text = data.find_all('div', class_='news-detail')[0].text
    img = requests.get("https://irkobl.ru"+img_url).content
    date = text.split(" ")[0]

    return [img, text, date]
import requests
from bs4 import BeautifulSoup  # Bu kutub xona xtml dan kerakli textlarni ajratib olishga yordam beradi

cars = []

for i in range(1, 5):
    url = "https://avtoelon.uz/avto/gorod-tashkent/?price-currency"

    response = requests.get(url)  # responsdan kelyotgan textni oladi va wepsayt html da qilingani uchun

    soup = BeautifulSoup(response.text, 'html.parser')  # html.parser yozladi (xml) da yozladgan sitelarham bor
    container = soup.find_all('div', {
        'class': 'list-item'})  # A.Uz dagi hama elon cantenrlarni ajratyamiz (fine_all ) bita narsa kop marta kelsa ham hamasni oliberadi

    for car_info in container:  # harbir canteinerdan titlelarni ajratyamiz va ularni htmlsiz textlarni yani-
        try:
            title = car_info.find('span', {'class': 'a-el-info-title'}).text  # mashinalarni titleni olyamiz
            prise = car_info.find('span', {'class': 'price'}).text
            prise = prise.replace('Цена:', "").replace('y.e.', '')
            title_splite = title.split(',')

            position = None
            try:
                position = title_splite[1].replace('позиция', '')
            except:
                pass
            # print(f"nomi: {title}")
            # print(f'position: {position}')
            # print(f'prise: {prise}')
            temp = {
                "name": title,
                "position": position,
                "prise": prise
            }
            cars.append(temp)
        except:
            continue

for i in cars:
    print("request is start")
    r = requests.post("http://127.0.0.1:8000/cars/", data=i)
    print("request is done")
    print(r.text)

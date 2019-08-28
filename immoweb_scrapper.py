from time import sleep
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


# Unformated Link
LINK = 'https://www.immoweb.be/fr/recherche/{}/a-vendre?zips={}&minroom={}'
# Link to chromedriver
EXECUTABLE_PATH = 'C:\\Users\\bebxtaxaerk\\Downloads\\chromedriver_win32\\chromedriver.exe'
# zips
ZIPS = ['1620', '1630', '1180', '1160', '1950', '1830', '1831', '1150',
        '1200', '1933', '1140', '1040', '1050', '1780', '1020', '3080']
TYPES = ['maison', 'appartement']
NUMBER_ROOMS = '3'


class ImmoScrapper(object):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(
            executable_path=EXECUTABLE_PATH, options=options)
        self.wait = WebDriverWait(self.driver, 10)
    def scrape(self):
        items = self.scrape_immo_links()
        self.driver.quit()
        return items

    def scrape_immo_links(self):
        items = []
        page_sources = []
        for typ in TYPES:
            sleep(3)
            for zip in ZIPS:
                sleep(3)
                self.driver.get(LINK.format(typ, zip, NUMBER_ROOMS))
                has_next_button = True
                while has_next_button :
                    page_sources.append(self.driver.page_source)
                    next_button = self.driver.find_elements_by_class_name(
                        "next")
                    if next_button:
                        self.driver.execute_script(
                            "arguments[0].click();", next_button[0])
                        sleep(3)
                    else:
                        has_next_button = False
        for page_source in page_sources:
            items.extend(self.get_items(page_source))
        return items

    def get_items(self, page_source):
        soup = BeautifulSoup(page_source, 'lxml')
        items = []
        items_selector = soup.find_all('div', class_='result-xl')
        for item_selector in items_selector:
            item = self.get_item(item_selector)
            items.append(item)
        return items

    def get_item(self, item_selector):
        id = item_selector.attrs['data-id']
        title = item_selector.find('div', class_='title-bar-left')
        adress = item_selector.find('span', class_='result-adress')
        zip = adress.get_text(strip=True).split()[0] if adress else ''
        town = adress.get_text(strip=True).split()[1] if adress else ''
        price_euro = item_selector.find('div', class_='xl-price rangePrice')
        price = price_euro.get_text(strip=True)if price_euro else ''
        price = price.split()[0].replace('.', '') if price else ''
        surface_rooms = item_selector.find( 
            'div', class_='xl-surface-ch').get_text(strip=True)
        surface = surface_rooms.split()[0] if surface_rooms else ''
        number_of_rooms = surface_rooms.split(
        )[surface_rooms.split().index("ch.")-1] if surface_rooms else ''
        desc = item_selector.find('div', class_='xl-desc')
        item = [
            (id if id else ''),
            (title.get_text(strip=True) if title else ''),
            (zip if zip else ''),
            (town if town else ''),
            (price if price else ''),
            (surface if surface else ''),
            (number_of_rooms if number_of_rooms else ''),
            (desc.get_text(strip=True) if desc else '')
        ]

        return item


if __name__ == '__main__':
    SCRAPER = ImmoScrapper()
    ITEMS = SCRAPER.scrape()
    with open('immoweb.csv', mode='w', newline='') as employee_file:
        IMMO_WRITER = csv.writer(
            employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        IMMO_WRITER.writerow(
            ['Id', 'Title','Zip','Town', 'Price', 'Surface','NumberOfRooms', 'Description'])
        for row in ITEMS:
            IMMO_WRITER.writerow(row)

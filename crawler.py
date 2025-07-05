import time
from bs4 import BeautifulSoup
from selenium import webdriver
from config import GX_CITIES

def get_city_data_realtime(city_pinyin, db):
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('detach', True)
    option.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=option)

    y_list = ['1', '2','3','4']
    for y in y_list:
        for p in range(1, 100):
            url = f'https://{city_pinyin}.anjuke.com/sale/p{p}-y{y}/?from=fangjia'
            print(url)
            driver.get(url)
            time.sleep(3)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            soup_list = soup.select('.property')

            try:
                page_1 = soup.select('.page .active')[0].text.replace('\n', '').strip()
                if page_1 == '1' and p != 1:
                    break
            except:
                try:
                    end_text = soup.select('.list-guess-title')[0].text
                    if '猜你喜欢' in end_text:
                        break
                except:
                    pass

            for sl in soup_list:
                data = {}
                data['标题'] = sl.select('.property-content-title-name')[0].text
                data['户型'] = sl.select('.property-content-info-text.property-content-info-attribute')[0].text
                data['面积'] = ''
                data['方位'] = ''
                data['楼层'] = ''
                data['时间'] = ''
                dt_list = sl.select('.property-content-info-text')
                for dl in dt_list:
                    if '㎡' in dl.text:
                        data['面积'] = dl.text.replace('\n','').strip()
                    if any(x in dl.text for x in ['东','南','西','北']):
                        data['方位'] = dl.text.replace('\n','').strip()
                    if '层' in dl.text:
                        data['楼层'] = dl.text.replace('\n','').strip()
                    if '建造' in dl.text:
                        data['时间'] = dl.text.replace('\n','').strip()
                data['所属小区'] = sl.select('.property-content-info-comm-name')[0].text
                data['所属区域'] = sl.select('.property-content-info-comm-address')[0].text
                total_price_elements = sl.select('.property-price-total')
                data['总价'] = total_price_elements[0].text if total_price_elements else 'N/A'
                average_price_elements = sl.select('.property-price-average')
                data['均价'] = average_price_elements[0].text if average_price_elements else 'N/A'
                data['房龄'] = '2年内' if y == '1' else '2-5年'
                db.insert_data(data)  # 实时写入数据库
            print(p)
    driver.quit()

def get_all_gx_data_realtime(db):
    for city in GX_CITIES:
        print(f'正在爬取: {city}')
        get_city_data_realtime(city, db)



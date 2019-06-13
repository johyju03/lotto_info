from urllib.request import urlopen
from bs4 import BeautifulSoup


# 가장 최근 회차번호 가져오기 (크롤링)
def get_recent_draw_no():
    url = "https://dhlottery.co.kr/common.do?method=main"
    html = urlopen(url)
    source = html.read()
    html.close()

    soup = BeautifulSoup(source, "html.parser")
    draw_no = soup.find(id="lottoDrwNo")
    return draw_no.get_text()

# 최다 당첨 지점 정보 가져오기 (크롤링)
def parse_best_rank_places():
    url = "https://dhlottery.co.kr/store.do?method=topStoreRank&rank=1&pageGubun=L645"
    html = urlopen(url)
    source = html.read()
    html.close()

    soup = BeautifulSoup(source, "html.parser")
    rank_table = soup.find(class_="tbl_data_col")
    rank_tbody = rank_table.find("tbody")

    store_list = []

    for index, tr in enumerate(rank_tbody.find_all('tr')):
        td_list = tr.find_all('td')
        store_info = {
            'store_name': td_list[1].get_text().strip(),  # 상가명
            'count': td_list[2].get_text(),  # 당첨 회수
            'address': td_list[3].get_text()  # 지점주소
        }
        store_list.append(store_info)
        if index == 4:
            break
    result = {
        "stores": store_list,
    }
    return result

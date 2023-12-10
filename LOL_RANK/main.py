# created by Demi 2021-03-12
# pip install selenium
# pip install bs4

import include.config as ic
import time
from selenium import webdriver
from bs4 import BeautifulSoup   
import sqlite3
from typing import List, Dict
from datetime import datetime
import csv
import sys
from multiprocessing import Process, freeze_support
import os
import hashlib

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 시간 전역변수

class Crawler:
    user_header = "user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
    rank_list = []
    rank_template = ('name', 'tear', 'score', 'rate')
    #search_rank = ('CHALLENGER','GRANDMASTER')  # 이곳에 검색할 티어 추가 가능
    search_rank = ('CHALLENGER', 'GRANDMASTER','MASTER')  # 이곳에 검색할 티어 추가 가능
    #search_rank = ('CHALLENGER', 'GRANDMASTER','MASTER','DIAMOND - I')  # 이곳에 검색할 티어 추가 가능
    #search_rank = ('CHALLENGER', 'GRANDMASTER','MASTER','DIAMOND - I','DIAMOND - II')  # 이곳에 검색할 티어 추가 가능
    #search_rank = ('CHALLENGER', 'GRANDMASTER','MASTER','DIAMOND - I','DIAMOND - II','DIAMOND - III')  # 이곳에 검색할 티어 추가 가능
    def __init__(self): 
        self.options = None 

    def setup(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        #self.options.add_argument('headless')  # << 주석 해제시 헤드리스 모드
        self.options.add_argument(self.user_header)
        
  
    def run(self) -> List[Dict]:
        driver = webdriver.Chrome(ic.web_driver, options=self.options)
        driver.get(ic.target_url)
        hash = ''
        while True: 
            time.sleep(1.5)  # 네트워크 상태에 따라 0.5~ 1.5
            driver.implicitly_wait(10)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('table')
            while table is None:
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                table = soup.find('table')
            trs = table.find('tbody').find_all('tr')
            if len(self.rank_list) > 10 and trs[-1].find_all('td')[1].get_text() in self.rank_list[-1]['name']:
                break
            for tr in trs:
                td = tr.find_all('td')
                name = td[1].get_text()
                span = td[2].find_all('span')
                tear = span[0].get_text()
                score = span[1].get_text()
                span = td[3].find_all('span')
                rate = span[0].get_text() + '승 ' + span[1].get_text() + '패 ' + span[2].get_text()
                rank_source = [name,tear,score,rate]
                print(rank_source)
                input_rank = dict(zip(self.rank_template, rank_source))
                self.rank_list.append(input_rank)
            else:
                element = driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div[2]/div[2]/div[3]/div[4]/div')
                a = driver.execute_script("arguments[0].click();", element)
        print("크롤링 완료")
        print("조건에 맞는 대상 수 : {}".format(len(self.rank_list)))
        driver.quit()
        return self.rank_list


class DbWriter:
    sql1 = 'insert into rank values (:name,:tear,:rate,:score,:created_at)'
    sql2 = 'insert into created_idx(created_at) values (?)'
    sql3 = 'select * from created_idx order by id desc'

    def __init__(self, data: List):
        self.datas = data
        self.conn = sqlite3.connect(ic.db_path)
        self.cursor = self.conn.cursor()

    def run(self):
        print("DB 입력 시작")
        for data in self.datas:
            self.cursor.execute(self.sql1, data)
        self.cursor.execute(self.sql2, (now, ))
        self.cursor.execute(self.sql3)
        new = self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        print("작업 라벨 : {} 작업 시간 {}".format(new[0], new[1]))
        print("DB 입력 완료")


class DbSelect:
    select_sql = 'select * from created_idx'

    compare_sql = 'select name from rank where created_at = (select created_at from created_idx where id = ?) ' \
                  'except ' \
                  'select name from rank where created_at = (select created_at from created_idx where id = ?)'

    def __init__(self):
        self.compare_data1 = None
        self.compare_data2 = None
        self.conn = sqlite3.connect(ic.db_path)
        self.cursor = self.conn.cursor()

    @property
    def compare_data(self):
        return self.compare_data1, self.compare_data2

    def view(self):
        self.cursor.execute(self.select_sql)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        self.conn.close()

    def compare(self):
        self.cursor.execute(self.compare_sql, (self.compare_data2, self.compare_data1))
        rows = self.cursor.fetchall()
        file_name = 'compare' + str(self.compare_data1) + " to " + str(self.compare_data2) + '.csv'
        file = open(file_name, 'w', encoding='utf-8-sig', newline='')
        writer = csv.writer(file)
        writer.writerow(('name', ))
        for row in rows:
            print(row)
            writer.writerow(row)
        file.close()
        self.conn.close()


class CsvWriter:

    def __init__(self, data: List):
        self.filename = now.split(' ')[0] + '.csv'
        self.file = open(self.filename, 'w', encoding='utf-8-sig', newline='')
        self.writer = csv.writer(self.file)
        self.datas = data
        self.template = ['name', 'tear', 'score', 'rate']

    def run(self):
        print("CSV 작성 시작")
        self.writer.writerow(self.template)
        for data in self.datas:
            self.writer.writerow((data['name'], data['tear'], data['score'], data['rate']))
        self.file.close()
        print("CSV 작성 완료")
        print("CSV 경로는 : {}".format(str(os.getcwd()) + '\\' + self.filename))


def index_out(index):
    out_sql = 'select * from rank where created_at = (select created_at from created_idx where id = ?)'

    conn = sqlite3.connect(ic.db_path)
    cursor1 = conn.cursor()
    cursor1.execute(out_sql, (index, ))
    rows = cursor1.fetchall()
    file = open(index + ".csv", 'w', encoding='utf-8-sig', newline='')
    writer = csv.writer(file)
    writer.writerow(('name', 'tear', 'rate', 'score'))

    for row in rows:
        writer.writerow((row[0], row[1], row[2], row[3]))
    file.close()
    conn.close()


def db_clean():
    del_sql = "delete from rank"
    del_sql2 = 'delete from created_idx'
    update_sql = 'update sqlite_sequence set seq = 0'

    conn = sqlite3.connect(ic.db_path)
    cursor = conn.cursor()
    cursor.execute(del_sql)
    cursor.execute(del_sql2)
    cursor.execute(update_sql)
    conn.commit()
    conn.close()
    print("DB초기화 완료")



def guide():
    print("사용할 수 있는 명령어")
    print("1. --start : 크롤링 시작, DB기록, CSV작성")
    print("2. --list : 크롤링한 시간과 번호 출력")
    print("3. --compare num1 num2 : 크롤링한 시간, 번호를 이용해 요청사항 수행\n\n")
    print("4 --out num : 해당 번호에 유저를 csv 파일로 출력합니다")
    print("5 --clean : DB를 초기화 합니다")
    print("ex : python main.py --list\n")
    print("- - -output- - -")
    print("(1, '2021-03-12 00:24:50')")
    print("(2, '2021-03-12 00:25:00')")
    print("ex : python main.py --compare 1 2")


def main():
    print('크롤링 시작')
    start_time = time.time()
    crawler = Crawler()
    crawler.setup()
    data = crawler.run()
    #dbwriter = DbWriter(data=data)
    csvwriter = CsvWriter(data=data)

    #p1 = Process(target=dbwriter.run())
    p2 = Process(target=csvwriter.run())

    #p1.start()
    p2.start()
    #p1.join()
    p2.join()
    # dbwriter.run()
    # csvwriter.run()
    end_time = time.time()
    print('작업완료 소요시간 : {}'.format(end_time-start_time))


if __name__ == '__main__':
    freeze_support()
    argv = sys.argv
    if len(argv) >= 2:
        if argv[1] == "--start":
            main()
        elif argv[1] == "--list":
            DataList = DbSelect()
            DataList.view()
        elif argv[1] == "--compare":
            DataCompare = DbSelect()
            DataCompare.compare_data1 = argv[2]
            DataCompare.compare_data2 = argv[3]
            DataCompare.compare()
        elif argv[1] == "--out":
            index_out(argv[2])
        elif argv[1] == "--help":
            guide()
        elif argv[1] == "--clean":
            print("정말 초기화 합니까 ? (y/n)[n] : ")
            answer = input().upper()
            if answer == "":
                print("작업 취소")
                pass
            elif answer == "Y":
                print("DB 초기화 시작 ")
                db_clean()
            elif answer == "N":
                print("작업 취소")
                pass
            else:
                print("잘못된 입력입니다 작업을 취소합니다")
        else:
            print("잘못된 명령어 입니다")
    else:
        main()

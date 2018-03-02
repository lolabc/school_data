#coding:utf-8
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql

class seleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def testEle(self):
        currentpage=1
        maxpage=93
        index_url='http://gkcx.eol.cn/soudaxue/queryschool.html?page='
        db = pymysql.connect("localhost","root","root","school",charset='utf8')
        cursor = db.cursor()
    
        for i in range(currentpage, maxpage):
            page_url=index_url+str(i)
            driver = self.driver
            driver.get(page_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            # trs = soup.find_all('tr', {'class': 'lin-gettr'})
           
            elem = driver.find_element_by_class_name('lin-gettr')
            trs = soup.find_all('tr', class_='lin-gettr')
            for tr in trs:
                datalist=[]
                for td in tr.findAll('td'):
                     datalist.append(td.getText())
                print (datalist)
                try:
                    sql="""insert into college (name,city,edu_level,hot,category_hot) values('%s','%s','%s','%d','%s')""" % \
                         (datalist[0],datalist[1],datalist[2],int(datalist[3]),datalist[4])    
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()
         
        db.close()
    def tearDown(self):
        print ('down')

if __name__ == "__main__":
    unittest.main()

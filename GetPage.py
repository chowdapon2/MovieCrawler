from selenium import webdriver
import time
from bs4 import BeautifulSoup


driver = webdriver.PhantomJS('D:\Github\MovieCrawler\phantomjs.exe')
# driver.implicitly_wait(5)
# get()方法會一直等到頁面被完全加載，然後才會繼續程序
driver.get("https://medium.com/topic/popular")

# <h3 class="ui-h2 ui-xs-clamp2 ui-sm-clamp2">‘It Is Absurdly, Obscenely Common’: Incest Survivors Speak&nbsp;Out</h3>

# 打印網頁渲染後的源代碼
#print(driver.page_source)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
#print (soup.prettify())
print(soup.find_all('h3'))
# 打印獲取的文本內容
#print(data)

# 打印頁面標題：百度一下，你就知道
print(driver.title)

driver.quit()